import pyautogui
pyautogui.hotkey('alt','tab')
def take_video():    
    pyautogui.hotkey('shift','m')
    pyautogui.hotkey('ctrl','k')

for i in range(3):
    take_video()