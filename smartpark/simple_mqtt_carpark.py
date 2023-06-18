import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage
import mqtt_device
from datetime import datetime


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        carpark_name = config['carpark_location']
        self.total_spaces = config['total_spaces']
        self.total_cars = config['total_cars']
        self.temperature = None
        print(f"Carpark at {carpark_name} is ready")
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0

    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(f"TIME: {readable_time}, " +
              f"SPACES: {self.available_spaces}, " +
              f"TEMPC: 42") # TODO: Temperature
        message = (f"TIME: {readable_time}, " +
              f"SPACES: {self.available_spaces}, " +
              f"TEMPC: 42")
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
