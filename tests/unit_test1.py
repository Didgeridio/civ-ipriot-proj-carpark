import unittest
from config_parser import parse_json_file
import json


class TestConfigParsing(unittest.TestCase):
    #test that a copy of the config file returns the same for carpark_location and initial available_spaces as expected.
    def test_parse_config_has_correct_location_and_spaces(self):
        config = parse_json_file("test_config.json")
        self.assertEqual(config['carpark_location'], "Moondalup City Square Parking")
        self.assertEqual(config['total_spaces'], 192)