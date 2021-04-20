# list_data = [1, 2, 3, 4, 6, 8, 5]
# embedded_list = [[1, 2, 3], [2, 3, 4]]
#
# for data in list_data:
#     print(data)
#
# # iterating through a list in a list
# for data in embedded_list:
#     print(data)
#     for number in data:
#         print(number)

# # A while loop
# # to stop a while statement in an infinite loop
#
# x = 0
# while x < 10:
#     print("this is true")
#     x += 1

# # break point
# x = 0
# while x < 10:
#     print("this is true")
#     print(x)
#     if x == 4:
#         break
#     x += 1

# Exercise use a while loop to ensure that a user inputs the correct value for an age
user_prompt = True

while user_prompt is True:
    age = input("what is you age?")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer as a digit")