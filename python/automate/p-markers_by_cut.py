import pyautogui
a = "x=593, y=938"
pyautogui.hotkey("alt","tab")

pyautogui.click(x=593, y=938)

pyautogui.press("home")

def marcar():
    pyautogui.hotkey("shift","down")
    pyautogui.PAUSE = .4
    pyautogui.click(x=593, y=938)
    pyautogui.PAUSE = .4
    pyautogui.press("m")

for i in range(37):
    marcar()