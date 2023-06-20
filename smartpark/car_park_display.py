import random
import threading
import time
from windowed_display import WindowedDisplay
import paho.mqtt.client as paho


class CarParkDisplay:
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowedDisplay('Moondalup', CarParkDisplay.fields)
        updater = threading.Thread(target=self.check_updates)
        self.time_value = ""
        self.spaces = 0
        self.temp = 0
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
        self.spaces = 100
        self.temp = int(random.gauss(25, 1))
        self.time_value = time.strftime("%H:%M")
        while True:
            # Not sure if I should be updating the temp often like the time or just when a car enters
            field_values = dict(zip(CarParkDisplay.fields, [
                f'{self.spaces}',
                f'{self.temp}℃',
                time.strftime("%H:%M")]))

            self.window.update(field_values)

            # Check if there are any new messages in the 'display' topic
            self.client = paho.Client("parking_big_display")
            self.client.connect("127.0.0.1", 1883)
            self.client.on_message = self.on_message
            self.client.loop_start()
            self.client.subscribe('display')

            time.sleep(5)
            self.client.loop_stop()


if __name__ == '__main__':
    CarParkDisplay()
