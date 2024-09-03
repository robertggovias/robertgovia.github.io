import pyautogui
pyautogui.hotkey("alt",'tab')
def pepe():    
    pyautogui.keyDown('shift')
    pyautogui.press('end')
    pyautogui.keyUp('shift')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('down')
    pyautogui.press('delete')    

for i in range(6):
    pepe()