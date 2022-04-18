from pynput import mouse
from pynput import keyboard
import time
import os


def on_move(x, y):
    global LastTime
    LastTime = time.time()


def on_click(x, y, button, pressed):
    global LastTime
    LastTime = time.time()


def on_scroll(x, y, dx, dy):
    global LastTime
    LastTime = time.time()


def on_press(key):
    global LastTime
    LastTime = time.time()


LastTime = time.time()

listener = keyboard.Listener(on_press=on_press)
listener.start()

listener = mouse.Listener(
    on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()

while True:
    time.sleep(0.2)

    if time.time()-LastTime >= 900:  # the break time,5 is second
        print(os.system("sudo init 0"))
        LastTime = time.time()
