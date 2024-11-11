import pyautogui

pyautogui.hotkey("alt", "tab")


def takeOfLInes():    
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('space')
    pyautogui.press('home')
    
for i in range (12):
    takeOfLInes()