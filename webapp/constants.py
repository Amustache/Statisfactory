import pandas as pd

PREFIXES = {
    3: ("kilo", "k"),
    6: ("mega", "M"),
    9: ("giga", "G"),
    12: ("tera", "T"),
    15: ("peta", "P"),
    18: ("exa", "E"),
    21: ("zetta", "Z"),
    24: ("yotta", "Y"),
    27: ("ronna", "R"),
    30: ("quetta", "Q"),
}

ITEMS = {
    "iron": {
        "name": "Minerai de fer",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 0.012,
    },
    "copper": {
        "name": "Minerai de cuivre",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 0.012,
    },
    "limestone": {
        "name": "Calcaire",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "coal": {
        "name": "Charbon",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 10.24,
    },
    "water": {
        "name": "Eau",
        "ig_unit": "m3",
        "irl_unit": "m3",
        "ig_to_irl": 1,  # Correct
    },
    "oil": {
        "name": "Pétrol brut",
        "ig_unit": "m3",
        "irl_unit": "t",
        "ig_to_irl": 0.4,
    },
    "caterium": {
        "name": "Minerai de catérium (or)",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "bauxite": {
        "name": "Bauxite",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "quartz": {
        "name": "Quartz brut",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "sulfur": {
        "name": "Sulfure",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "uranium": {
        "name": "Uranium",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
    "biomass": {
        "name": "Bois (Biomasse)",
        "ig_unit": "unit",
        "irl_unit": "t",
        "ig_to_irl": 1,
    },
}

MULTIPLIERS = {
    0.25: "L'équivalent du quart de ",
    0.5: "L'équivalent de la moitié de ",
    0.75: "L'équivalent des trois quarts de ",
    1: "L'équivalent de ",
    2: "L'équivalent de 2 fois ",
    3: "L'équivalent de 3 fois ",
    4: "L'équivalent de 4 fois ",
    5: "L'équivalent de 5 fois ",
    6: "L'équivalent de 6 fois ",
    7: "L'équivalent de 7 fois ",
    8: "L'équivalent de 8 fois ",
    9: "L'équivalent de 9 fois ",
    10: "L'équivalent de 10 fois ",
}
