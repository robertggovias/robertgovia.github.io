import pyautogui

pyautogui.hotkey("alt", "tab")


def takeOfLInes():
    with pyautogui.hold('shift'):
        pyautogui.press(['end','down','delete'])
    pyautogui.press('delete')
    for i in range (2):
        pyautogui.press("down")                
for i in range (27):
    takeOfLInes()