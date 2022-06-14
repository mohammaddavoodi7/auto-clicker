import pyautogui as pt
from time import sleep

# https://mouseaccuracy.com/

pt.FAILSAFE = True


def nav_to_image(image, clicks):
    try:
        position = pt.locateCenterOnScreen(image, confidence=.8)
        pt.moveTo(position, duration=.0001)
        pt.click(clicks=clicks, interval=.1)
    except Exception as e:
        print(f'{image} not found...', e)


sleep(2)
nav_to_image('.\images\start.png', 2)
sleep(3)
for i in range(30):
    nav_to_image('.\images\click.png', 1)
