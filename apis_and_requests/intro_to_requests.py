import requests
import json
from pprint import pprint

# # simple request
# post_code_req = requests.get("https://api.postcodes.io/postcodes/dt94ls")
#
# print(post_code_req)
# print(post_code_req.headers)
# print(post_code_req.content)
# print(type(post_code_req.content))
# print(type(post_code_req.json))
# print(post_code_req.json())   # Returns it in a nice json string

# # Multiple postcode look up

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

postcode_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

pprint(postcode_multi_req.json())

