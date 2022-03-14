from concurrent.futures import thread
import datetime
from logging.config import listen
from pynput.mouse import Listener
from pynput import mouse
from pynput import keyboard
import time
import os
import timer
import platform
from time import sleep
from threading import Thread

os_is = platform.system()
os_release = platform.release()

DEFAULT_IDLE_INFO = 15
DEFAULT_IDLE_TIME = 900


def on_move(timer_start, timer_stop):
    timer_start = time.asctime()
    timer_stop = time.asctime()
    print(f"Moving Mouse Start {timer_start} and Stop {timer_stop}")


def on_scroll(timer_start, timer_stop, dx, dy):
    timer_start = time.asctime()
    timer_stop = time.asctime()
    print(f"Scrolling Start {timer_start} and Stop {timer_stop}")


listener = mouse.Listener(
    on_move=on_move,
    on_scroll=on_scroll)
listener.start()


def on_press(key):
    time_start = time.asctime()
    time_end = time.asctime()
    try:
        print(f'Press Start {time_start} Pressed Ended {time_end}'.format(
            key.char))
    except AttributeError:
        print(f' Start Pressing Special Key {time_start} Pressed Ended {time_end}'.format(
            key))


def on_release(key):
    time_start = time.asctime()
    time_end = time.asctime()
    print('{0} Pressed Keyboard Value'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


date_time = time.asctime()


while True:

    with mouse.Events() as events:
        # Block at most one second
        event1 = events.get(DEFAULT_IDLE_TIME)
        if event1 is None:
            print(
                f'You did not interact with the mouse within {DEFAULT_IDLE_INFO} minutes will shutdown device now')
            sleep(10)
            # flexible both windows os and linux, just type the right command for the dedicated os
            print(os.system("sudo init 0"))
        else:
            print(
                f"Received mouse movements dated {date_time} with OS {os_is} {os_release}")

    while True:

        with keyboard.Events() as events:
            # Block at most one second
            event2 = events.get(DEFAULT_IDLE_TIME)
            if event2 is None:
                print(
                    f'You did not interact with the keyboard within {DEFAULT_IDLE_INFO} minutes will shutdown device now')
                sleep(10)
                # flexible both windows os and linux, just type the right command for the dedicated os
                print(os.system("sudo init 0"))
            else:
                print(
                    f"Received mouse movements dated {date_time} with OS {os_is} {os_release}")
