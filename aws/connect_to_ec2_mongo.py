import pymongo
from pprint import pprint

client = pymongo.MongoClient("18.197.107.75", 27017)

db = client["demo"]

# dave = db.hello.find_one({"f_name": "Dave"})
# pprint(dave, sort_dicts=False)


all_docs = db.hello.find({})
all_docs = map(lambda x: x, all_docs)
pprint(list(all_docs), sort_dicts=False)
