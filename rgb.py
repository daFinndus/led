from led import LED


class RGB:
    colors = {
        "red": [0, 255, 255],
        "green": [255, 0, 255],
        "blue": [255, 255, 0],
    }

    channels = {
        "red_channel": 36,
        "green_channel": 38,
        "blue_channel": 40
    }

    def __init__(self):
        self.actual_color = None

        self.LED_red = LED(self.channels["red_channel"])
        self.LED_green = LED(self.channels["green_channel"])
        self.LED_blue = LED(self.channels["blue_channel"])

    def set_color(self, color_light):
        if color_light.lower() in self.colors.keys():
            self.LED_red.set_intensity(self.colors.get(color_light)[0])
            self.LED_green.set_intensity(self.colors.get(color_light)[1])
            self.LED_blue.set_intensity(self.colors.get(color_light)[2])
            self.actual_color = color_light
            print(f"\nSet color to {color_light}.")
        else:
            print("\nColor not registered.")

    def clean_up_pins(self):
        self.LED_red.switch_off()
        self.LED_green.switch_off()
        self.LED_blue.switch_off()
        print("\nCleaned up all used pins.\n")
