import json

import pandas as pd

from .constants import actions

# path_csv = 'G:/Projects/speech aligner/kamal speech aliner/speach_aliner/app/kamal_action.csv'

data_json = {"fragments":[]}

type_value_dic = actions['jamal']


def csv_to_aeaneas_json(path, name):
    type_value_dic = actions[name]
    if isinstance(path, str):
        df = pd.read_csv(path)
    else:
        df = path

    for line in df.itertuples():
        data = {}
        # print(line[7])
        data['character'] = type_value_dic['character'].get(str(line[1]))
        data['emotion'] = type_value_dic['emotion'].get(str(line[2]))
        data['intensity'] = type_value_dic['intensity'].get(str(line[3]))
        
        data['head_direction'] = type_value_dic['head_direction'].get(str(line[4]))
        data['eyes_direction'] = type_value_dic['eyes_direction'].get(str(line[5]))
        data['screen_mode'] = type_value_dic['screen_mode'].get(str(line[6]))
        data['body_action'] = type_value_dic['body_action'].get(str(line[7]))
        data['reaction_bool'] = line[8]
        data['lines'] = [line[9].strip()]
        data['begin'] = line[10]
        data['end'] = line[11]
        data['zoom'] = line[12]
        
        
        data_json['fragments'].append(data)
        
    return data_json


# with open('G:/Projects/speech aligner/kamal speech aliner/speach_aliner/app/json/json_data_for_frame/kamal.json', 'w') as f:
#     json.dump(data_json, f)
#     f.close()