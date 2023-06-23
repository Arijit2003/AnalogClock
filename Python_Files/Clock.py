import cv2
import datetime
import math
import numpy as np
from constants import RADIUS
from constants import CENTER
from constants import COLORS
from constants import CANVAS_SIZE
from HelperFunctions import get_ticks, get_time

hours_init,hours_dest=get_ticks()
CANVAS=np.zeros(shape=(CANVAS_SIZE),dtype=np.uint8)
CANVAS[:]=[255,255,255]
for i in range(len(hours_init)):
    if i%5==0:
        cv2.line(CANVAS,hours_init[i],hours_dest[i],COLORS.get("black"),3)
    else:
        cv2.circle(CANVAS,hours_init[i],5,COLORS.get("gray"),-1)
cv2.circle(CANVAS,CENTER,RADIUS+10,COLORS.get("yellow"),2)
cv2.putText(CANVAS,"TITAN",(250,230),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,COLORS.get("dark_gray"),2)


while(True):
    image=CANVAS.copy()
    image=get_time(image)
    cv2.imshow("Analog CLock",image)
    if(cv2.waitKey(1)==27):
        break
    


