import pyautogui
pyautogui.hotkey('alt','tab')

def pepinho():
    pyautogui.hotkey('ctrl','alt','down')
    pyautogui.hotkey('ctrl','shift','k')

for i in range(9):
    pepinho()