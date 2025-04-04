import json
import math

from webapp.constants import PREFIXES, ITEMS


def to_prefix(num: float | int, unit: str = "IGu", delimiter: str = "'"):
    # (complete, text, scientific, engineer)
    # (00_000_000, "00'000'000", "0.00x10^7", "00.0 Xunit")
    #num = int(num)
    if num == 0.0:
        return num, "0", "0", f"0 {unit}"
    if num < 1.0:
        return num, str(f"{num:.2f}"), str(f"{num:.2f}"), f"{num:.2f} {unit}"

    #num = int(num)
    e = int(math.log10(num))
    if e < 3:
        match math.floor(math.log10(abs(int(num)))) + 1:
            case 1:
                res = f"{num:.2f}"
            case 2:
                res = f"{num:.1f}"
            case _:
                res = f"{int(num)}"
        return num, str(res), str(res), f"{res} {unit}"
    else:
        # just a wee bit of fun
        text = str(int(num))
        text = "".join(list(reversed(
            delimiter.join(["".join(t) for t in [list(reversed(text))[x:x + 3] for x in range(0, len(text), 3)]]))))

        sci = f"{num:.2E}".replace("E+", " x10^")

        key = 3 * (e // 3)
        mult = PREFIXES[key][1]
        res = num / 10 ** key
        match math.floor(math.log10(abs(int(res)))) + 1:
            case 1:
                res = f"{res:.2f}"
            case 2:
                res = f"{res:.1f}"
            case _:
                res = f"{int(res)}"
        eng = f"{res} {mult}{unit}"

        return num, text, sci, eng


def read_result(file: str, real: bool = True):
    with open(file, "r") as f:
        res = json.load(f)

    res = res[-2:]
    production = "production_real" if real else "production"
    total = "total_real" if real else "total"

    # item: production_previous, production_current, total_previous, total_current
    ret = {
        item: {
            "production_previous": res[0][production][item],
            "production_current": res[-1][production][item],
            "total_previous": res[0][total][item],
            "total_current": res[-1][total][item],
        }
        for item in ITEMS.keys()
    }

    return ret  # pd.DataFrame.from_dict(ret)

def to_human(cur_prod: dict):
    items = {}
    for item, info in cur_prod.items():
        items[item] = ITEMS[item].copy()
        for key, value in info.items():
            items[item][key] = to_prefix(value * items[item]["ig_to_irl"], unit=items[item]["irl_unit"])

    return items

if __name__ == "__main__":
    print(read_result("webapp/production.json"))
    # tests = [1, 1024, 500000, 1048576, 50000000, 1073741824, 5000000000, 1099511627776, 5000000000000]
    # for t in tests:
    #     print(to_prefix(t))
