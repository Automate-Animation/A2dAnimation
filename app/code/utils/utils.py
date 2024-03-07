import os
import random

# blinker_data = {
#     '2':0,'3':0,'4':0, 'counter':0, "blank_counter" : 0
# }
# number = 4
# blank_counter = 7

def path_creation_for_mouth(character_number=1, mouth_type="happy"):
    path = f"./images/mouth/character_{character_number}/{mouth_type}/"
    return path
    
def path_creation_for_mouth_reaction(character_number=1, mouth_type="happy",intensity=False):
    if intensity:
        path = f"./images/mouth/mouth_expression/{mouth_type}_2.png"
    else:    
        path = f"./images/mouth/mouth_expression/{mouth_type}.png"
    return path

def path_creation_for_eyes(character_number=1, eyes_type="", eyes_emotion="happy",intensity=False, eyes_position="L"):
    """1.  character_number: which character to use (1-6)
    2.  eyes_type: which eyes to use (blinking or not) 
    3.  eyes_emotion: which emotion to use (happy, angry, sad, surprised, confused, sleepy) 
    4.  intensity: if True, use intensity images, if False, use normal images
    5.  eyes_position: which eyes to use (L or R or M) """

    path = f"./images/eyes/character_{character_number}/side_eyes"

    if eyes_type == "blinking":
        eyes_type = f"_{eyes_type}"
        path += eyes_type+"/"
    else:
        path += "/"
    path += f"{eyes_emotion}"

    if intensity:
        path += "_2/"
        #image name
        path += f"{eyes_emotion}_2_{eyes_position}.png"
    else:
        path += "/"
        path += f"{eyes_emotion}_{eyes_position}.png"


    return path

def path_creation_for_head(character_number=1, direction="L"):
    path = f"./images/head/character_{character_number}/{direction}.png"
    return path


def path_creation_for_body(character_number=1, body_action="achieve"):
    path = f"./images/body/character_{character_number}/{body_action}"

    # # mypath= './frames/backgroundFrames'
    # files = [f for f in os.listdir(path)]
    # image_name = random.choice(files)
    # path = path + "/" + image_name
    # print(image_name)
    # print(files)
    return path

def path_creation_for_background(character_number=1,background_type="office",background_name="wall"):
    path = f"./images/background/{background_type}/character_{character_number}/{background_name}.png"
    return path

def key_generator(character, emotion,phonem, eye_path, intensity, eyes_position, head_direction, screen_mode, background_type, background_name,
                    body_action, body_path, head_rotation,mouth_image_path, zoom):

    if screen_mode == "white":
        return "white"
    key = character + emotion + phonem + eye_path.split('/')[-1].split('.')[0] + intensity + eyes_position + head_direction + screen_mode + background_type + background_name + body_action + body_path.split('/')[-1].split('.')[0] + head_rotation + mouth_image_path.split('/')[-1].split('.')[0] + zoom
    return key 
# def random_generator(checker, emotion):
#     data = ['first','2','3','4','last']
#     data_iter = iter(data)
#     val = next(data_iter)
#     if val=='first' :
#         return emotion, checker
#     elif val=='last' :
#         data_iter = iter(data)
#         checker = False
#         return emotion, checker
#     else :
#         return val, checker
        

# def blinder_Generator(emotion="happy"):
#     yield emotion , True
#     yield 2 , True
#     yield 3, True
#     yield 4, True
#     yield emotion , False
# x is a generator object
# i=0
# checker =False
# while i<14:
#     i+=1
#     if i%2==0:
#         if checker == False:
#             print("checker")
#             x = Blinder_Generator()
#         val , checker = next(x)
#         print(val)
#     else:
#         print('--')




# def random_generator(emotion=None, blinking=None, intensity=None, eyes_position=None):
#         print("intensity  ",blinking)
#         if blinking == None:

#             blinking = random.choice([ "blinking"])
#         else:
#             blinking = blinking

#         if emotion == None:
#             emotion = 'happy'
        
#         if intensity == None:
#             intensity = random.choice([True, False,False,False,False])
        
#         if eyes_position == None:
#             eyes_position = random.choice(["L", "R","M","M","M","M","M","M"])
#         print(blinking, emotion, intensity, eyes_position)
#         return  blinking, emotion, intensity, eyes_position

# def blinker(emotion=None, blinking=None, intensity=None, eyes_position=None, start=False):
#     return_num = 0
#     if blinker_data['blank_counter'] <= 144 and blinker_data['counter']>=3:
#         blinker_data['blank_counter'] += 1
#         return *random_generator(blinking="noblinking", emotion=emotion, intensity=intensity, eyes_position=eyes_position), None
#     else:
#         blinker_data['blank_counter'] = 0
#     if start:
#         if blinker_data['counter']>=3:
#             for key, value in blinker_data.items():
#                 blinker_data[key]= 0
#         data = list(blinker_data.keys())[blinker_data['counter']]
#         if blinker_data[data] < number:
#             blinker_data[data] += 1 

#             return  *random_generator(blinking=blinking, emotion=emotion, intensity=intensity, eyes_position=eyes_position),  data
#         else:
#             blinker_data['counter'] +=1
#             return *random_generator(blinking=blinking, emotion=emotion, intensity=intensity, eyes_position=eyes_position), data
#             print("counter  ",blinker_data['counter'])
#     else:
#         return *random_generator(blinking=blinking, emotion=emotion, intensity=intensity, eyes_position=eyes_position), None