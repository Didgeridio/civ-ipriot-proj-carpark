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
        payload = msg.payload.decode()
        key_value_pairs = payload.split(", ")
        parsed_payload = {}
        for pair in key_value_pairs:
            key, value = pair.split(": ")
            parsed_payload[key.strip()] = value.strip()
        time_value = parsed_payload['TIME']
        spaces = parsed_payload['SPACES']
        temp = parsed_payload['TEMPC']
        print(f"The time is {time_value}")
        print(f"There are {spaces} spaces available")
        print(f"The current temperature is {temp} ℃")
if __name__ == '__main__':
    from config_parser import parse_json_file
    config = parse_json_file("config3.json")
    display = Display(config)

