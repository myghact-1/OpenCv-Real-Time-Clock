### IMPORTING ALL REQUIRED LIBRARIES ###

import cv2
import numpy as np
import math
import time


## CREATE A CANVAS ##
blank = np.ones((512, 512, 3), np.uint8) * 100

def real_time_clock():
    blank_copy = blank.copy()  # COPIED BLANK IMAGE

    ## DRAW CLOCK ON BLANK IMAGE AND PUT TEXT ##
    cv2.circle(blank_copy, (256, 256), 250, (255, 255, 255), 2)
    cv2.rectangle(blank_copy, (150, 100), (370, 180), (255, 255, 255), -1)
    cv2.putText(blank_copy, "OpenCv Real", (155, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(blank_copy, "Time Clock", (160, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    line_pt1 = []
    line_pt2 = []
    Cx, Cy = 256, 256  # CENTER POINT OF CLOCK
    radius = 250

    for theta in range(0, 360, 30):
        x = int(Cx + radius * math.cos(theta * 3.14 / 180))
        y = int(Cy + radius * math.sin(theta * 3.14 / 180))
        line_pt1.append((x, y))

    for theta in range(0, 360, 30):
        x = int(Cx + (radius - 20) * math.cos(theta * 3.14 / 180))
        y = int(Cy + (radius - 20) * math.sin(theta * 3.14 / 180))
        line_pt2.append((x, y))

    ## DRAW HOURLY SMALL LINES
    for i in range(len(line_pt1)):
        cv2.line(blank_copy, line_pt1[i], line_pt2[i], (255, 255, 255), 2)

    ### GET CURRENT TIME ###
    now = time.ctime()
    time_list = now.split()  # day, month, date, time, year

    current_time = time_list[3]
    current_time_list = current_time.split(sep=':')  # hour, minute, second
    hour = int(current_time_list[0])
    minute = int(current_time_list[1])
    second = int(current_time_list[2])

    full_date = f"{time_list[0]}, {time_list[2]}/{time_list[1]}/{time_list[-1]}"

    ## SECOND RECTANGLE FOR REAL TIME ##
    cv2.rectangle(blank_copy, (140, 400), (370, 450), (255, 255, 255), -1)
    cv2.putText(blank_copy, f"{current_time}", (150, 440), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)

    # ANGLES OF SECOND, MINUTE, AND HOUR NEEDLE #
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour * 30) + (minute / 2) + 270, 360)

    # DRAW LINES FOR SECOND, MINUTE, AND HOUR:
    second_x = round(Cx + (radius - 15) * math.cos(second_angle * 3.14 / 180))
    second_y = round(Cy + (radius - 15) * math.sin(second_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (second_x, second_y), (255, 0, 0), 2)

    minute_x = round(Cx + (radius - 30) * math.cos(minute_angle * 3.14 / 180))
    minute_y = round(Cy + (radius - 30) * math.sin(minute_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (minute_x, minute_y), (255, 0, 0), 8)

    hour_x = round(Cx + (radius - 50) * math.cos(hour_angle * 3.14 / 180))
    hour_y = round(Cy + (radius - 50) * math.sin(hour_angle * 3.14 / 180))
    cv2.line(blank_copy, (Cx, Cy), (hour_x, hour_y), (255, 0, 0), 10)

    #### DRAW CURRENT DATE AND DAY ####
    cv2.putText(blank, full_date, (155, 390), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 255), 2)

    ## CENTER POINT OF ALL NEEDLES ##
    cv2.circle(blank_copy, (Cx, Cy), 10, (0, 0, 255), -1)

    return blank_copy


while True:

    ## SHOW CLOCK ##
    cv2.imshow("Clock, PRESS 'q' TO CLOSE WINDOW", real_time_clock())
    
    ## PRESS 'q' TO CLOSE WINDOW
    if cv2.waitKey(1)==ord('q'):
        break

## DESTROY ALL WINDOWS    
cv2.destroyAllWindows()