import pyautogui
pyautogui.hotkey("alt","tab")
x=1.5



def clicks1():        
    pyautogui.click(x=534, y=422)    
    pyautogui.PAUSE=1
    pyautogui.hotkey("shift","d")    
    pyautogui.PAUSE=1    
    pyautogui.press("g")    
    pyautogui.PAUSE=0.2        
    pyautogui.moveTo(x=597, y=278)
    pyautogui.press("esc")
    pyautogui.click(x=1330, y=524)    
    pyautogui.PAUSE=0.2  
for i in range(4):
    clicks1()            
    pyautogui.PAUSE=0.2            
    sumM=i*x
    suma=str(sumM)
    pyautogui.write(suma)
    pyautogui.PAUSE=0.2                
    pyautogui.press("enter")
    pyautogui.PAUSE=0.2     
    pyautogui.press("esc")       
    pyautogui.PAUSE=0.5     
        

