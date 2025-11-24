import pyautogui

pyautogui.hotkey("alt", "tab")

def tabs(e):
    for i in range(e):
        pyautogui.press('tab')

def copyTitle():    
    pyautogui.click(x=1421, y=60)    
    pyautogui.click(x=1421, y=60)    
    pyautogui.press("right")    
    pyautogui.hotkey("home")    
    with pyautogui.hold('ctrl'):
        pyautogui.press(['right','right','right','right','right'])    
    with pyautogui.hold('shift'):
        pyautogui.press('end')
    pyautogui.hotkey("ctrl","c")
def pressDownload():    
    pyautogui.click(x=2435, y=446)
    tabs(5)
    pyautogui.press("enter")
def chooseProject():        
    tabs(4)
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press('enter')
def pasteTitle():
    pyautogui.hotkey("right")    
    pyautogui.hotkey("end")    
    with pyautogui.hold('ctrl'):
        pyautogui.press(['left','left','left','left','left','left','left','left'])    
    pyautogui.press('left')    
    with pyautogui.hold('shift'):
        pyautogui.press('home')
    pyautogui.hotkey("ctrl","v")
    pyautogui.press('enter')

""" pyautogui.click(x=1840, y=412)
    pyautogui.click(x=1840, y=440)
    pyautogui.click(x=1840, y=460)
    pyautogui.moveTo(x=985, y=474)    
    pyautogui.PAUSE=2.4
    pyautogui.click(x=985, y=474)    
    pyautogui.PAUSE=0.5
    pyautogui.click(x=1038, y=1201) """
copyTitle()
pressDownload()
pyautogui.PAUSE=1
chooseProject()
pasteTitle()