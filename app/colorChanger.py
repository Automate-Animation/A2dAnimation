import glob
from code.editImage.changingColor import changing_color_using_hsv

import cv2

# # search all files inside a specific folder
# # *.* means file name with any extension
dir_path = r"./images/body/character_9/**/*.*"
for file in glob.glob(dir_path, recursive=True):
    print(file.split("\\"))
    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    color = [244, 208, 63][::-1]
    color_change_image = changing_color_using_hsv(
        img, color=color, lower_hsv_value=[45, 118, 0], upper_hsv_value=[255, 255, 255]
    )
    cv2.imwrite(
        "./images/body/character_9/"
        + file.split("\\")[-2]
        + "/"
        + file.split("\\")[-1],
        color_change_image,
    )


# image_path = r'G:/Projects/speech aligner/kamal speech aliner/speach_aliner/app/images/body/character_6/you\body20.png'
# # image_path = r'G:/Projects/speech aligner/kamal speech aliner/speach_aliner/clean/practice_code/eyes.png'
# img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
# color_change_image=changing_color_using_hsv(img, color=[79, 168, 246],lower_hsv_value=[ 40,   0, 186], upper_hsv_value= [ 255, 255, 255])
# cv2.imwrite('change.png', color_change_image)

#  for character_1 shirt color
# l_b  [ 0 82 64]
# u_b  [ 36 147 255]

# light green
# l_b  [40,   0 ,186]
# u_b  [255 255 255]

# #dark green
# l_b  [ 45, 118 ,  0]
# u_b  [255 255 255]
