import pyautogui

pyautogui.hotkey("alt", "tab")

def takeOfLInes():
    with pyautogui.hold('shift'):
        pyautogui.press(['down','end','delete'])
        pyautogui.press('delete')
    for i in range (1):
        pyautogui.press("down")                
        pyautogui.press("delete") 

for i in range (88):
    takeOfLInes()