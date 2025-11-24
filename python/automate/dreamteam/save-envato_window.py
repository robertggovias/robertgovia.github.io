import pyautogui

pyautogui.hotkey("alt", "tab")
def copyTitle():
    pyautogui.click(x=920, y=640)
    pyautogui.PAUSE=0.1
    pyautogui.click(x=920, y=640)
    pyautogui.hotkey("end")    
    with pyautogui.hold('ctrl'):
        pyautogui.press(['left','left','left','left','left','left','left','left'])    
    pyautogui.press('left')    
    with pyautogui.hold('shift'):
        pyautogui.press('home')
    pyautogui.hotkey("ctrl","v")
def clickSave():    
    pyautogui.click(x=1840, y=412)
    pyautogui.click(x=1840, y=440)
    pyautogui.click(x=1840, y=460)
    pyautogui.moveTo(x=985, y=474)    
    pyautogui.PAUSE=2.4
    pyautogui.click(x=985, y=474)    
    pyautogui.PAUSE=0.5
    pyautogui.click(x=1038, y=1201)
copyTitle()