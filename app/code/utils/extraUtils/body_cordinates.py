import json

import pandas as pd

df = pd.read_excel("character 5 body cordin.xlsx").to_dict()
clean_body_json = {}


print(df["body_cordinates"])

for body, head_size, body_cordinates in zip(
    df["name"].items(), df["head_size"].items(), df["body_cordinates"].items()
):
    print(head_size[1])
    if body != "nan":
        try:
            clean_body_json[body[1]] = {
                "head_size": [int(i) for i in head_size[1].split(",")],
                "head_position": [int(i) for i in body_cordinates[1].split(",")],
            }
        except:
            pass


with open("body_cordinations_character_5.json", "w") as outfile:
    json.dump(clean_body_json, outfile)
