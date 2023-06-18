"""A class or function to parse the config file and return the values as a dictionary.

The config file itself can be any of the following formats:

- ryo: means 'roll your own' and is a simple text file with key-value pairs separated by an equals sign. For example:
```
location = "Moondalup City Square Parking"
number_of_spaces = 192
```
**you** read the file and parse it into a dictionary.
- json: a json file with key-value pairs. For example:
```json
{location: "Moondalup City Square Parking", number_of_spaces: 192}
```
json is built in to python, so you can use the json module to parse it into a dictionary.
- toml: a toml file with key-value pairs. For example:
```toml
[location]
name = "Moondalup City Square Parking"
spaces = 192
```
toml is part of the standard library in python 3.11, otherwise you need to install tomli to parse it into a dictionary.
```bash
python -m pip install tomli
```
see [realpython.com](https://realpython.com/python-toml/) for more info.

Finally, you can use `yaml` if you prefer.



"""


import json

import json

def parse_json_file(file_path: str) -> dict:
    with open(file_path) as json_file:
        data = json.load(json_file)

    # Create an empty dictionary
    parsed_data = {}

    # Add the values to the dictionary
    parsed_data['location'] = data['location']
    parsed_data['total_spaces'] = data['total_spaces']
    parsed_data['total_cars'] = data['total_cars']
    parsed_data['broker'] = data['broker']
    parsed_data['sensor'] = data['sensor']
    parsed_data['port'] = data['port']
    parsed_data['name'] = data['name']
    parsed_data['topic-root'] = data['topic-root']
    parsed_data['topic-qualifier'] = data['topic-qualifier']
    parsed_data['carpark_location'] = data['carpark_location']

    return parsed_data
