from RPi import GPIO


class LED_Device:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)  # Adress pins with their numbers
        GPIO.setup(pin, GPIO.OUT)  # Set pins as output

        self.pwm_object = GPIO.PWM(pin, 100)  # Initialize object with 100hz
        self.pwm_object.start(0)  # Start the pwm_object

        self.__intensity = 0  # Private object to calibrate LEDs

        self.pin = pin  # Private object

        print("\nLED-Device setup is complete.")

    # Set the intensity to a certain value
    def set_intensity(self, value):
        if value in range(0, 256):
            self.__intensity = value
            self.pwm_object.ChangeDutyCycle(self.__intensity / 255 * 100)
        else:
            self.__intensity = 0
            print("\nWarning: The intensity value is not between 0 and 255.")
            print("Please enter a number between 0 and 255.\n")

    # Function to turn off the pwm_object
    def switch_off(self):
        self.pwm_object.stop()
        GPIO.output(self.pin, False)

    # Change all outputs to inputs
    def clean_up_GPIO(self):
        GPIO.cleanup()
        print("\nCleaned all pins.\n")
