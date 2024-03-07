import statistics

import numpy as np
from PIL import Image, ImageOps


def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)

def adding_image(img_bg, img_fg, location, size = 30, rotation=0, mirror=False, size_cordinates=None):
    
    """ PIL import image required not openCV. this function is responsiable for adding image, size and rotating it """
    if size_cordinates is not None:
        dim = size_cordinates
    else:
        width, height = img_fg.size
        scale_percent = size # percent of original size
        width = int(width * scale_percent / 100)
        height = int(height * scale_percent / 100)
        dim = (width, height)

    if mirror:
        img_fg = ImageOps.mirror(img_fg)
    
    if rotation != 0:
        img_fg = img_fg.rotate(rotation)
        
    img_fg = img_fg.resize(dim)
    
    img_bg.paste(img_fg, location, mask = img_fg)
    
    return img_bg


def mirror_image(img):
    return ImageOps.mirror(img)
 # how to use this function:
# face = Image.open(r"new face1.png")

# eye = Image.open(r"sad.png")

# im  = np.array(face.convert('RGB'))

# # Define the blue colour we want to find - PIL uses RGB ordering
# blue = [253,250,230]

# # Get X and Y coordinates of all blue pixels
# Y, X = np.where(np.all(im==blue,axis=2))
# x, y=statistics.mean(X),statistics.mean(Y)

# new_image = adding_image(face, eye, location=(x,y), rotation=3)
# new_image.show()
# new_image.save('new_G.png')