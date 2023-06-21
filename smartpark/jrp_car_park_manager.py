import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage
import mqtt_device
from datetime import datetime
import random
import time


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        carpark_name = config['carpark_location']
        self.total_spaces = config['total_spaces']
        self.total_cars = config['total_cars']
        print(f"Carpark at {carpark_name} is ready")
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.loop_active = True
        self.run_loop()

    def run_loop(self):
        while self.loop_active == True:
            self.client.loop()
            time.sleep(0.1)

    def exit_loop(self):
        self.loop_active = False


    @property
    def available_spaces(self):
        if self.total_cars < 0:
            self.total_cars = 0
        available = self.total_spaces - self.total_cars
        if available > 192:
            available = 192
        return available if available > 0 else 0

    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        temperature = int(random.gauss(25, 1))
        print(f"TIME: {readable_time}, " +
              f"SPACES: {self.available_spaces}, " +
              f"TEMPC: {temperature}")
        message = (f"TIME: {readable_time}, " +
              f"SPACES: {self.available_spaces}, " +
              f"TEMPC: {temperature}")
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    from config_parser import parse_json_file
    config = parse_json_file("config.json")
    print("Carpark initialized")
    car_park = CarPark(config)
