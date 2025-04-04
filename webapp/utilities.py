import csv
import json
import math
import random
from urllib.parse import urlparse

import pandas as pd
import requests

from webapp.constants import PREFIXES, ITEMS, MULTIPLIERS


def to_prefix(num: float | int, unit: str = "IGu", delimiter: str = " "):
    # (complete, text, scientific, engineer)
    # (00_000_000, "00'000'000", "0.00x10^7", "00.0 Xunit")
    # num = int(num)
    if num == 0.0:
        return num, "0", "0", f"0 {unit}"
    if num < 1.0:
        return num, str(f"{num:.2f}"), str(f"{num:.2f}"), f"{num:.2f} {unit}"

    # num = int(num)
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


CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTT0gbP8t-D1dW6tAErn2WYvfJ-e0KokkGiFxXLAet3QC5fQGai9afTuv_082jFZU7luQ7SK7Pfccu5/pub?gid=1978893223&single=true&output=csv"


# from webapp.utilities import download_expand_and_save_funfacts, CSV_URL;download_expand_and_save_funfacts(CSV_URL, "funfacts.csv")
def download_expand_and_save_funfacts(csv_url: str, save_path: str):
    with requests.Session() as s:
        # Get data
        download = s.get(csv_url)
        decoded_content = download.content.decode("utf-8")
        cr = list(csv.reader(decoded_content.splitlines(), delimiter=','))

        # Augment data
        res = []
        for c in cr[1:]:
            for value, previous in MULTIPLIERS.items():
                tmp = c.copy()
                tmp[1] = float(tmp[1]) * value
                tmp.append(previous)
                res.append(tmp)

        # Save data
        with open(save_path, "w") as f:
            write = csv.writer(f)

            write.writerow(cr[0] + ["previous"])
            write.writerows(res)


def get_closest_funfact(file: str, item: str, value: float | int):
    df = pd.read_csv(file, header=0)
    df = df.astype({"value": float, "source": str})
    df = df.loc[df["item"] == item].reset_index(drop=True)
    df_sort = df.iloc[(df["value"] - value).abs().argsort()[:2]]
    try:
        ind = df_sort.index.tolist()[0]
    except IndexError:
        return None

    return {
        "previous": df.iloc[ind]["previous"],
        "main": df.iloc[ind]["main"],
        "value": df.iloc[ind]["value"],
        "source": urlparse(df.iloc[ind]["source"]).netloc if df.iloc[ind]["source"] else None,
        "illustration": df.iloc[ind]["illustration"],
    }
