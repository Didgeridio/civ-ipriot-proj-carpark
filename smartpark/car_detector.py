import random
import threading
import time
import tkinter as tk
import mqtt_device
from typing import Iterable
from windowed_display import WindowedDisplay

class CarDetector(mqtt_device.MqttDevice):
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car. This is a skeleton only."""

    def __init__(self, config):
        super().__init__(config)
        sensor_name = config['sensor']
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.root.mainloop()

    def incoming_car(self):
        message = "enter"
        self.client.publish('sensor', message)
        print("Car goes in")

    def outgoing_car(self):
        message = "exit"
        self.client.publish('sensor', message)
        print("Car goes out")

if __name__ == '__main__':
    from config_parser import parse_json_file

    config2 = parse_json_file("config2.json")
    CarDetector(config2)