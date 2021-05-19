# # List
# shopping_list = ["eggs", "milk", "bread"]
# print(shopping_list)
# print(type(shopping_list))
#
# # Same rules as slices
# print(shopping_list[0])
# # Up to but not including bread
# print(shopping_list[0:2])
#
# # Changing things within a list - They are mutable
# shopping_list[0] = "chocolate"
#
# # Lists can contain multiple data types
# shopping_list = ["eggs", "milk", "bread", 37, 41.78]
#
# # append and pop can add and remove data to lists
# # Tuples
# shopping_tup = ["eggs", "milk", "bread"]
# print(shopping_tup)
# # Printed lists output surrounded by square brackets
# # Printed tuples output surrounded by curly brackets
# # Tuples are immutable, does not support item assignment
#
# # Dictionaries - Key/value pairs

# student_1 = {
#     "name": "Dave",
#     "stream": "Data",
#     "Address": ["Newhay", "Dorset", "DT9 4LS"]
# }
# # Print whole dictionary
# print(student_1)
# # Print entry from dictionary
# print(student_1["stream"])
# # Print entry from list within a table
# print(student_1["Address"][2])
#
# # Update value in dictionary
# student_1["name"] = "Emily"
# print(student_1)
#
# # Remove entry in dictionary
# student_1["Address"].remove("DT9 4LS")
# print(student_1)

# Sets like a dictionary but does not have key value pairs
# Sets can only take unique values
car_parts = {"wheels", "doors", "windows"}
print(car_parts)
print(type(car_parts))

# Add value to set
car_parts.add("headlights")
print(car_parts)

# Remove value from set
car_parts.discard("doors")
print(car_parts)
