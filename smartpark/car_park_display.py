import random
import threading
import time
import mqtt_device
import tkinter as tk
from typing import Iterable
from windowed_display import WindowedDisplay
import paho.mqtt.client as paho

class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowedDisplay('Moondalup', CarParkDisplay.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        key_value_pairs = payload.split(", ")
        parsed_payload = {}
        for pair in key_value_pairs:
            key, value = pair.split(": ")
            parsed_payload[key.strip()] = value.strip()

        self.time_value = parsed_payload['TIME']
        self.spaces = parsed_payload['SPACES']
        self.temp = parsed_payload['TEMPC']

        field_values = {
            'Available bays': self.spaces,
            'Temperature': f'{self.temp}℃',
            'At': self.time_value
        }

        self.window.update(field_values)

    def check_updates(self):
        self.spaces = 100  # Initial value
        self.temp = int(random.gauss(25, 1)) # Initial value
        self.time_value = time.strftime("%H:%M:%S")
        while True:
            # Not sure if I should be updating the temp often like the time or just when a car enters
            field_values = dict(zip(CarParkDisplay.fields, [
                f'{self.spaces}',
                f'{self.temp}℃',
                time.strftime("%H:%M:%S")]))

            self.window.update(field_values)

            # Check if there are any new messages in the 'display' topic
            self.client = paho.Client("parking_big_display")
            self.client.connect("127.0.0.1", 1883)
            self.client.on_message = self.on_message
            self.client.loop_start()
            self.client.subscribe('display')

            time.sleep(0.5)
            self.client.loop_stop()

if __name__ == '__main__':
    # TODO: Run each of these classes in a separate terminal. You should see the CarParkDisplay update when you click the buttons in the CarDetector.
    # These classes are not designed to be used in the same module - they are both blocking. If you uncomment one, comment-out the other.


    CarParkDisplay()