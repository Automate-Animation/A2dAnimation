import json
import os
from code.editImage.addingImages import adding_image
from os.path import isfile, join

import numpy as np
from PIL import Image

mypath = "./json/character_head_cordinates/"
files = [f for f in os.listdir(mypath)]
# print(files)
character_body_cordination_data = {}
for each_file in files:
    character_number = each_file.split("_")[-1].split(".")[0]
    if character_number not in character_body_cordination_data:
        character_body_cordination_data[character_number] = {}
        character_body_cordination_data[character_number] = json.load(
            open(mypath + each_file)
        )

# print(character_body_cordination_data)


def adding_head_and_body(head, body_path, frame_name, rotation=0):
    # "./images/body/character_2/aa6.png"
    # finder = "character_"
    # x = body_path.find(finder)

    character_number = body_path.split("/")[3].split("_")[-1]
    # head = Image.open(head_path)

    body_image_name = body_path.split("/")[-1].split(".")[0]
    body = Image.open(body_path)

    new_image = adding_image(
        body,
        head,
        location=character_body_cordination_data[character_number][body_image_name][
            "head_position"
        ],
        rotation=rotation,
        mirror=False,
        size_cordinates=character_body_cordination_data[character_number][
            body_image_name
        ]["head_size"],
    )

    # new_image.show()
    # new_image.save(f'./frames/bodyFrames/{frame_name}.png')
    return new_image


#  #how to use this function:
# head = "./frames/headFrames/15.png"

# body = "./images/body/Character_3/aa1.png"


# new = adding_head_and_body(head_path=head, body_path=body, frame_name='testing', rotation=-9)
