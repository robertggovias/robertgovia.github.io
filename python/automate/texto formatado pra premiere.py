import pyautogui
pyautogui.hotkey("alt", "tab")

def copiarIllustratorPegarPremiere():    
    pyautogui.press('home')    
    with pyautogui.hold('shift'):
        pyautogui.press('end')
    pyautogui.hotkey("ctrl","c")
    pyautogui.doubleClick(x=2256, y=962)
    pyautogui.press('home')        
    with pyautogui.hold('shift'):
        pyautogui.press('end')    
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl','v')
    pyautogui.click(x=1592, y=971)
    pyautogui.hotkey('shift','down')
    pyautogui.hotkey("alt", "tab")    
    pyautogui.press('down')    
    pyautogui.press('down')

for i in range(5):
    copiarIllustratorPegarPremiere()