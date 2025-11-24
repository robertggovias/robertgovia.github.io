import pyautogui

pyautogui.hotkey("alt", "tab")
with pyautogui.hold('alt'):
    pyautogui.press(['tab','tab'])    
pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("alt", "tab")
def takename():    
    pyautogui.press('F2')    
    pyautogui.hotkey("ctrl", "c")    
    pyautogui.hotkey("alt", "tab")    
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.hotkey("alt", "tab")    
    pyautogui.press('right')    

for i in range(19):
    takename()