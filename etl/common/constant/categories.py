from pyspark.sql import SparkSession

from etl.common.extract.read_csv import read_csv


def categories(spark: SparkSession) -> dict:
    return {
        "beverages": {
            "abb": "BEV",
            "name": "Beverages",
            "df": read_csv("data/beverages.csv", spark),
        },
        "butchers": {
            "abb": "BUT",
            "name": "Butchers",
            "df": read_csv("data/butchers.csv", spark),
        },
        "cea": {
            "abb": "CEA",
            "name": "Computers and electric accessories",
            "df": read_csv("data/computers_and_electric_accessories.csv", spark),
        },
        "ehe": {
            "abb": "EHE",
            "name": "Electric household essentials",
            "df": read_csv("data/electric_household_essentials.csv", spark),
        },
        "food": {"abb": "FOOD", "name": "Food", "df": read_csv("data/food.csv", spark)},
        "furniture": {
            "abb": "FUR",
            "name": "Furniture",
            "df": read_csv("data/butchers.csv", spark),
        },
        "milk": {
            "abb": "MILK",
            "name": "Milk Products",
            "df": read_csv("data/milk_products.csv", spark),
        },
        "patisserie": {
            "abb": "PAT",
            "name": "Patisserie",
            "df": read_csv("data/patisserie.csv", spark),
        },
    }
