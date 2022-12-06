import pyautogui
pyautogui.hotkey("alt","tab")
x=2
a=str(16)
b=str(8)
letra="C"
logotipo=a+"x"+b+"- "+letra+" L"
def clicks1():
    pyautogui.click(x=741, y=506)
    pyautogui.click(x=760, y=749)
    pyautogui.PAUSE=0.27   
    pyautogui.click(x=780, y=541)
    pyautogui.PAUSE=0.17   
def clicks2():    
    pyautogui.PAUSE=0.27    
    pyautogui.click(x=251, y=570)
    pyautogui.moveTo(x=251, y=570)
    pyautogui.dragTo(x=1045, y=802,duration=0.8)
    pyautogui.hotkey("x")
    pyautogui.PAUSE=0.17  
    pyautogui.click(x=584, y=611)
    pyautogui.hotkey("ctrl","v")
       
def logotipando():
    for i in range(4):
        clicks1()                      
        logotipos=logotipo+str(i+x)
        pyautogui.write(logotipos)
           
        clicks2()

logotipando()