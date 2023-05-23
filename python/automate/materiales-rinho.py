import pyautogui
import time
#nombre
pyautogui.hotkey("Alt","Tab")
ynome = 265
ytriggernome = 265
ywritenome = 200
ycolor = 289
suma = 19
oi = 23
def createName():    
    
    pyautogui.moveTo(x=1139, y=ynome)
    pyautogui.doubleClick(x=1139, y=ynome)
    pyautogui.click(x=1139, y=ynome)
    pyautogui.hotkey("ctrl","a")    
    pyautogui.hotkey("Ctrl","c")
    pyautogui.moveTo(x=1315, y=ytriggernome)
    pyautogui.click(x=1315, y=ytriggernome)
    pyautogui.moveTo(x=550, y=243)
    pyautogui.click(x=550, y=243)   
    pyautogui.hotkey("ctrl","a")    
    pyautogui.press("delete") 
    pyautogui.hotkey("Ctrl","v")
    #ok nome    
    pyautogui.click(x=687, y=756)



for ja in range(9):
    ynome = ynome + suma
    ytriggernome = ytriggernome + suma
    ywritenome = ywritenome + suma
    ycolor = ycolor + suma

for i in range(19):
    createName()  
    ynome = ynome + suma
    ytriggernome = ytriggernome + suma
    ywritenome = ywritenome + suma
    ycolor = ycolor + suma