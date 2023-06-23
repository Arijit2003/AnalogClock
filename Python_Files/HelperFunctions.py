import cv2
import datetime
import math
from constants import RADIUS
from constants import CENTER
from constants import COLORS

def get_ticks():
    hours_init=[]
    hours_dest=[]
    for i in range(0,360,6):
        x_coordinate=CENTER[0]+(RADIUS*math.cos(i*math.pi/180))
        y_coordinate=CENTER[1]+(RADIUS*math.sin(i*math.pi/180))
        hours_init.append((int(x_coordinate),int(y_coordinate)))

    for i in range(0,360,6):
        x_coordinate=CENTER[0]+((RADIUS-20)*math.cos(i*math.pi/180))
        y_coordinate=CENTER[1]+((RADIUS-20)*math.sin(i*math.pi/180))
        hours_dest.append((int(x_coordinate),int(y_coordinate)))
    
    return hours_init,hours_dest

def get_time(Canvas):
    time_now=datetime.datetime.now().time()
    hour=math.fmod(time_now.hour,12)
    minute=time_now.minute
    second=time_now.second
    #angle
    second_angle=math.fmod(6*second+270,360)
    minute_angle=math.fmod(6*minute+270,360)
    hour_angle=math.fmod((30*hour)+(minute/2)+270,360)
    # draw line
    second_x=int(CENTER[0]+(RADIUS-25)*math.cos(second_angle*math.pi/180))
    second_y=int(CENTER[1]+(RADIUS-25)*math.sin(second_angle*math.pi/180))
    cv2.line(Canvas,CENTER,(second_x,second_y),COLORS.get("black"),2)

    minute_x=int(CENTER[0]+(RADIUS-60)*math.cos(minute_angle*math.pi/180))
    minute_y=int(CENTER[1]+(RADIUS-60)*math.sin(minute_angle*math.pi/180))
    cv2.line(Canvas,CENTER,(minute_x,minute_y),COLORS.get("amber"),3)


    hour_x=int(CENTER[0]+(RADIUS-100)*math.cos(hour_angle*math.pi/180))
    hour_y=int(CENTER[1]+(RADIUS-100)*math.sin(hour_angle*math.pi/180))
    cv2.line(Canvas,CENTER,(hour_x,hour_y),COLORS.get("amber"),7)

    cv2.circle(Canvas,CENTER,5,COLORS.get("black"),-2)

    return Canvas
