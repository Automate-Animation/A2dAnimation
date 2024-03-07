import os
from code.utils.utils import (path_creation_for_background,
                              path_creation_for_body, path_creation_for_eyes,
                              path_creation_for_head, path_creation_for_mouth)

# mypath= './frames/backgroundFrames'
# files = [f for f in os.listdir(mypath)]
# print(files)



path = path_creation_for_body('3', "not_me")
print(path)