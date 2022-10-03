from asyncore import write
import string
import pyautogui
from datetime import timedelta
x=timedelta(hours=00,minutes=00,seconds=00,microseconds=00)
y=timedelta(hours=00,minutes=00,seconds=20,microseconds=00)
def mySeconds():
    pyautogui.click(x=70, y=364)
    pyautogui.typewrite(z)
    pyautogui.press("enter")
    pyautogui.click(x=249, y=424)
    pyautogui.press("m")

pyautogui.hotkey("alt","tab")
for i in range(96):    
    z = str(x+y)+":00"
    mySeconds()
    x = x + y
    
