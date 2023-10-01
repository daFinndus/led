from RPi import GPIO
from time import time


class Button:
    def __init__(self):
        GPIO.setwarnings(False)  # Mute all these stupid warnings, don't need them anyway
        GPIO.setmode(GPIO.BOARD)

        # Create dictionary storaging button pins
        self.buttons = {
            "Button 1": 13,
            "Button 2": 11
        }

        # Change all button pins to inputs
        for pin in self.buttons.values():
            GPIO.setup(pin, GPIO.IN)
            print(f"Setup for pin {pin} is complete.")

        print(f"Setup for the buttons are completed.\n")

    # Function to check if button 1 is being pressed
    def tap_button(self):
        if GPIO.input(self.buttons['Button 1']) == GPIO.HIGH:
            print(f"Pin: {self.buttons['Button 1']} is pressed.")
            return True

    # Function to check if button 2 is being pressed for 5 seconds
    def hold_button(self):
        if GPIO.input(self.buttons['Button 2']) == GPIO.HIGH:
            tap_time = time()

            while GPIO.input(self.buttons['Button 2']) == GPIO.HIGH:
                if time() - tap_time >= 5:
                    return True
