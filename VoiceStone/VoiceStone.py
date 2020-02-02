import numpy as np
from PIL import ImageGrab
import cv2

while(True):
    printScreen_PIL = ImageGrab.grab(bbox = (0, 40, 800, 640))
    printScreen_Numpy = np.array(printScreen_PIL.getdata(), dtype = 'uint8')\
                          .reshape((printScreen_PIL.size[1], printScreen_PIL.size[0], 3))

    cv2.imshow('window', printScreen_Numpy)

    if(cv2.waitKey(25) & 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break