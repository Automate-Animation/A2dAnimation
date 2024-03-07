import json

file_name = 'align.json' 
with open(file_name, 'r') as f:
  data = json.load(f)

aeanes_json = {"fragments": []}


for each_word in data['words']:
    print(each_word)
    if each_word['case']== 'success':
        fragment = {}
        fragment['begin'] = each_word["start"]
        fragment['end'] = each_word["end"]
        fragment['lines'] = [each_word["word"]]
        aeanes_json['fragments'].append(fragment)
        
    

with open(file_name.split('.')[0]+"_aeanes.json", "w") as outfile:
    json.dump(aeanes_json, outfile)