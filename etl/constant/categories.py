
from etl.extract.read_csv import read_csv


categories = {
    "beverages": {
        "abb": "BEV",
        "name": "Beverages",
        "df": read_csv("data/beverages.csv"),
    },
    "butchers": {
        "abb": "BUT",
        "name": "Butchers",
        "df": read_csv("data/butchers.csv"),
    },
    "cea": {
        "abb": "CEA",
        "name": "Computers and electric accessories",
        "df": read_csv("data/computers_and_electric_accessories.csv"),
    },
    "ehe": {
        "abb": "EHE",
        "name": "Electric household essentials",
        "df": read_csv("data/electric_household_essentials.csv"),
    },
    "food": {"abb": "FOOD", "name": "Food", "df": read_csv("data/food.csv")},
    "furniture": {
        "abb": "FUR",
        "name": "Furniture",
        "df": read_csv("data/butchers.csv"),
    },
    "milk": {
        "abb": "MILK",
        "name": "Milk Products",
        "df": read_csv("data/milk_products.csv"),
    },
    "patisserie": {
        "abb": "PAT",
        "name": "Patisserie",
        "df": read_csv("data/patisserie.csv"),
    },
}