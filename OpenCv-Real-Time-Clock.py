### IMPORTING ALL REQUIRED LIBRARIES ###

import warnings
warnings.filterwarnings('ignore')

import cv2
import numpy as np
import math
import calendar
import datetime


## CREATE A BLANK IMAGE ##
blank = np.zeros((512,512,3),np.uint8)

while True:
    
    blank_copy = blank.copy() # COPIED BLANK IMAGE
    
    ## DRAW CLOCK ON BLANK IMAGE AND PUT TEXT ##
    cv2.circle(blank_copy,(256,256),250,(255,255,255),2)
    cv2.rectangle(blank_copy,(150,100),(370,180),(255,255,255),-1)
    cv2.putText(blank_copy,"OpenCv Real",(155,130),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    cv2.putText(blank_copy,"Time Clock",(160,170),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

    line_pt1 = []
    line_pt2 = []
    Cx, Cy = 256, 256 # CENTER POINT OF CLOCK
    radius = 250

    for theta in range(0,360,30):
        x = int(Cx + radius*math.cos(theta*3.14/180))
        y = int(Cy + radius*math.sin(theta*3.14/180))
        line_pt1.append((x,y))

    for theta in range(0,360,30):
        x = int(Cx + (radius-20)*math.cos(theta*3.14/180))
        y = int(Cy + (radius-20)*math.sin(theta*3.14/180))
        line_pt2.append((x,y))
        
    ## DRAW HOURLY SMALL LINES
    for i in range(len(line_pt1)):
        cv2.line(blank_copy,line_pt1[i],line_pt2[i],(255,255,255),2)

    
    ### GET CURRENT TIME ###
    date_time_now = datetime.datetime.now()
    time_now = date_time_now.time()
    
    hour = int(math.fmod(time_now.hour, 12)) # HOUR 12 NOT 24 #
    minute = time_now.minute
    second = time_now.second
    
    ## SECOND RECTANGLE FOR REAL TIME ##
    cv2.rectangle(blank_copy,(150,400),(360,450),(255,255,255),-1)
    cv2.putText(blank_copy,f"{hour}:{minute}:{second:.2g}",(170,440),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
    
    # ANGLES OF SECOND, MINUTE, AND HOUR NEEDLE #
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour*30) + (minute/2) + 270, 360)
    
    # DRAW LINES FOR SECOND, MINUTE, AND HOUR:
    second_x = round(Cx + (radius-15) * math.cos(second_angle * 3.14 / 180))
    second_y = round(Cy + (radius-15) * math.sin(second_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (second_x, second_y), (255,0,0), 2)

    minute_x = round(Cx + (radius-30) * math.cos(minute_angle * 3.14 / 180))
    minute_y = round(Cy + (radius-30) * math.sin(minute_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (minute_x, minute_y), (255,0,0), 8)

    hour_x = round(Cx + (radius-50) * math.cos(hour_angle * 3.14 / 180))
    hour_y = round(Cy + (radius-50) * math.sin(hour_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (hour_x, hour_y), (255,0,0), 10)
    
    #### DRAW CURRENT DATE AND DAY ####
    dt = datetime.datetime.now()
    year, month, day = dt.year, dt.month, dt.day
    weekday_number = calendar.weekday(year,month,day)
    weekday_name = calendar.day_abbr[weekday_number]
    month_name = calendar.month_abbr[month]
    
    cv2.putText(blank,f"{weekday_name}, {day} {month_name} {year}",(155,390),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),2)
    
    ## CENTER POINT OF ALL NEEDLES ##
    cv2.circle(blank_copy,(Cx,Cy),10,(0,0,255),-1)

    ## SHOW CLOCK ##
    cv2.imshow("Clock, PRESS 'q' TO CLOSE WINDOW",blank_copy)
    
    ## PRESS 'q' TO CLOSE WINDOW
    if cv2.waitKey(1)==ord('q'):
        break

## DESTROY ALL WINDOWS    
cv2.destroyAllWindows()
