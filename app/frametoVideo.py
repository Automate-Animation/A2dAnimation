
import argparse
import json
import os
from datetime import datetime
from os.path import isfile, join

import cv2
import numpy as np

# Initialize parser 
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-n", "--name", help = "name of video")

# mypath = './frames/headFrames/'

frame_data = open('./json/frameCreationInfo/frameCreationInfo.json')

frame_data = json.load(frame_data)


def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))
    filename=pathIn + frame_data['frame_key']['0'] + '.png'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for counter in range(len(frame_data['frame_key'])):

                # print(number)
            # counter +=1
            # files = str(counter) + '.png'
            # print(files)

            filename=pathIn + frame_data['frame_key'][str(counter)] + '.png'
            img = cv2.imread(filename)
            # height, width, layers = img.shape
            # # dim = (653, 1158)
            # # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            # # size = dim
            # size = (width, height)
            print(counter, " : ", filename)
            # print(size)
            #inserting the frames into an image array
            # frame_array.append(img)
            out.write(img)

    

    # for i in range(len(frame_array)):
    #     # writing to a image array
    #     out.write(frame_array[i])
    out.release()

def main():
    # pathIn= './frames/headFrames/'
    # pathIn= './frames/bodyFrames/'
    pathIn= './frames/backgroundFrames/'
   
    
    # Read arguments from command line
    args = parser.parse_args()
    if args.name:
        pathOut = f'./video/{args.name}.avi'
        name = args.name
    else:
        today = datetime.now()
        pathOut = f'./video/{str(today)}.avi'
        name = today
    print(f"file name is {name}")
    fps = 24.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()