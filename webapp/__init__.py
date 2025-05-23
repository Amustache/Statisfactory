from pprint import pprint
from flask import Flask, render_template, request, url_for, redirect
from webapp.config import Config
from webapp.constants import ITEMS
from webapp.utilities import read_result, to_prefix, to_human, get_closest_funfact


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    print(f"Using {app.config['PARSED_SAVE_FILE']}")

    app.jinja_env.globals.update(to_prefix=to_prefix)

    @app.route("/")
    def main():
        # Get latest prod file
        cur_prod = read_result(app.config["PARSED_SAVE_FILE"])
        # Filter out when no ressource
        cur_prod = {k: v for k, v in cur_prod.items() if v["total_current"] > 0.0}

        # Add information
        item_keys = list(cur_prod.keys())
        for item in item_keys:
            cur_prod[item].update(ITEMS[item])

        # Check for item validity
        cur_item = request.args.get("cur_item")
        if item_keys:
            if cur_item not in item_keys:
                cur_item = item_keys[0]
                return redirect(url_for("main", cur_item=cur_item))
        else:
            # No production, no valid item
            cur_item = None

        if cur_item:
            next_item = item_keys[(item_keys.index(cur_item) + 1) % len(item_keys)]
            average_total = cur_prod[cur_item]["ig_to_irl"] \
                            * (cur_prod[cur_item]["total_previous"] + cur_prod[cur_item]["total_current"]) / 2
            funfact = get_closest_funfact(app.config["FUNFACTS_FILE"], cur_item, average_total)
        else:
            next_item = None
            funfact = None

        return render_template(
            "main.html",
            items=cur_prod,
            cur_item=cur_item,
            next_item=next_item,
            elapsing=5 if app.config["DEBUG"] else app.config["TIME_BETWEEN_SAVES"],
            funfact=funfact,
        )

    return app
