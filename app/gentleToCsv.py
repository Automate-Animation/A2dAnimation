import json
import queue

import pandas as pd

q = queue.Queue()


from code.utils.valueCreator import (random_value_genrator,
                                     random_value_genrator_for_body)
import argparse
args = argparse.Namespace


def main():
    print("main")
    global args
    args = parse_args()
    final_file= pd.DataFrame(columns= [
    'character','emotion','intensity','head_direction','eyes_direction',
    'screen_mode','body_action','reaction_bool','word','init','final','room'
    ])
    
    
    if args.file:
        print("using csv file of : % s" % args.file)

    path = f"./gentle_json/{args.file}.json"

    f = open(path) 
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    list_of_data = []
    temp = None
    for i in range(len(data['words'])):
        try:
            dic_new = {}
        #     print(data['words'][i]['word'])
            dic_new['word'] = data['words'][i]['word']
            if data['words'][i]['case'] == "success":
                dic_new['word'] = data['words'][i]['word']
                dic_new['init'] = data['words'][i]['start']
                dic_new['final'] = data['words'][i]['end']
                # if round(data['words'][i]['start'],3) == temp:
                #     dic_new['init'] = round(data['words'][i]['start'],3) + 0.01
                    
                # else:
                #     dic_new['init'] = round(data['words'][i]['start'],3)
                    
                    
                # dic_new['final'] = round(data['words'][i]['end'],3)
                # temp = round(data['words'][i]['end'],3)
                # q.put(dic_new)
                
            else:
                print(data['words'][i]['case'])
                dic_new['init'] = ''
                dic_new['final'] = ''
            list_of_data.append(dic_new)
        except Exception as e:
            print(e)
            
    # while(not(q.empty())):
    #     result = q.get()
    #     final_file = final_file.append(result, ignore_index=True)
    for element in list_of_data:
        final_file = final_file.append(element, ignore_index=True)
    name = path.split('/')[-1].split('.')[0]

    print(final_file)
    print(name)
    final_file.to_csv(f'./csv/{name}.csv', index=False)
    f.close()

def character_random_values(total_frams,difference,list_of_values, option, list_of_data):
    
    option_data = random_value_genrator(total_frams,difference=difference,list_of_values=list_of_values)
    for i in range(total_frams):
        list_of_data[i][option] = option_data[i]
    return list_of_data
    

def gentle_to_csv(gentle_json):
    print("gentle_to_csv_function")
    final_file= pd.DataFrame(columns= [
    'character','emotion','intensity','head_direction','eyes_direction',
    'screen_mode','body_action','reaction_bool','word','init','final','room'
    ])
    

    path = f"./gentle_json/{gentle_json}.json"

    f = open(path) 

    data = json.load(f)
    list_of_data = []
    for i in range(len(data['words'])):
        try:
            dic_new = {}
        #     print(data['words'][i]['word'])
            dic_new['word'] = data['words'][i]['word']
            if data['words'][i]['case'] == "success":
                dic_new['word'] = data['words'][i]['word']
                dic_new['init'] = data['words'][i]['start']
                dic_new['final'] = data['words'][i]['end']

                
            else:
                print(data['words'][i]['case'])
                dic_new['init'] = 0
                dic_new['final'] = 0
            list_of_data.append(dic_new)
        except Exception as e:
            print(e)
    total_frams = len(data['words'])
    
    list_of_data = character_random_values(total_frams, 7, [1,2] , 'intensity',  list_of_data)
    list_of_data = character_random_values(total_frams, 10, [1,2,3] , 'head_direction',  list_of_data)
    list_of_data = character_random_values(total_frams, 5, [1,2,3] , 'eyes_direction',  list_of_data)
    list_of_data = character_random_values(total_frams, 5, [False] , 'reaction_bool',  list_of_data)
    list_of_data = character_random_values(total_frams, 5, [4] , 'screen_mode',  list_of_data)
    list_of_data = character_random_values(total_frams, 7, [1,2,3,4,5,6,7,8] , 'body_action',  list_of_data)
    list_of_data = character_random_values(total_frams, 10, [1,5,6,14] , 'emotion',  list_of_data)
    list_of_data = character_random_values(total_frams, 40, [1.5,0] , 'room',  list_of_data)
    list_of_data = character_random_values(total_frams, 40, [9] , 'character',  list_of_data)
    
    for element in list_of_data:
        final_file = final_file.append(element, ignore_index=True)
    name = path.split('/')[-1].split('.')[0]

    print(final_file)
    print(name)
    final_file.to_csv(f'./csv/{name}.csv', index=False)
    f.close()
    return final_file

def parse_args():
    
    parser = argparse.ArgumentParser(description="Script to parse")
    # Adding optional argument
    parser.add_argument("-f", "--file", help = "json file name")
    
    # Read arguments from command line
    return parser.parse_args()


if __name__ == '__main__':
    
    main()