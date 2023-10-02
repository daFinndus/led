import os
from time import sleep

from button import Button
from led import LED
from rgb import RGB


# Function to clear all pins and then shutdown
def shutdown_pi(RGB_device):
    RGB_device.turn_off_pins()  # Switch off all pwm_objects
    LED.clean_up_gpio()  # Clean up every pin on board

    print("\nCleaned all LED-Pins.")
    sleep(3)
    print("\nShutting down now.")
    sleep(1)
    os.system("sudo shutdown -h now")  # Command to shut down raspberry pi safely


# Executing the whole color show process
def execute_task():
    Button_instance = Button()
    RGB_instance = RGB()

    while True:
        if Button_instance.tap_button():
            sleep(1)
            while True:
                for color in RGB_instance.colors:  # Going through all colors we stored in our dictionary
                    if Button_instance.tap_button():  # Do this on tap
                        RGB_instance.turn_off_pins()  # Switch off all pwm_objects
                        print("Stopped the rgb flow.\n")
                        sleep(1)
                        execute_task()  # Put this here so the program's listening for the buttons again
                    else:
                        RGB_instance.set_color(color)  # Change the color of the RGB LED
                        sleep(0.5)
        if Button_instance.hold_button():  # Execute this code, if the button is being held down for more then 5 seconds
            shutdown_pi(RGB_instance)
        else:
            continue


if __name__ == "__main__":
    execute_task()
