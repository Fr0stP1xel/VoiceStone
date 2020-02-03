import numpy as np
from PIL import ImageGrab
import cv2
import time

def processImage(originalImage):
    #highThresh, thresh_im = cv2.threshold(originalImage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #lowThresh = 0.5*highThresh
    processedImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    processedImage = cv2.Canny(processedImage, threshold1 = 125, threshold2 = 175)
    return processedImage

lastTime = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox = (0, 40, 800, 640)))
    newScreen = processImage(screen)

    print('Loop took {} seconds'.format(time.time() - lastTime))
    lastTime = time.time()

    cv2.imshow('window', newScreen)
    #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if(cv2.waitKey(25) & 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break