import numpy as np
import cv2
import string
from math import fabs
import math

font = cv2.FONT_HERSHEY_SIMPLEX

window_height = 500
window_width = 600

img = np.zeros((window_height, window_width, 3), dtype = "uint8")

k = 0
step = 5

ulx = 300
drx = 300
height = 280
ground_height = 280

red = 0
green = 255
blue = 100

gradiant = 5
green_changing_for_next_state = green
direction = 0

rdlx = 0
rdly = 0
rulx = 0
ruly = 0
rurx = 0
rury = 0
rdrx = 0
rdry = 0

tulx = 0
tdrx = 0
theight = 0

check = 0

def square(thickness):
    down_side_y = int(height+fabs(ulx - drx)) if int(height+fabs(ulx - drx)) <= ground_height else ground_height

    cv2.line(img, (ulx, down_side_y), (drx, down_side_y), (blue, 0, red), thickness)
    cv2.line(img, (ulx, down_side_y), (ulx, height), (blue, 0, red), thickness)
    cv2.line(img, (ulx, height), (drx, height), (blue, 0, red), thickness)
    cv2.line(img, (drx, height), (drx, down_side_y), (blue, 0, red), thickness)

def rotational_homothety(degrees, thickness):
    global rdlx
    global rdly
    global rulx
    global ruly
    global rurx
    global rury
    global rdrx
    global rdry

    down_side_y = int(height+fabs(ulx - drx)) if int(height+fabs(ulx - drx)) <= ground_height else ground_height

    rdlx = ulx if rdlx == 0 else rdlx
    rdly = ground_height if rdly == 0 else rdly
    rulx = ulx if rulx == 0 else rulx
    ruly = height if ruly == 0 else ruly
    rurx = drx if rurx == 0 else rurx
    rury = height if rury == 0 else rury
    rdrx = drx if rdrx == 0 else rdrx
    rdry = ground_height if rdry == 0 else rdry

    rdlx -= int(fabs(tulx + tdrx) / 2)
    rdly -= int(fabs(ground_height + theight) / 2)
    rulx -= int(fabs(tulx + tdrx) / 2)
    ruly -= int(fabs(ground_height + theight) / 2)
    rurx -= int(fabs(tulx + tdrx) / 2)
    rury -= int(fabs(ground_height + theight) / 2)
    rdrx -= int(fabs(tulx + tdrx) / 2)
    rdry -= int(fabs(ground_height + theight) / 2)

    rdlx = int(rdlx * math.cos(degrees) - (rdly * math.sin(degrees)))
    rdly = int(rdly * math.cos(degrees) + (rdlx * math.sin(degrees)))
    rulx = int(rulx * math.cos(degrees) - (ruly * math.sin(degrees)))
    ruly = int(ruly * math.cos(degrees) + (rulx * math.sin(degrees)))
    rurx = int(rurx * math.cos(degrees) - (rury * math.sin(degrees)))
    rury = int(rury * math.cos(degrees) + (rurx * math.sin(degrees)))
    rdrx = int(rdrx * math.cos(degrees) - (rdry * math.sin(degrees)))
    rdry = int(rdry * math.cos(degrees) + (rdrx * math.sin(degrees)))

    rdlx += int(fabs(tulx + tdrx) / 2)
    rdly += int(fabs(ground_height + theight) / 2)
    rulx += int(fabs(tulx + tdrx) / 2)
    ruly += int(fabs(ground_height + theight) / 2)
    rurx += int(fabs(tulx + tdrx) / 2)
    rury += int(fabs(ground_height + theight) / 2)
    rdrx += int(fabs(tulx + tdrx) / 2)
    rdry += int(fabs(ground_height + theight) / 2)

    cv2.line(img, (rdlx, rdly), (rdrx, rdry), (blue, 0, red), thickness)
    cv2.line(img, (rdlx, rdly), (rulx, ruly), (blue, 0, red), thickness)
    cv2.line(img, (rulx, ruly), (rurx, rury), (blue, 0, red), thickness)
    cv2.line(img, (rurx, rury), (rdrx, rdry), (blue, 0, red), thickness)

    cv2.imshow('homothety', img)

def rotational_homothety_changing_center(degrees, thickness):
    global rdlx
    global rdly
    global rulx
    global ruly
    global rurx
    global rury
    global rdrx
    global rdry

    down_side_y = int(height+fabs(ulx - drx)) if int(height+fabs(ulx - drx)) <= ground_height else ground_height

    rdlx = ulx if rdlx == 0 else rdlx
    rdly = ground_height if rdly == 0 else rdly
    rulx = ulx if rulx == 0 else rulx
    ruly = height if ruly == 0 else ruly
    rurx = drx if rurx == 0 else rurx
    rury = height if rury == 0 else rury
    rdrx = drx if rdrx == 0 else rdrx
    rdry = ground_height if rdry == 0 else rdry

    rdlx -= int(fabs(ulx + drx) / 2)
    rdly -= int(fabs(ground_height + height) / 2)
    rulx -= int(fabs(ulx + drx) / 2)
    ruly -= int(fabs(ground_height + height) / 2)
    rurx -= int(fabs(ulx + drx) / 2)
    rury -= int(fabs(ground_height + height) / 2)
    rdrx -= int(fabs(ulx + drx) / 2)
    rdry -= int(fabs(ground_height + height) / 2)

    rdlx = int(rdlx * math.cos(degrees) - (rdly * math.sin(degrees)))
    rdly = int(rdly * math.cos(degrees) + (rdlx * math.sin(degrees)))
    rulx = int(rulx * math.cos(degrees) - (ruly * math.sin(degrees)))
    ruly = int(ruly * math.cos(degrees) + (rulx * math.sin(degrees)))
    rurx = int(rurx * math.cos(degrees) - (rury * math.sin(degrees)))
    rury = int(rury * math.cos(degrees) + (rurx * math.sin(degrees)))
    rdrx = int(rdrx * math.cos(degrees) - (rdry * math.sin(degrees)))
    rdry = int(rdry * math.cos(degrees) + (rdrx * math.sin(degrees)))

    rdlx += int(fabs(ulx + drx) / 2)
    rdly += int(fabs(ground_height + height) / 2)
    rulx += int(fabs(ulx + drx) / 2)
    ruly += int(fabs(ground_height + height) / 2)
    rurx += int(fabs(ulx + drx) / 2)
    rury += int(fabs(ground_height + height) / 2)
    rdrx += int(fabs(ulx + drx) / 2)
    rdry += int(fabs(ground_height + height) / 2)

    cv2.line(img, (rdlx, rdly), (rdrx, rdry), (green_changing_for_next_state, blue, red), thickness)
    cv2.line(img, (rdlx, rdly), (rulx, ruly), (green_changing_for_next_state, blue, red), thickness)
    cv2.line(img, (rulx, ruly), (rurx, rury), (green_changing_for_next_state, blue, red), thickness)
    cv2.line(img, (rurx, rury), (rdrx, rdry), (green_changing_for_next_state, blue, red), thickness)

    cv2.imshow('homothety', img)

def move_object(left, right, show_previous_state):
    global k
    global height
    global ulx
    global drx
    global img
    global green_changing_for_next_state
    global direction

    k = fabs(ulx - drx)
    #print(str(k))
    if right == 0:
        ulx -= left * 2
        drx -= left
        height -= left
    elif left == 0:
        ulx += right * 2
        drx += right
        height += right
    if show_previous_state != 1:
        global rdlx
        global rdly
        global rulx
        global ruly
        global rurx
        global rury
        global rdrx
        global rdry
        rdlx = 0
        rdly = 0
        rulx = 0
        ruly = 0
        rurx = 0
        rury = 0
        rdrx = 0
        rdry = 0
        global tulx
        global tdrx
        global theight
        tulx = ulx
        tdrx = drx
        theight = height

        direction = 0
        green_changing_for_next_state = green
        img = np.zeros((window_height, window_width, 3), dtype = "uint8")
        cv2.rectangle(img, (ulx, height), (drx, ground_height), (blue, green, red), 3)
        try:
            k = (drx - ulx) / k
            #print(str(drx - ulx))
            #print(str(k))
        except ZeroDivisionError:
            k = 0
        cv2.line(img, (0, 280), (window_width, 280), (255, 255, 255), 1)
        cv2.putText(img, 'k = ' + str(k), (50, 50),
                    font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    else:
        if green_changing_for_next_state >= gradiant and direction == 0:
            green_changing_for_next_state -= gradiant
            if(green_changing_for_next_state <= gradiant):
                direction = 1
        elif direction == 1 and green_changing_for_next_state < 255:
            green_changing_for_next_state += gradiant
        else:
            direction = 0
        if check == 2:
            rotational_homothety_changing_center(270, 3)
        cv2.rectangle(img, (ulx, height), (drx, ground_height), (blue, green_changing_for_next_state, red), 3)

    cv2.imshow('homothety', img)

def change_step():
    global img
    global step

    img = np.zeros((window_height, window_width, 3), dtype = "uint8")
    cv2.putText(img, 'Step =  ' + str(step), (50, 50),
        font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.rectangle(img, (ulx, height), (drx, ground_height), (blue, green, red), 3)
    cv2.line(img, (0, 280), (window_width, 280), (255, 255, 255), 1)
    cv2.imshow('homothety', img)
    temp = step
    step = 0
    digits = string.digits
    while True:
        key = cv2.waitKey(1)
        for digit in digits:
            if key == ord(digit):
                step = int(digit) + (step * 10)
                img = np.zeros((window_height, window_width, 3), dtype = "uint8")
                cv2.putText(img, 'Step =  ' + str(step), (50, 50),
                    font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.rectangle(img, (ulx, height), (drx, ground_height), (blue, green, red), 3)
                cv2.line(img, (0, 280), (window_width, 280), (255, 255, 255), 1)
                cv2.imshow('homothety', img)
        if key == ord('\n') or key == ord('\r'):
            if step == 0:
                step = temp
            break
    print(str(step))

cv2.rectangle(img, (ulx, height), (drx, ground_height), (blue, green, red), 3)
cv2.line(img, (0, 280), (window_width, 280), (255, 255, 255), 1)
cv2.putText(img, 'k = ' + str(k), (50, 50),
            font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('homothety', img)

while True:
    value = cv2.waitKeyEx()
    check = 0 if check != 2 else 2
    if value == 2490368 and ulx > 0 and height > 0:
        print("Up")
        move_object(step, 0, 0)
    elif value == 2621440 and ulx < window_width and height < window_height:
        print("Down")
        move_object(0, step, 0)
    elif value == 119 and ulx > 0 and height > 0:
        print("Up with previous state shown")
        move_object(step, 0, 1)
    elif value == 115 and ulx < window_width and height < window_height:
        print("Down with previous state shown")
        move_object(0, step, 1)
    elif value == 113:
        change_step()
    elif value == 114:
        rotational_homothety(270, 3)
    elif value == 116:
        check = 1
        rotational_homothety_changing_center(270, 3)
    elif value == 101:
        check = 2 if check != 2 else 0
    elif value != 2490368 and value != 2621440 and value != 119 and value != 115 and value != 113 and value != 114 and value != 116 and value != 101:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
