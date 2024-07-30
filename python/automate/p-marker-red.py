import pyautogui

pyautogui.hotkey("alt","tab")

pyautogui.click(x=873, y=929)
#pyautogui.press("home")

def goRed():
    pyautogui.hotkey("shift","m")
    pyautogui.hotkey("shift","m")
    pyautogui.press("m")
    pyautogui.PAUSE = .4
    pyautogui.click(x=1222, y=600)
    pyautogui.PAUSE = .2
    pyautogui.click(x=1458, y=404)
    pyautogui.PAUSE = 1.5
    
for i in range (10):
    goRed()