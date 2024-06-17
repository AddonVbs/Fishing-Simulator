from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time
import keyboard as ky
import mouse 
S = "s"
W = "W"
A = "a"
D = "d"
E = "e"


#print("write how much space you have in your bag") 
#bag = int(input())

#if bag == str:
    #print("you didn't enter numbers :) change over")

#print("record the number of clicks required to reeling speed")
#farm = int(input())

#if farm  == str:
    #print("you didn't enter numbers :) change over")







def glick():
    click_mouse()
    time.sleep(1)
    ky.press("win")
    time.sleep(0.6)
    ky.release("win")
    time.sleep(1)
    click_mouse()
    time.sleep(1)
    ky.press("win")
    time.sleep(0.6)
    ky.release("win")
    time.sleep(1)
    click_mouse()


def click_mouse():
    mouse.press(Button.left) 
    mouse.release(Button.left)

mouse = MouseController()
Keyboard = KeyboardController()

time.sleep(20)
ky.press("w")
time.sleep(4)
ky.release("w")
time.sleep(1)
            
ky.press("a")
time.sleep(1)
ky.release("a")
time.sleep(1)
            
            
ky.press("w")
time.sleep(5.7)
ky.release("w")
time.sleep(1)






time.sleep(2)
for i in range(10000):


    ky.press("e")
    ky.release("e")
    time.sleep(3)

    click_mouse()

    mouse.position = (1209, 429)
    time.sleep(1)
    click_mouse()
    time.sleep(1)
    click_mouse()

    click_mouse()
    glick()
    click_mouse()
    time.sleep(1)
    click_mouse()
    click_mouse()
    time.sleep(1)
    click_mouse()
    click_mouse()

    time.sleep(1)
    
    mouse.position = (1356, 574)
    
    click_mouse()
    glick()
    time.sleep(1)
    click_mouse()
    time.sleep(1)
    mouse.press(Button.left) 
    mouse.release(Button.left)
    time.sleep(1)
    click_mouse()
    click_mouse()
    time.sleep(1)
    click_mouse()
    click_mouse()
    time.sleep(1)
    click_mouse()
    click_mouse()


    ky.press("a")
    time.sleep(5.7)
    ky.release("a")
    time.sleep(1)

    ky.press("w")
    time.sleep(1.4)
    ky.release("w")
    time.sleep(1)

    ky.press("a")
    time.sleep(1.7)
    ky.release("a")
    time.sleep(1)
    
    
    ky.press("1")
    ky.release("1")
    time.sleep(1)
    ky.press("1")
    ky.release("1")
    time.sleep(1)
    ky.press("1")
    ky.release("1")
    time.sleep(1)
    ky.press("2")
    ky.release("2")
    time.sleep(1)
    ky.press("1")
    ky.release("1")
    time.sleep(1)
    click_mouse()
    time.sleep(1)
    ky.press("win + d")
    ky.release("win + d")
    time.sleep(1)
    click_mouse()
    time.sleep(1)
    ky.press("win + d")
    ky.release("win + d")
    time.sleep(1)
    ky.press("1")
    ky.release("1")
    time.sleep(1)
    ky.press("1")
    ky.release("1")

    time.sleep(1)
    for i in range(300):                 #Закинул удочку
        mouse.press(Button.left) 
        mouse.release(Button.left)
        time.sleep(3.5)
    
        for i in range(8):                 #Фарм
            time.sleep(0.5)
            mouse.press(Button.left) 
            mouse.release(Button.left)
    
    ky.press("d")
    time.sleep(2.36)
    ky.release("d")
    time.sleep(1)

    ky.press("s")
    time.sleep(1.4)
    ky.release("s")
    time.sleep(1)

    ky.press("d")
    time.sleep(2.08)
    ky.release("d")
    time.sleep(1)
    
