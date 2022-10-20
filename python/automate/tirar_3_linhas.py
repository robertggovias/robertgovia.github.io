import pyautogui
pyautogui.hotkey("alt", "tab")
def takeOfLInes():
    pyautogui.press("down")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("down")    
for i in range (30):
    takeOfLInes()