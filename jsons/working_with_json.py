import json

# pet_data = {"name": "Bob", "food": "carrots"}
# print(pet_data)
#
# pet_data_json_str = json.dumps(pet_data)
# print(pet_data_json_str)      # Cant use standard dictionary way of selected elements, treats entire thing as a string

# print(type(pet_data))       # Dict
# print(type(pet_data_json_str))      # Str


# with open("new_json_file.json", "w") as jsonfile:   # make a json file from a dictionary
#     json.dump(pet_data, jsonfile)

# with open("new_json_file.json") as json_file:
#     pet = json.load(json_file)       # Take in json file and open it up
#     print(type(pet))
#     print(pet)
#     print(pet["name"])      # makes it into a dictionary


class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        self.gbp = self.rates["GBP"]

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rates_reader = RatesParser("exchange_rates.json")
print(rates_reader.base, rates_reader.rates)
