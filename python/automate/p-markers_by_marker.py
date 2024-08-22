import pyautogui
a = "x=593, y=938"
pyautogui.hotkey("alt","tab")

pyautogui.click(x=593, y=938)



def marcar():
    pyautogui.PAUSE = .4
    pyautogui.click(x=593, y=938)
    pyautogui.hotkey("shift","m")
    pyautogui.click(x=593, y=938)
    pyautogui.hotkey("shift","m")    
    pyautogui.press("m")

for i in range(13):
    marcar()