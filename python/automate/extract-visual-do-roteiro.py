import pyautogui

pyautogui.hotkey("alt", "tab")

def takeOfLInes():
    with pyautogui.hold('shift'):
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")        
        pyautogui.press('delete')
    for i in range (2):
        pyautogui.press("down")                        

for i in range (32):
    takeOfLInes()