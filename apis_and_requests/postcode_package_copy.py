import requests
import json
from pprint import pprint


class PostCode:
    def __init__(self, post_code, columns):
        self.postcode = post_code
        self.column_list = columns

    def retrieve_all_details(self):
        postcode_details = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}")
        return dict(postcode_details.json())["result"].items()

    def retrieve_selected_details(self):
        postcode_details_dictionary = self.retrieve_all_details()
        return [(key, value) for (key, value) in postcode_details_dictionary if key in self.column_list]


def get_columns():  # Call this function to just get a list of potential fields
    postcode_details = requests.get(f"https://api.postcodes.io/random/postcodes")
    postcode_details_dictionary = dict(postcode_details.json())["result"].items()
    key_list = [key for (key, value) in postcode_details_dictionary]
    return key_list


my_code = PostCode("dt94ls", ["postcode", "parliamentary_constituency", "admin_county", "longitude", "latitude"])
pprint(my_code.retrieve_all_details(), sort_dicts=False)
pprint(my_code.retrieve_selected_details(), sort_dicts=False)

# pprint(get_columns(), sort_dicts=False)
