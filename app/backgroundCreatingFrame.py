import json
import os
from code.editImage.addingImages import adding_image, zoom_at

import numpy as np
from PIL import Image

mypath = "./json/character_body_cordinates/"
files = [f for f in os.listdir(mypath)]
character_body_cordination_data = {}
for each_file in files:
    character_number = each_file.split("_")[-1].split(".")[0]
    if character_number not in character_body_cordination_data:
        character_body_cordination_data[character_number] = {}
        character_body_cordination_data[character_number] = json.load(
            open(mypath + each_file)
        )


mypath = "./json/background_extra/"
files = [f for f in os.listdir(mypath)]
extra_image_data = {}
for each_file in files:
    character_number = each_file.split("_")[-1].split(".")[0]
    if character_number not in extra_image_data:
        extra_image_data[character_number] = {}
        extra_image_data[character_number] = json.load(open(mypath + each_file))

# print(extra_image_data)


def adding_background(body_path, background_path, frame_name, rotation=0, zoom=0):
    character_number = background_path.split("/")[4].split("_")[-1]
    screen_mode = background_path.split("/")[3]
    # head = Image.open(head_path)

    # body = Image.open(body_path)
    background = Image.open(background_path)

    # a check you want to add something on background or not
    if character_body_cordination_data[character_number][screen_mode]["addition"]:

        # adding image before the main character
        if extra_image_data[character_number][screen_mode]["extra_before"]:
            pass

        new_image = adding_image(
            background,
            body_path,
            location=character_body_cordination_data[character_number][screen_mode][
                "body_position"
            ],
            rotation=rotation,
            mirror=character_body_cordination_data[character_number][screen_mode][
                "mirror"
            ],
            size_cordinates=character_body_cordination_data[character_number][
                screen_mode
            ]["body_size"],
        )

        # adding image after the main character
        if extra_image_data[character_number][screen_mode]["extra_after"]:
            for each_extra_image in extra_image_data[character_number][screen_mode][
                "extra_after"
            ]:
                new_image = adding_image(
                    new_image,
                    Image.open(each_extra_image["image"]),
                    location=each_extra_image["location"],
                    rotation=rotation,
                    mirror=False,
                    size_cordinates=each_extra_image["size"],
                )

        if zoom > 0 and zoom < 8:
            print("character_number : ", character_number)
            print(character_body_cordination_data[character_number][screen_mode])
            x = character_body_cordination_data[character_number][screen_mode][
                "zoom_point"
            ][0]
            y = character_body_cordination_data[character_number][screen_mode][
                "zoom_point"
            ][1]
            new_image = zoom_at(new_image, x, y, zoom)
        # new_image.show()
        new_image.save(f"./frames/backgroundFrames/{frame_name}.png")
        # return new_image
    else:
        background.save(f"./frames/backgroundFrames/{frame_name}.png")


#  #how to use this function:
# body = "./frames/bodyFrames/15.png"

# background = "./images/background/office/character_1/wall.png"


# new = adding_background(body_path=body, background_path=background, frame_name='testing')
