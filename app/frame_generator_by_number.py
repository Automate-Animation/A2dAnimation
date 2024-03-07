# import pandas as pd
import argparse
import csv
import json
import os
import random
from code.utils.utils import (
    key_generator,
    path_creation_for_background,
    path_creation_for_body,
    path_creation_for_eyes,
    path_creation_for_head,
    path_creation_for_mouth,
    path_creation_for_mouth_reaction,
)
from code.utils.valueCreator import (
    random_value_genrator,
    random_value_genrator_for_body,
)

import pandas as pd


args = argparse.Namespace


def parse_args():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-f", "--file", help="csv file name")

    # Read arguments from command line
    return parser.parse_args()


# from backgroundCreatingFrame import adding_background
# from bodyCreatingFrame import adding_head_and_body
# from headCreatingFrame import adding_eyes_and_mouth
def main():
    print("Main....!")
    global args

    header = [
        "frame",
        "character",
        "emotion",
        "phonem",
        "blinking_choice",
        "eyes_emotion_choice",
        "intensity",
        "eyes_position",
        "mouth_image_path",
        "pause",
        "word",
        "head_direction",
        "screen_mode",
        "background_type",
        "background_name",
        "body_action",
        "body_path",
        "reaction_bool",
        "reaction",
        "zoom",
    ]

    args = parse_args()
    if args.file:
        try:
            frame_data = open(f"./json/json_data_for_frame/{args.file}.json")
        except Exception as e:
            print(e)
    else:
        print("Please Provide -f file_name from json_data_for_frame folder")

    frames_json = json.load(frame_data)

    if frames_json["MODE"] == "gentle":
        f = open("./json/gentle_phonemes.json")
    else:
        f = open("./json/phonemes_json.json")

    phonemes = json.load(f)

    # face = "./images/head/character_2.png"

    eye_emotion = emotion = frames_json["fragments"][0]["emotion"]
    eyes_position_choice = frames_json["fragments"][0]["eyes_direction"]
    intensity_choice = frames_json["fragments"][0]["intensity"]
    character = frames_json["fragments"][0]["character"]
    head_direction = frames_json["fragments"][0]["head_direction"]
    screen_mode = frames_json["fragments"][0]["screen_mode"]
    body_action = frames_json["fragments"][0]["body_action"]
    reaction_bool = frames_json["fragments"][0]["reaction_bool"]
    reaction = frames_json["fragments"][0]["emotion"]
    zoom = frames_json["fragments"][0]["zoom"]

    BLINKING = 80
    HEAD_ROTATION = 60

    background_type = frames_json["fragments"][0]["screen_mode"]
    background_name = "wall"

    CHANGE_INTENSITY_SECOUND = 5
    CHANGE_INTENSITY_SECOUND = CHANGE_INTENSITY_SECOUND * 24  # convert to frames
    # CHANGE_INTENSITY_SECOUND = CHANGE_INTENSITY_SECOUND * 2 #  cuz half for intensity heigh and half for intensity low

    frame_counter = 0

    with open("frame_info.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        while frame_counter <= frames_json["TOTAL_VIDEO_FRAMES"]:
            # if frame_counter%(CHANGE_INTENSITY_SECOUND*2) < CHANGE_INTENSITY_SECOUND:
            #     intensity_choice = False
            # else:
            #     intensity_choice = True
            for each_fagment in frames_json["fragments"]:

                if (
                    frame_counter >= each_fagment["init_frame"]
                    and frame_counter <= each_fagment["final_frame"]
                ):
                    print(frame_counter, " matched with ")
                    for phoneme, number_of_frame in each_fagment[
                        "phonemes_frame"
                    ].items():
                        print(phoneme, " : ", number_of_frame)
                        if phonemes.get(phoneme):
                            phonem_dic = phonemes.get(phoneme)
                            emotion = [
                                "happy"
                                if each_fagment["emotion"] in ["happy", "content"]
                                else "sad"
                            ][0]
                            if each_fagment["reaction_bool"]:
                                mouth_path = path_creation_for_mouth_reaction(
                                    each_fagment["character"], each_fagment["emotion"]
                                )
                            else:
                                mouth_path = path_creation_for_mouth(
                                    each_fagment["character"], emotion
                                )
                                mouth_path = mouth_path + phonem_dic[emotion]

                            blinking_choice = "not_blinking"
                            eyes_position_choice = each_fagment["eyes_direction"]

                            eyes_emotion_choice = each_fagment["emotion"]
                            eye_emotion = each_fagment["emotion"]
                            intensity_choice = each_fagment["intensity"]
                            character = each_fagment["character"]
                            head_direction = each_fagment["head_direction"]
                            screen_mode = each_fagment["screen_mode"]
                            background_type = each_fagment["screen_mode"]
                            body_action = each_fagment["body_action"]
                            reaction_bool = each_fagment["reaction_bool"]
                            reaction = each_fagment["emotion"]
                            zoom = each_fagment["zoom"]

                            for number in range(int(number_of_frame)):
                                print(frame_counter, "emotions")
                                data = [
                                    frame_counter,
                                    character,
                                    each_fagment["emotion"],
                                    phoneme,
                                    blinking_choice,
                                    eyes_emotion_choice,
                                    intensity_choice,
                                    eyes_position_choice,
                                    mouth_path,
                                    False,
                                    each_fagment["lines"][0],
                                    head_direction,
                                    screen_mode,
                                    background_type,
                                    background_name,
                                    body_action,
                                    "",
                                    reaction_bool,
                                    reaction,
                                    zoom,
                                ]
                                writer.writerow(data)
                                frame_counter += 1

            print(frame_counter)
            if reaction_bool:
                mouth_path = path_creation_for_mouth_reaction(character, emotion)
            else:
                if emotion == "happy":
                    # ./images/mouth/character_1/happy/m_b_close_h.png
                    mouth_path = (
                        f"./images/mouth/character_{character}/happy/m_b_close_h.png"
                    )
                else:
                    mouth_path = (
                        f"./images/mouth/character_{character}/sad/m_b_close_s.png"
                    )

            blinking_choice = "not_blinking"
            # eyes_position_choice = random.choices(["L", "R", "M"], weights=(15, 15, 70))[0]

            eyes_emotion_choice = eye_emotion

            data = [
                frame_counter,
                character,
                emotion,
                "",
                blinking_choice,
                eyes_emotion_choice,
                intensity_choice,
                eyes_position_choice,
                mouth_path,
                True,
                "",
                head_direction,
                screen_mode,
                background_type,
                background_name,
                body_action,
                "",
                reaction_bool,
                reaction,
                zoom,
            ]
            writer.writerow(data)
            frame_counter += 1

    ########################################           L, R and M strating                #############################################################
    data = pd.read_csv("frame_info.csv")
    total_frams = data.shape[0]
    # frames_for_L = total_frams*70//100

    # frames_for_M = total_frams*30//100
    # new_total = frames_for_L+ frames_for_M
    # difference = total_frams - new_total
    # if new_total < total_frams:
    #     frames_for_L += difference
    # elif new_total > total_frams:
    #     frames_for_L -= difference
    # else:
    #     pass
    # frms_after_shuffling = 240
    # my_list = []
    # for i in range(1,total_frams+1):
    #     significant_value = i%frms_after_shuffling
    #     if significant_value <= 192 : # for main eye contact there is 8 sec thus frames = 8*24
    #         my_list.append('L')
    # #         print(i,'L')
    #     else:
    #         my_list.append('M') # the rest which is
    # #         print(i,'M')

    # my_list= random_value_genrator(total_frams,difference=30,list_of_values=['L','M',"R"])

    # data.drop(columns=['eyes_position'])
    # data['eyes_position'] = my_list

    ########################################           L, R and M ending                #############################################################

    ########################################           eye path starting                #############################################################

    data["eye_path"] = data.apply(
        lambda x: path_creation_for_eyes(
            character_number=x.character,
            eyes_type=x.blinking_choice,
            eyes_emotion=x.eyes_emotion_choice,
            intensity=x.intensity,
            eyes_position=x.eyes_position,
        ),
        axis=1,
    )

    ########################################           eye path ending                #############################################################

    ########################################           blinking starting                #############################################################

    counter = 0
    inner_counter = 0
    head_rotation = []
    HEAD_ROTATION = 60
    head_rotation_choice = 0

    character = "-"
    body_action = "-"
    for i, each_data in enumerate(data.eye_path):
        if counter >= BLINKING and counter < BLINKING + 5:

            counter += 1
            inner_counter += 1

            list_of_path = each_data.split("/")
            if list_of_path[4] != "side_eyes_blinking":
                list_of_path[4] = "side_eyes_blinking"

            if inner_counter == 1:
                print("first")

            elif inner_counter == 2:
                list_of_path[-1] = "02" + ".png"
            elif inner_counter == 3:
                list_of_path[-1] = "03" + ".png"
            elif inner_counter == 4:
                list_of_path[-1] = "04" + ".png"
            elif inner_counter == 5:
                # print("last")
                inner_counter = 0
            print("/".join(list_of_path))
            data.eye_path[i] = "/".join(list_of_path)
        elif counter >= BLINKING + 5:
            print("reset")
            counter = 0
        else:
            counter += 1

        # head rotation
        if i % HEAD_ROTATION == HEAD_ROTATION - 1:
            head_rotation_choice = random.choices(
                [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                weights=(40, 20, 20, 20, 60, 70, 60, 20, 20, 20, 40),
            )[0]
        head_rotation.append(head_rotation_choice)

        # body path
        if data.character[i] != character or data.body_action[i] != body_action:
            character = data.character[i]
            body_action = data.body_action[i]
            path = path_creation_for_body(data.character[i], data.body_action[i])
            files = [f for f in os.listdir(path)]
            image_name = random.choice(files)
            path = path + "/" + image_name

        data["body_path"][i] = path

    data["head_rotation"] = head_rotation
    ########################################           blinking end                #############################################################

    ########################################           head end                #############################################################

    data["head_path"] = data.apply(
        lambda x: path_creation_for_head(
            character_number=x.character, direction=x.head_direction
        ),
        axis=1,
    )

    ########################################           head end                #############################################################

    ########################################           body end                #############################################################

    # list_of_body = random_value_genrator_for_body(
    #     number_of_value=total_frams, difference=100, list_of_values=['a', 'aa'])
    # data['body_action'] = list_of_body

    # data["body_path"] = data.apply(lambda x: path_creation_for_body(
    #                                character_number=x.character,
    #                                body_action=x.body_action), axis=1)

    ########################################           body end                #############################################################

    ########################################           background end                #############################################################

    data["background_path"] = data.apply(
        lambda x: path_creation_for_background(
            character_number=x.character,
            background_type=x.background_type,
            background_name=x.background_name,
        ),
        axis=1,
    )

    ########################################           background end                #############################################################

    ########################################           key end                #############################################################

    data["key"] = data.apply(
        lambda x: key_generator(
            str(x.character),
            str(x.emotion),
            str(x.phonem),
            str(x.eye_path),
            str(x.intensity),
            str(x.eyes_position),
            str(x.head_direction),
            str(x.screen_mode),
            str(x.background_type),
            str(x.background_name),
            str(x.body_action),
            str(x.body_path),
            str(x.head_rotation),
            str(x.mouth_image_path),
            str(x.zoom),
        ),
        axis=1,
    )

    ########################################           key end                #############################################################

    data.to_csv("new_LMR.csv")


# counter =0
# for eye, mouth, face, body in zip(data.eye_path, data.mouth_image_path, data.face_path, data.body_path):
#     head = adding_eyes_and_mouth(face_path=face, eye_path=eye, mouth_path=mouth, frame_name=counter)
#     body = adding_head_and_body(head,body,  frame_name=counter)
#     # background = "./images/background/simple/1.jpg"
#     # adding_background(body_path=body, background_path=background,  frame_name=counter)
#     counter += 1


def adding_frame_data(frame_data):
    print("add_extra_info....!")
    global args

    header = [
        "frame",
        "character",
        "emotion",
        "phonem",
        "blinking_choice",
        "eyes_emotion_choice",
        "intensity",
        "eyes_position",
        "mouth_image_path",
        "pause",
        "word",
        "head_direction",
        "screen_mode",
        "background_type",
        "background_name",
        "body_action",
        "body_path",
        "reaction_bool",
        "reaction",
        "zoom",
    ]

    # frames_json = json.load(frame_data)
    frames_json = frame_data

    if frames_json["MODE"] == "gentle":
        f = open("./json/gentle_phonemes.json")
    else:
        f = open("./json/phonemes_json.json")

    phonemes = json.load(f)

    eye_emotion = emotion = frames_json["fragments"][0]["emotion"]
    eyes_position_choice = frames_json["fragments"][0]["eyes_direction"]
    intensity_choice = frames_json["fragments"][0]["intensity"]
    character = frames_json["fragments"][0]["character"]
    head_direction = frames_json["fragments"][0]["head_direction"]
    screen_mode = frames_json["fragments"][0]["screen_mode"]
    body_action = frames_json["fragments"][0]["body_action"]
    reaction_bool = frames_json["fragments"][0]["reaction_bool"]
    reaction = frames_json["fragments"][0]["emotion"]
    zoom = frames_json["fragments"][0]["zoom"]

    BLINKING = 80
    HEAD_ROTATION = 60

    background_type = frames_json["fragments"][0]["screen_mode"]
    background_name = "wall"

    CHANGE_INTENSITY_SECOUND = 5
    CHANGE_INTENSITY_SECOUND = CHANGE_INTENSITY_SECOUND * 24  # convert to frames
    # CHANGE_INTENSITY_SECOUND = CHANGE_INTENSITY_SECOUND * 2 #  cuz half for intensity heigh and half for intensity low

    frame_counter = 0

    with open("frame_info.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        while frame_counter <= frames_json["TOTAL_VIDEO_FRAMES"]:
            # if frame_counter%(CHANGE_INTENSITY_SECOUND*2) < CHANGE_INTENSITY_SECOUND:
            #     intensity_choice = False
            # else:
            #     intensity_choice = True
            for each_fagment in frames_json["fragments"]:

                if (
                    frame_counter >= each_fagment["init_frame"]
                    and frame_counter <= each_fagment["final_frame"]
                ):
                    print(frame_counter, " matched with ")
                    for phoneme, number_of_frame in each_fagment[
                        "phonemes_frame"
                    ].items():
                        print(phoneme, " : ", number_of_frame)
                        if phonemes.get(phoneme):
                            phonem_dic = phonemes.get(phoneme)
                            emotion = [
                                "happy"
                                if each_fagment["emotion"] in ["happy", "content"]
                                else "sad"
                            ][0]
                            if each_fagment["reaction_bool"]:
                                mouth_path = path_creation_for_mouth_reaction(
                                    each_fagment["character"], each_fagment["emotion"]
                                )
                            else:
                                mouth_path = path_creation_for_mouth(
                                    each_fagment["character"], emotion
                                )
                                mouth_path = mouth_path + phonem_dic[emotion]

                            blinking_choice = "not_blinking"
                            eyes_position_choice = each_fagment["eyes_direction"]

                            eyes_emotion_choice = each_fagment["emotion"]
                            eye_emotion = each_fagment["emotion"]
                            intensity_choice = each_fagment["intensity"]
                            character = each_fagment["character"]
                            head_direction = each_fagment["head_direction"]
                            screen_mode = each_fagment["screen_mode"]
                            background_type = each_fagment["screen_mode"]
                            body_action = each_fagment["body_action"]
                            reaction_bool = each_fagment["reaction_bool"]
                            reaction = each_fagment["emotion"]
                            zoom = each_fagment["zoom"]

                            for number in range(int(number_of_frame)):
                                print(frame_counter, "emotions")
                                data = [
                                    frame_counter,
                                    character,
                                    each_fagment["emotion"],
                                    phoneme,
                                    blinking_choice,
                                    eyes_emotion_choice,
                                    intensity_choice,
                                    eyes_position_choice,
                                    mouth_path,
                                    False,
                                    each_fagment["lines"][0],
                                    head_direction,
                                    screen_mode,
                                    background_type,
                                    background_name,
                                    body_action,
                                    "",
                                    reaction_bool,
                                    reaction,
                                    zoom,
                                ]
                                writer.writerow(data)
                                frame_counter += 1

            print(frame_counter)
            if reaction_bool:
                mouth_path = path_creation_for_mouth_reaction(character, emotion)
            else:
                if emotion == "happy":
                    # ./images/mouth/character_1/happy/m_b_close_h.png
                    mouth_path = (
                        f"./images/mouth/character_{character}/happy/m_b_close_h.png"
                    )
                else:
                    mouth_path = (
                        f"./images/mouth/character_{character}/sad/m_b_close_s.png"
                    )

            blinking_choice = "not_blinking"

            eyes_emotion_choice = eye_emotion

            data = [
                frame_counter,
                character,
                emotion,
                "",
                blinking_choice,
                eyes_emotion_choice,
                intensity_choice,
                eyes_position_choice,
                mouth_path,
                True,
                "",
                head_direction,
                screen_mode,
                background_type,
                background_name,
                body_action,
                "",
                reaction_bool,
                reaction,
                zoom,
            ]
            writer.writerow(data)
            frame_counter += 1

    ########################################           L, R and M strating                #############################################################
    data = pd.read_csv("frame_info.csv")
    # total_frams = data.shape[0]

    ########################################           L, R and M ending                #############################################################

    ########################################           eye path starting                #############################################################

    data["eye_path"] = data.apply(
        lambda x: path_creation_for_eyes(
            character_number=x.character,
            eyes_type=x.blinking_choice,
            eyes_emotion=x.eyes_emotion_choice,
            intensity=x.intensity,
            eyes_position=x.eyes_position,
        ),
        axis=1,
    )

    ########################################           eye path ending                #############################################################

    ########################################           blinking starting                #############################################################

    counter = 0
    inner_counter = 0
    head_rotation = []
    HEAD_ROTATION = 60
    head_rotation_choice = 0

    character = "-"
    body_action = "-"
    for i, each_data in enumerate(data.eye_path):
        if counter >= BLINKING and counter < BLINKING + 5:

            counter += 1
            inner_counter += 1

            list_of_path = each_data.split("/")
            if list_of_path[4] != "side_eyes_blinking":
                list_of_path[4] = "side_eyes_blinking"

            if inner_counter == 1:
                print("first")

            elif inner_counter == 2:
                list_of_path[-1] = "02" + ".png"
            elif inner_counter == 3:
                list_of_path[-1] = "03" + ".png"
            elif inner_counter == 4:
                list_of_path[-1] = "04" + ".png"
            elif inner_counter == 5:
                # print("last")
                inner_counter = 0
            print("/".join(list_of_path))
            data.eye_path[i] = "/".join(list_of_path)
        elif counter >= BLINKING + 5:
            print("reset")
            counter = 0
        else:
            counter += 1

        # head rotation
        if i % HEAD_ROTATION == HEAD_ROTATION - 1:
            head_rotation_choice = random.choices(
                [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
                weights=(40, 20, 20, 20, 60, 70, 60, 20, 20, 20, 40),
            )[0]
        head_rotation.append(head_rotation_choice)

        # body path
        if data.character[i] != character or data.body_action[i] != body_action:
            character = data.character[i]
            body_action = data.body_action[i]
            path = path_creation_for_body(data.character[i], data.body_action[i])
            files = [f for f in os.listdir(path)]
            image_name = random.choice(files)
            path = path + "/" + image_name

        data["body_path"][i] = path

    data["head_rotation"] = head_rotation
    ########################################           blinking end                #############################################################

    ########################################           head end                #############################################################

    data["head_path"] = data.apply(
        lambda x: path_creation_for_head(
            character_number=x.character, direction=x.head_direction
        ),
        axis=1,
    )

    ########################################           head end                #############################################################

    ########################################           body end                #############################################################

    ########################################           body end                #############################################################

    ########################################           background end                #############################################################

    data["background_path"] = data.apply(
        lambda x: path_creation_for_background(
            character_number=x.character,
            background_type=x.background_type,
            background_name=x.background_name,
        ),
        axis=1,
    )

    ########################################           background end                #############################################################

    ########################################           key end                #############################################################

    data["key"] = data.apply(
        lambda x: key_generator(
            str(x.character),
            str(x.emotion),
            str(x.phonem),
            str(x.eye_path),
            str(x.intensity),
            str(x.eyes_position),
            str(x.head_direction),
            str(x.screen_mode),
            str(x.background_type),
            str(x.background_name),
            str(x.body_action),
            str(x.body_path),
            str(x.head_rotation),
            str(x.mouth_image_path),
            str(x.zoom),
        ),
        axis=1,
    )

    ########################################           key end                #############################################################

    data.to_csv("new_LMR.csv")
    print("save to csv")
    return data


if __name__ == "__main__":
    main()
