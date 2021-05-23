import pyautogui
import pydirectinput
import time

start_time = time.time()
i = 0
a = 0
t = 0
change = 3

while True:
    space_time = time.time() - start_time - i
    time_now = time.time() - start_time - t
    done_time = time.time() - start_time - a
    stick = pyautogui.locateAllOnScreen('bombhead.png',grayscale=True,region=(596,869,554,170),confidence=0.75)
    tank = pyautogui.locateAllOnScreen('tank.png',grayscale=True,region=(550,800,554,190),confidence=0.4)
    if stick != None:
        for elem in stick:
            pyautogui.tripleClick(x=(elem.left+27),y=(elem.top+12))
    if tank != None:
        for elem in tank:
            print(elem)
            pyautogui.tripleClick(x=(elem.left+27),y=(elem.top+12))
    if space_time > change:
        pydirectinput.press('space')
        i += change
    if time_now > 180 and change < 20:
        change += 1
        t += 60
    if done_time > 5:
        clip = pyautogui.locateOnScreen('clip.png',grayscale=True,region=(586,541,1314,1079),confidence=0.6)
        if clip != None:
            for z in range(10):
                pyautogui.tripleClick(x=(clip.left+20),y=(clip.top+20))
        done = pyautogui.locateOnScreen('realdone.png',grayscale=True,region=(596,869,554,170),confidence=0.4)
        if done != None:
            pyautogui.click(x=done.left,y=done.top)
        a += 5
