from config_parser import parse_json_file
from mqtt_device import MqttDevice
class ParkingLot:
    def __init__(self):
        self.location: None #str
        self.total_spaces: None #int
        self.available_spaces: None #int
        self.mqtt_client: None #MQTTClient

    def create_mqtt_client(self):
        #read the config file
        file_path = "config.json"
        config = parse_json_file(file_path)
        #instantiate an mqtt device
        mqtt_device = MqttDevice(config)
        #assign device to the mqtt client instance variable
        self.mqtt_client = mqtt_device
        #get the location's details
        self.location = config['carpark_location']
        self.total_spaces = config['total_spaces']
    def enter(self):
        pass

    def exit(self):
        pass

    def publish_update(self):
        pass


