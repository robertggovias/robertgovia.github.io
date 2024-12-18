import pyautogui

pyautogui.hotkey("alt", "tab")


def takeOfLInes():
    with pyautogui.hold('shift'):
        pyautogui.press(['end','delete'])
    pyautogui.press('delete')
    for i in range (1):
        pyautogui.press("down")                
for i in range (98):
    takeOfLInes()