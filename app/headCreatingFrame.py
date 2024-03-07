import json
import os
from code.editImage.addingImages import adding_image, mirror_image
from os.path import isfile, join

import numpy as np
from PIL import Image

mypath = './json/character_cordinates/'
files = [f for f in os.listdir(mypath)]
character_cordination_data = {}
for each_file in files:
    face_number = each_file.split('_')[1]
    mouth_or_eyes = each_file.split('_')[2]
    if face_number not in character_cordination_data:
        character_cordination_data[face_number] = {}
        character_cordination_data[face_number][mouth_or_eyes] = json.load(open(mypath + each_file))
    else:
        character_cordination_data[face_number][mouth_or_eyes] = json.load(open(mypath + each_file))
    
    
# print(character_cordination_data)
# eyes_cordinations = open('./json/character_cordinates/character_2_eyes_cordinations.json')
# mouth_cordinations = open('./json/character_cordinates/character_2_mouth_cordinations.json')

# eyes_cordinations = json.load(eyes_cordinations)
# mouth_cordinations = json.load(mouth_cordinations)


def adding_eyes_and_mouth(face_path, eye_path, mouth_path, frame_name):
    character_number = face_path.split('/')[3].split('_')[-1]
    face = Image.open(face_path)
    print("character_number ;",character_number)
    eye = Image.open(eye_path)

    mouth = Image.open(mouth_path)

    eye_phenome = eye_path.split('/')[-2]

    print(eye_phenome)

    mouth_phenome = mouth_path.split('/')[-1].split('.')[0]

    print(character_cordination_data[character_number]['eyes'][eye_phenome]['eye_location'])
    new_image = adding_image(face, eye, 
                            location=character_cordination_data[character_number]['eyes'][eye_phenome]['eye_location'], 
                            rotation=0, 
                            mirror=False, 
                            size_cordinates=character_cordination_data[character_number]['eyes'][eye_phenome]['eye_size'])


    new_image = adding_image(new_image, mouth, 
                            location=character_cordination_data[character_number]['mouth'][mouth_phenome]['mouth_location'], 
                            mirror=True,
                            size_cordinates=character_cordination_data[character_number]['mouth'][mouth_phenome]['mouth_size'])
    if face_path[-5]=='R':
        new_image = mirror_image(new_image)
    # new_image.show()
    # new_image.save(f'./frames/headFrames/{frame_name}.png')
    return new_image



if __name__ == "__main__":
    character = 10
    #  #how to use this function:
    face = f"./images/head/character_{character}/R.png"

    eye = f"./images/eyes/character_{character}/side_eyes/content_2/content_2_M.png"

    mouth = f"./images/mouth/character_{character}/happy/l_h.png"

    new = adding_eyes_and_mouth(face, eye, mouth,"test")