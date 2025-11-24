import pyautogui
pyautogui.hotkey("alt", "tab")
def spiral():
    pyautogui.moveTo(x=920, y=640)
    pyautogui.PAUSE=0.5
    pyautogui.moveTo(x=1840, y=412, duration=0.5)
    """ pyautogui.press("esc") """
    pyautogui.PAUSE=0.3
    pyautogui.moveTo(x=1840, y=440, duration=0.5)
    pyautogui.PAUSE=2.4
    """ pyautogui.press("esc") """
    pyautogui.moveTo(x=1840, y=460, duration=0.5)
    pyautogui.PAUSE=0.4
    pyautogui.moveTo(x=985, y=474, duration=0.5)
    """ pyautogui.press("esc") """
    pyautogui.PAUSE=1.4
    pyautogui.moveTo(x=985, y=474, duration=0.5)
    pyautogui.PAUSE=0.2
    pyautogui.moveTo(x=1038, y=1201, duration=0.5)
    """ pyautogui.press("esc") """

for i in range(300):
    spiral()