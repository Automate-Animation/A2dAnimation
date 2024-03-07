import json

import pandas as pd

df = pd.read_csv('phonemes2.csv').to_dict()
new_clean_phenome = {}

for each_entry in df['phonemes']:
    print(each_entry)
    new_clean_phenome[df['phonemes'][each_entry].strip()] = {'happy': df['happy'][each_entry], 'sad': df['sad'][each_entry]}

print(new_clean_phenome) 


 
# Data to be written

with open("phonemes_gentle_json.json", "w") as outfile:
    json.dump(new_clean_phenome, outfile)