import mqtt_device
import time
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)
    def on_message(self, client, userdata, msg):
       data = msg.payload.decode()
       self.display(*data.split(','))
       # TODO: Parse the message and extract free spaces,\
       #  temperature, time
if __name__ == '__main__':
    from config_parser import parse_json_file
    config = parse_json_file("config3.json")
    display = Display(config)

