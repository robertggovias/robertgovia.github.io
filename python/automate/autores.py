import pyautogui
pyautogui.hotkey("alt","tab")
x=20



def clicks1():        
    pyautogui.click(x=902, y=515)
    pyautogui.PAUSE=0.2
    pyautogui.click(x=491, y=630)    
    pyautogui.PAUSE=0.2
    pyautogui.click(x=532, y=530)
    pyautogui.PAUSE=0.2
    pyautogui.press("enter")
    
for i in range(20):
    clicks1()            
"""     pyautogui.PAUSE=0.2            
    sumM=i+x
    suma=str(sumM)+("-")
    pyautogui.write(suma)
    pyautogui.PAUSE=0.2   
   for f in range (5):
        pyautogui.press("keyUp")             
    pyautogui.press("enter")
    pyautogui.PAUSE=0.2     
    """

