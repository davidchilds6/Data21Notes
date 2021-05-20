import pymongo
from pprint import pprint

client = pymongo.MongoClient()
# print(client)
db = client["starwars"]
print(db)

# examples of differences in syntax db.characters.insert_one(), db.characters.insert_many()

# luke = db.characters.find({"name": "Luke Skywalker"})
# print(luke)
# luke = db.characters.find_one({"name": "Luke Skywalker"})
# pprint(luke) # auto arranges keys in alphabetical order
# print(type(luke))
# pprint(luke, sort_dicts=False)


# luke2 = db.characters.find({"name": "Luke Skywalker"})
# for entry in luke2:
#     print(entry["name"])

# blue = db.characters.find({"eye_color": "blue"})
# blue_names = map(lambda x: x["name"], blue)
# pprint(list(blue_names))


# Print names of all the droids in the collection
# droids = db.characters.find({"species.name": "Droid"})
# droid_names = map(lambda x: x["name"], droids)
# pprint(list(droid_names))

# Find the height of dart vader, only return results for the name the height.
# vader = db.characters.find_one({"name": "Darth Vader"})
# print(vader["name"], vader["height"])
#
# print(
#     db.characters.find_one({"name": "Darth Vader"},
#                            {"name": 1, "height":1, "_id": 0})
# )
#
# print(
#     db.characters.find_one({"name": {"$regex": "Vader"}},
#                            {"name": 1, "height": 1, "_id": 0})
# )

# Find all characters with yellow eyes
# only return names
#
# pprint(list(db.characters.find({"eye_color": "yellow"}, {"name": 1, "_id": 0})))

# Find male character. limit to first 3
# pprint(
#     list(db.characters.find(
#         {"gender": "male"},
#         {"name": 1, "_id": 0}
#     ).limit(3)
#          )
# )
#
# male_char = db.characters.find(
#         {"gender": "male"},
#         {"name": 1, "_id": 0}
#     ).limit(3)
#
# for char in male_char:
#     print(char)
#
# male_char = male_char = db.characters.find(
#         {"gender": "male"},
#         {"name": 1, "_id": 0}
#     ).limit(3)
#
# for char in male_char:
#     print(char)
#
# for char in male_char[0:3]:
#     print(char)

# Find names of all the humans whose home world is Alderaan
# human_alderaan = db.characters.find(
#         {"species.name": "Human", "homeworld.name": "Alderaan"},
#         {"name": 1, "_id": 0}
#     )
#
# for human in human_alderaan:
#     print(human)

# What is the average height of female characters import numpy as it has nan object
# avg_h_fem = db.chardemo.aggregate(
#     [
#         {"$match": {"gender": "female", "height": {"$ne": float("nan")}}},
#         {"$group": {"_id": "$gender", "average height": {"$avg": "$height"}}}
#     ]
# )
# print(avg_h_fem.next())

# Which character is the tallest? find max height first then make sure that anyone with the same is also being displayed
#
# max_height = db.chardemo.aggregate(
#     [
#         {"$match": {"height": {"$ne": float("nan")}}},
#         {"$group": {"_id": "None", "max_height": {"$max": "$height"}}}
#     ]
# ).next()["max_height"]
#
# for tallest in db.chardemo.find({"height": max_height}):
#     print(tallest["name"], tallest["height"])
