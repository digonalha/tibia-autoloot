#!/usr/bin/env python3

from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
import time

mouse = mouse_controller()
keyboard = keyboard_controller()

positions = [
    (794, 291),
    (743, 292),
    (749, 336),
    (742, 384),
    (792, 392),
    (856, 387),
    (857, 334),
    (859, 276),
    (803, 329)
]

def pick_loot_around():
    original_position = mouse.position

    for i in positions:
        mouse.position = i
        time.sleep(0.01)

        with keyboard.pressed(Key.shift):
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(0.01)
        
    mouse.position = original_position

if (__name__ == "__main__"):
    pick_loot_around()
