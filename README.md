# A2dAnimation
Automate-2d-Animation



## Description

A2dAnimation project aims to create 2d videos Animation using Gentle by utilizing a set of Python scripts. It involves steps to generate videos based on predefined character actions, emotions, and reactions.

## Installation
### Prerequisites

    Python 3.x installed on your system
    virtualenv module installed (optional but recommended)

### Setup

Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/project-name.git
```
Navigate to the project directory.

```bash
cd project-name
```
(Optional) Create a virtual environment.

```bash
virtualenv venv
```

Activate the virtual environment.

On Windows:

```bash
venv\Scripts\activate
```
On macOS and Linux:

```bash
source venv/bin/activate
```
Install the required Python packages.

bash

    pip install -r requirements.txt

Usage

   
 ```python
 python gentleToCsv.py -f fiverr
 ```

Generates a CSV file in the csv folder based on predefined JSON values. Images associated with these values can be found in the images folder.


    kamal = {
        "character":{"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10",},

        "emotion":{"1":"happy", "2":"sad", "3":"angry", "4":"bore", "5":"content",
                "6":"glare", "7":'sarcasm', "8":"worried","9":"crazy","10":"evil_laugh","11":"lust",
                "12":"shock", "13":'silly', "14":"spoked"},


        "intensity":{"1":True, '2':False},
        "head_direction":{"1":"L", "2":"M","3":"R"},
        "eyes_direction":{"1":"L", "2":"M","3":"R"},
        
        "screen_mode":{"1":"office","2":"explaination","3":"white", "4":"plain","5":"green",},

        "body_action":{"1":"achieve", "2":"answer", "3":"explain", "4":"me", 
                    "5":"not_me", "6":"question", "7":'technical', "8":"why","9":"achieve","10":"answer",
                    "11":"chilling", "12":"come", "13":'confuse', "14":"crazy","15":"dancing","16":"explain",
                    "17":"feeling_down", "18":"hi", "19":'i', "20":"idea","21":"idk","22":"joy",
                    "23":"jumping", "24":"kung_fu", "25":'love',"27":"meditation","28":"model",
                    "30":"paper", "31":'praying', "32":"question","33":"running","34":"search",
                    "35":"shy", "36":"singing", "37":'sneaky', "38":"standing","39":"technical","40":"that",
                    "41":"thinking", "42":"this", "43":'what', "44":"why","45":"winner","46":"yeah", "47":"you",},

        "reaction":{"1":"happy", "2":"sad", "3":"angry", "4":"bore",
                    "5":"content", "6":"glare", "7":'scard', "8":"worried"},
        }

```python
python manual_update.py -i kamal -f fiverr -t normal
```
Manually updates based on specified parameters.
```python
python frame_generator_by_number.py -f fiverr
```
Generates frames for the video.
```python
python main.py
```
Converts frames to a video.
```python
python frametoVideo.py -n fiverr
```

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.