import pyautogui

pyautogui.hotkey("alt","tab")

pyautogui.click(x=593, y=938)

#pyautogui.press("home")

def marcar():
    pyautogui.hotkey("shift","down")    
    pyautogui.press("m")

for i in range(30):
    marcar()