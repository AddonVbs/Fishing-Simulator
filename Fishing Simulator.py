from pynput.mouse import Button, Controller
import time
mouse = Controller()

time.sleep(2)

mouse.press(Button.left) 
mouse.release(Button.left)