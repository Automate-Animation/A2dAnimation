# import pandas as pd
import argparse
from ast import arg
import json
from code.gentle_conversion.phonemes import add_phonemes, add_gentle_phonemes
from code.utils.updating_json_by_manual_csv import csv_to_aeaneas_json

args = argparse.Namespace

def parse_args():
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--input", help = "input jamal or kamal for images")
    parser.add_argument("-f", "--file", help = "csv file name")
    parser.add_argument("-t", "--type", help = "gentle or other")
    
    # Read arguments from command line
    return parser.parse_args()

def main():
    global args
    args = parse_args()
    if args.input and args.file and args.type:
        print("using images of : % s" % args.input)
        print("using csv file of : % s" % args.file)
        print("phonemes calculation : % s" % args.type)

        path_csv = f'./csv/{args.file}.csv'
        name = path_csv.split('/')[-1].split('.')[0]
        data = csv_to_aeaneas_json(path_csv,args.input)
        if  args.type == 'gentle':
            path = f"./gentle_json/{args.file}.json"
            f = open(path) 
            gentle_data = json.load(f)
            data = add_gentle_phonemes(data, gentle_data)
        else:
            data = add_phonemes(data)

        print("save json : ",name)
        with open(f'./json/json_data_for_frame/{name}.json', "w") as outfile:
            json.dump(data, outfile)
    else:
        print("Please input correct value for example using -i jamal and -f file_name and -t gentle or normal")
        
def aeaneas_json(input, csv, gentle_file, type='normal' ):
    print("csv_to_aneaneas_json")

    print("using images of : % s" % input)


    data = csv_to_aeaneas_json(csv,input)
    if type == 'gentle':
        path = f"./gentle_json/{gentle_file}.json"
        f = open(path) 
        gentle_data = json.load(f)
        data = add_gentle_phonemes(data, gentle_data)
    else:
        data = add_phonemes(data)

    return data
    
    
if __name__ == '__main__':
    main()