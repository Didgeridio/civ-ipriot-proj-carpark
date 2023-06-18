""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""

import mqtt_device
import random


class Sensor(mqtt_device.MqttDevice):
    def __init__(self, config):
        super().__init__(config)
        sensor_name = config['sensor']
        print(f"Sensor {sensor_name} is ready")

    def temperature(self):
        """Returns the current temperature"""
        return random.randint(10, 35)

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection("entered")
            else:
                self.on_detection("exited")


if __name__ == '__main__':
    from config_parser import parse_json_file

    config2 = parse_json_file("config2.json")

    sensor1 = Sensor(config2)
    print(sensor1)

    print("Sensor initialized")
    sensor1.start_sensing()

