#Dependency
from email import message
import pyautogui as gui
import time
import random, string

numMessage = input("Enter number of message: ")

time.sleep(5)

for i in range(int(numMessage)):
    text = string.ascii_lowercase
    message = "".join(random.sample(text, 10))
    gui.typewrite(message)
    gui.press("Enter")
