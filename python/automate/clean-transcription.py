import pyautogui

pyautogui.hotkey("alt", "tab")


def takeOfLInes():
    with pyautogui.hold('shift'):
        pyautogui.press('end')
    pyautogui.press('delete')            
    pyautogui.press('delete')
    pyautogui.press('down')               
    pyautogui.press('delete')    
for i in range (24):
    takeOfLInes()