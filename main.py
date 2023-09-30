from rgb import RGB
from time import sleep

RGB_instance = RGB()

while True:
    RGB_instance.set_color("red")
    sleep(1)
    RGB_instance.set_color("green")
    sleep(1)
    RGB_instance.set_color("blue")
    sleep(1)


