
print("Main....!")


# from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import json
import multiprocessing
import os
import time
from itertools import product
from multiprocessing import Pool, freeze_support

import pandas as pd

from backgroundCreatingFrame import adding_background
from bodyCreatingFrame import adding_head_and_body
from headCreatingFrame import adding_eyes_and_mouth

data_dict = {"face":[], "eye":[], "mouth":[],  "body":[], "frame_name":[],"background":[], "key":[], "rotation":[], "zoom":[]}
frame_data = {"key_counter":{}, "frame_key":{}}
mypath= './frames/backgroundFrames'
files = [f for f in os.listdir(mypath)]
for each_file in files:
    key_name =each_file.split('.')[0]
    if key_name:
        frame_data['key_counter'][each_file.split('.')[0]] = 1


def imageCreater(face_path, eye_path, mouth_path,body_path, background_path ,frame_name, key, rotation, zoom):

    if key not in frame_data['key_counter']:
        frame_data['key_counter'][key] = 1
        head = adding_eyes_and_mouth(face_path=face_path, eye_path=eye_path, mouth_path=mouth_path, frame_name=frame_name)
        body = adding_head_and_body(head,body_path,  frame_name=frame_name,rotation= rotation)
        background = background_path
        adding_background(body_path=body, background_path=background,  frame_name=key, zoom=zoom)
    else:
        frame_data['key_counter'][key] = frame_data['key_counter'][key] + 1
    frame_data['frame_key'][frame_name] = key
    print(frame_name ,  " -- ", key)
    
def main():
    data = pd.read_csv('new_LMR.csv')
    
    counter = 0 
    for face, eye, mouth,  body, background, key, rotation, zoom in zip(data.head_path, data.eye_path, data.mouth_image_path,  data.body_path, data.background_path, data.key, data.head_rotation,data.zoom):
        data_dict["face"].append(face)
        data_dict["eye"].append(eye)
        data_dict["mouth"].append(mouth)
        data_dict["body"].append(body)
        data_dict["frame_name"].append(counter)
        data_dict["background"].append(background)
        data_dict["key"].append(key)
        data_dict["rotation"].append(rotation)
        data_dict["zoom"].append(zoom)
        counter += 1
    
    with concurrent.futures.ThreadPoolExecutor(max_workers= 5) as executor:
        # executor.submit(imageCreater, data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"], data_dict["background"] ,data_dict["frame_name"],data_dict["key"])

        executor.map(imageCreater, data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"], data_dict["background"] ,data_dict["frame_name"],data_dict["key"],data_dict["rotation"],data_dict["zoom"])
    # print(frame_data)
    with open('./json/frameCreationInfo/frameCreationInfo.json', "w") as outfile:
        json.dump(frame_data, outfile)
        
def imageGenerator(data):
    print("imageGenerator called......")
    # data = pd.read_csv('new_LMR.csv')
    
    counter = 0 
    for face, eye, mouth,  body, background, key, rotation, zoom in zip(data.head_path, data.eye_path, data.mouth_image_path,  data.body_path, data.background_path, data.key, data.head_rotation,data.zoom):
        data_dict["face"].append(face)
        data_dict["eye"].append(eye)
        data_dict["mouth"].append(mouth)
        data_dict["body"].append(body)
        data_dict["frame_name"].append(counter)
        data_dict["background"].append(background)
        data_dict["key"].append(key)
        data_dict["rotation"].append(rotation)
        data_dict["zoom"].append(zoom)
        counter += 1
    
    with concurrent.futures.ThreadPoolExecutor(max_workers= 5) as executor:
        # executor.submit(imageCreater, data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"], data_dict["background"] ,data_dict["frame_name"],data_dict["key"])

        executor.map(imageCreater, data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"], data_dict["background"] ,data_dict["frame_name"],data_dict["key"],data_dict["rotation"],data_dict["zoom"])
    # print(frame_data)
    with open('./json/frameCreationInfo/frameCreationInfo.json', "w") as outfile:
        json.dump(frame_data, outfile)
    return frame_data
    

def multi_run_wrapper(*args):
    time.sleep(1)
    print(*args)

if __name__ == "__main__":
    main()
    # pool = multiprocessing.Pool(1) 

    # M = pool.starmap(imageCreater, zip(data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"], data_dict["background"] ,data_dict["frame_name"],data_dict["key"])) # this is the way to use multiprocessing
    
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #     executor.map(imageCreater, zip(data_dict["face"], data_dict["eye"], data_dict["mouth"],data_dict["body"],data_dict["frame_name"]))