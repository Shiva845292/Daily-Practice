import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE= False
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
while True:
    time.sleep(170)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("slp is competed",current_time)
    now1 = datetime.now()
    for i in range(5):
        pyautogui.moveTo(1,i)
    for k in range(3):
        pyautogui.press('shift')
# print("Current Time =", current_time)
# current_time1 = now1.strftime("%H:%M:%S")
# print("Current Time =", current_time1)
# print("completed Task")