import json
import os

path = "./json/json_data_for_frame/kamal_phonemes.json"
type_value_dic = {
    "character": {"1": "1", "2": "2", "3": "3"},
    "emotion": {
        "1": "happy",
        "2": "sad",
        "3": "angry",
        "4": "bore",
        "5": "content",
        "6": "glare",
        "7": "sarcasm",
        "8": "worried",
    },
    "intensity": {"1": True, "2": False},
    "head_direction": {"1": "L", "2": "M", "3": "R"},
    "eyes_direction": {"1": "L", "2": "M", "3": "R"},
    "screen_mode": {"1": "office", "2": "explaination", "3": "white", "4": "plain"},
    "body_action": {
        "1": "achieve",
        "2": "answer",
        "3": "explain",
        "4": "me",
        "5": "not_me",
        "6": "question",
        "7": "technical",
        "8": "why",
        "9": "you",
    },
    "reaction": {
        "1": "happy",
        "2": "sad",
        "3": "angry",
        "4": "bore",
        "5": "content",
        "6": "glare",
        "7": "scard",
        "8": "worried",
    },
}

frame_data = open(path)

frames_json = json.load(frame_data)


def clean_creen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def addingValues(type_value):
    add_checker = input("what to add .. ? press 1 Otherwise press q :  ").strip()
    if add_checker == "1":

        for each_fagment in frames_json["fragments"]:
            if type_value in each_fagment:
                del each_fagment[type_value]

        text = ""

        for each_fragment in frames_json["fragments"]:
            if text == "":
                text = each_fragment["lines"][0]
            else:
                text = text + " " + each_fragment["lines"][0]
        length_of_text = len(frames_json["fragments"])

        counter = length_of_text

        while text != "":
            print(text)
            user_input = input("Enter the name of the file: ").strip()
            length = len(user_input)
            user_input_list = user_input.split(" ")
            print(f"type of {type_value}: ?")
            print("--" * 20)
            print(type_value_dic[type_value])
            value = input(f"Enter from above {type_value}: ")

            get_value = type_value_dic[type_value].get(value)
            if get_value == None:
                print("Invalid input :", value)
                print("added happy!!")
                get_value = type_value_dic[type_value]["1"]
                print(f"added {get_value}!!")

            for each_word in user_input_list:
                if (
                    frames_json["fragments"][length_of_text - counter]["lines"][0]
                    == each_word
                ):
                    if (
                        type_value
                        not in frames_json["fragments"][length_of_text - counter]
                    ):
                        frames_json["fragments"][length_of_text - counter][
                            type_value
                        ] = get_value
                        counter -= 1

            text = text[length:].strip()


def addingReaction(type_value):

    for each_fagment in frames_json["fragments"]:
        if "reaction_bool" in each_fagment:
            del each_fagment["reaction_bool"]

        if "reaction" in each_fagment:
            del each_fagment["reaction"]

    text = ""

    for each_fragment in frames_json["fragments"]:
        if text == "":
            text = each_fragment["lines"][0]
        else:
            text = text + " " + each_fragment["lines"][0]
    length_of_text = len(frames_json["fragments"])

    counter = length_of_text

    while text != "":
        print(text)
        user_input = input("Enter the name of the file: ").strip()
        length = len(user_input)
        user_input_list = user_input.split(" ")
        print(f"type of {type_value}: ?")
        print("--" * 20)
        # checker
        checker = input(f"Want to add reaction ? Press 1 otherwise press q :  ")
        if checker == "1":
            print(type_value_dic[type_value])
            value = input(f"Enter from above {type_value}: ")

            get_value = type_value_dic[type_value].get(value)
            if get_value == None:
                print("Invalid input :", value)
                get_value = type_value_dic[type_value]["1"]
                print(f"added {get_value}!!")

            print(type_value_dic["character"])
            value = input(f"Chooce your reaction character: ")

            character = type_value_dic["character"].get(value)
            if character == None:
                print("Invalid input :", character)
                character = type_value_dic[type_value]["1"]
                print(f"added {character}!!")
        else:
            get_value = ""

        for each_word in user_input_list:
            if (
                frames_json["fragments"][length_of_text - counter]["lines"][0]
                == each_word
            ):
                if checker == "1":
                    frames_json["fragments"][length_of_text - counter][
                        "reaction_bool"
                    ] = True
                    frames_json["fragments"][length_of_text - counter][
                        "character"
                    ] = character
                else:
                    frames_json["fragments"][length_of_text - counter][
                        "reaction_bool"
                    ] = False
                frames_json["fragments"][length_of_text - counter][
                    type_value
                ] = get_value

                counter -= 1

        text = text[length:].strip()


# this code just delete the key if exists

# for each_fagment in frames_json['fragments']:
#     if 'character' in each_fagment:
#         del each_fagment['character']

#     if 'emotion' in each_fagment:
#         del each_fagment['emotion']

#     if 'intensity' in each_fagment:
#         del each_fagment['intensity']

#     if 'head_direction' in each_fagment:
#         del each_fagment['head_direction']

#     if 'eyes_direction' in each_fagment:
#         del each_fagment['eyes_direction']

#     if 'screen_mode' in each_fagment:
#         del each_fagment['screen_mode']

#     if 'body_action' in each_fagment:
#         del each_fagment['body_action']

clean_creen()
print("------------------------------- character -------------------------------")
addingValues("character")

clean_creen()
print("------------------------------- emotion -------------------------------")
addingValues("emotion")

clean_creen()
print("------------------------------- intensity -------------------------------")
addingValues("intensity")

clean_creen()
print("------------------------------- head_direction -------------------------------")
addingValues("head_direction")

clean_creen()
print("------------------------------- eyes_direction -------------------------------")
addingValues("eyes_direction")

clean_creen()
print("------------------------------- screen_mode -------------------------------")
addingValues("screen_mode")

clean_creen()
print("------------------------------- body_action -------------------------------")
addingValues("body_action")

clean_creen()
print("------------------------------- reaction -------------------------------")
addingReaction("reaction")

with open(path, "w") as outfile:
    json.dump(frames_json, outfile)
