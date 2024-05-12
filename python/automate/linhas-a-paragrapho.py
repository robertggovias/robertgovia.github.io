import pyautogui

pyautogui.hotkey("alt","tab")

def takeEndSpace():
    pyautogui.press('end')
    pyautogui.press('space')
    pyautogui.press('delete')    
for i in range (53):
    takeEndSpace()