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
git clone https://github.com/Automate-Animation/A2dAnimation.git
```
Navigate to the project directory.

```bash
cd A2dAnimation
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

### Usage

first we are going to use the json which was created by Gentle. i alrady placed it in folder gentle_json. 
 ```python
 python gentleToCsv.py -f software_intro
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


Right now you dont need to fill out the csv based on above json.  i already fill the CSV file software_intro2 in csv folder.
```python
python manual_update.py -i kamal -f software_intro2 -t normal
```
Manually updates based on specified parameters.
```python
python frame_generator_by_number.py -f software_intro2
```
Generates frames for the video. this may take time based on how long is the video.
```python
python main.py
```
Converts frames to a video. this may take time based on how long is the video. 
```python
python frametoVideo.py -n intro-video
```
After completion you will find the video in video folder. the video is without the audio you can attach the audio with your animation on any of your video editor. 

## Demo Video

Watch our demo video to see how A2dAnimation create video when attach it to audio. :

[Automate Animation Demo](http://www.youtube.com/watch?v=cxLqrV8j5zQ "Automate Animation Demo")


# Create Gentle Json

## Prerequisites

    Install Docker and docker-compose

## Running Gentle Docker

Go to ```Docker``` folder

```bash
sudo docker-compose up --build
``` 
After running the Docker command open the Browse open the link 
[127.0.0.1:49153](http://127.0.0.1:49153)

if you dont have Audio and text script use the assessd script in folder 
```example``` and upload it to [127.0.0.1:49153](http://127.0.0.1:49153)

After downloading the ```zip file``` open it and copy the ```align.json``` to ```gentle_json``` folder also rename it. rest of the flow is the same as above documentation. 

### Author

A2dAnimation is developed and maintained by [Oyekamal](https://github.com/oyekamal), a passionate creator dedicated to pushing the boundaries of animation technology.


### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.