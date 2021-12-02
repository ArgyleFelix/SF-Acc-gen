import numpy  
import pytesseract
import cv2
import time
import pyautogui
import win32api
import win32con
import keyboard
import random
import string
import os
from PIL import ImageGrab

#scrolling down 17 times with down arrow
def scrolldown():
    for i in range(17):
        pyautogui.press("down")

#scrolling up 17 times with up arrow        
def scrollup():
    for i in range(17):
        pyautogui.press("up")

#creating the caracter
def CaracterCreation():
    
    #details
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)) #random alphanumeric generator
    link = "https://temp-mail.org/hu/"
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    #new
    click1 = 771, 784
    pyautogui.moveTo(click1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #arrow
    r = random.randint(1,9)
    for i in range(r):
        click2 = 1360, 932
        pyautogui.moveTo(click2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #create
    click3 = 1134, 936
    pyautogui.moveTo(click3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #get class name (read string from display (#start x, start y, end x, end y))
    #start x, start y, end x, end y
    getclasstype = ImageGrab.grab(bbox =(233, 549, 408, 602))
    classtype = pytesseract.image_to_string(cv2.cvtColor(numpy.array(getclasstype), cv2.COLOR_BGR2GRAY), lang ='eng')

    time.sleep(2)

    #dice
    click4 = 1581, 772
    pyautogui.moveTo(click4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #name (read string from display (#start x, start y, end x, end y))
    getname = ImageGrab.grab(bbox =(1250, 745, 1555, 806))
    name = pytesseract.image_to_string(cv2.cvtColor(numpy.array(getname), cv2.COLOR_BGR2GRAY), lang ='eng')

    time.sleep(2)

    #making the text file or if it already exists then just editing it
    while True:
        if os.path.isfile("Account List.txt") == True:
            with open("Account List.txt", "r+") as f:
                old = f.read()
                f.seek(0)
                name = name.replace('\f','')
                classtype = classtype.replace('\f','')
                f.write(old + name + "\n" + password + "\n" + classtype + "\n")
                break
        else:
                f= open("Account List.txt", "w+")
                f.write("")
                f.close
                continue

    time.sleep(2)

    #save
    click5 = 1134, 936
    pyautogui.moveTo(click5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)            

    time.sleep(2)

    #exclamation mark
    click6 = 229, 148
    pyautogui.moveTo(click6)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #password
    click7 = 1116, 591
    pyautogui.moveTo(click7)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    keyboard.write(password)
    pyautogui.press("tab")     
    keyboard.write(password)   

    time.sleep(2)

    #new browser tab
    click8 = 272, 16
    pyautogui.moveTo(click8)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #open temp mail
    time.sleep(3)
    click9 = 1200, 55
    pyautogui.moveTo(click9)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    keyboard.write(link)
    pyautogui.press("return")

    time.sleep(10)

    scrollup()

    time.sleep(5)

    #change email
    click10 = 1220, 567
    pyautogui.moveTo(click10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(15)

    #copy email
    click11 = 1154, 309
    pyautogui.moveTo(click11)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #back to sf page
    click12 = 146, 17
    pyautogui.moveTo(click12)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)

    #paste email
    click13 = 1124, 747
    pyautogui.moveTo(click13)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")    
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    #send email
    click14 = 1142, 922
    pyautogui.moveTo(click14)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)   
    
    #go back to tempmail
    scrollup()
    time.sleep(3)
    click15 = 369, 19
    pyautogui.moveTo(click15)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)     

    time.sleep(45) 

    #open mail
    click16 = 814, 737
    pyautogui.moveTo(click16)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

    time.sleep(5)

    scrolldown()   

    time.sleep(2)   

    #click link in mail
    click17 = 731, 924
    pyautogui.moveTo(click17)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

    time.sleep(2) 

    #back to sf page
    click18 = 146, 17
    pyautogui.moveTo(click18)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)  

    time.sleep(2)  

    #log out of sf
    click19 = 430, 1020
    pyautogui.moveTo(click19)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      
    time.sleep(0.5)  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    time.sleep(2)                      

#execution function loop with int value as a loop round
try:
    print("How many accounts do you want?")
    for i in range(int(input())):
        CaracterCreation()
        print("Done")
except KeyboardInterrupt:
    pass