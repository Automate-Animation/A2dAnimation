import argparse
import json
args = argparse.Namespace

from gentleToCsv import gentle_to_csv
from manual_update import aeaneas_json
from frame_generator_by_number import adding_frame_data
from main import imageGenerator

def main():
    global args
    args = parse_args()
    if args.file and args.type and args.input:
        print("using csv file of : % s" % args.file)
        csv = gentle_to_csv(args.file)
        json_data = aeaneas_json(input=args.input, csv=csv, gentle_file=args.file, type=args.input)
        # print(json_data)
        frames = adding_frame_data(json_data)
        
        video_info =  imageGenerator(frames)
        with open(f'./json/json_data_for_frame/test.json', "w") as outfile:
            json.dump(json_data, outfile)
    else:
        print("Please input correct value for example using -i kamal and -f file_name and -t gentle or normal")



def parse_args():
    
    parser = argparse.ArgumentParser(description="Script to parse")
    # Adding optional argument
    parser.add_argument("-f", "--file", help = "json file name")
    parser.add_argument("-i", "--input", help = "input jamal or kamal for images")
    parser.add_argument("-t", "--type", help = "gentle or other")
    # Read arguments from command line
    return parser.parse_args()


if __name__ == '__main__':
    
    main()