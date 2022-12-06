import pyautogui
pyautogui.hotkey("alt","tab")
x=1
col = 1
a=str(16)
b=str(6)
letra="C"
color=a+"x"+b+"- "+letra+" C"
logotipo=a+"x"+b+"- "+letra+" L"
def clicks1():
    pyautogui.click(x=741, y=506)
    pyautogui.click(x=760, y=749)
    pyautogui.PAUSE=0.27   
def clicks2():
    pyautogui.press("enter")
    pyautogui.PAUSE=0.27
    pyautogui.click(x=1421, y=381)
    pyautogui.hotkey("delete")
    pyautogui.hotkey("paste")

def coloreando():
    for z in range(2):
        clicks1()
        colores=color+str(col+z)
        pyautogui.click(x=1329, y=503)
        pyautogui.write(colores)
        clicks2()
        
def logotipando():
    for i in range(5):
        clicks1()        
        logotipos=logotipo+str(x+i)    
        pyautogui.click(x=1329, y=503)
        pyautogui.write(logotipos)
        clicks2()
coloreando()
logotipando()