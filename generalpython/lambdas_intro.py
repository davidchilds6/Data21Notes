# # Demonstration of a lambda function.
# def addition(num1, num2):  # A func we want to represent as a lambda func
#     return num1 + num2
#
#
# add = lambda num1, num2: num1 + num2  # Lambda func

# # Print both for comparison
# print(addition(2, 3))
# print(add(2, 3))

# # Maps take in a
# savings = [234, 555, 674, 78]
#
#
# def bonus():
#     new = []
#     for i in savings:
#         i = 1.1*i
#         new = new.append(i)
#         print(new)
#
#
# print(bonus(savings))

# # # lambda version
# savings = [234, 555, 674, 78]
#
# print(savings)
# bonus_lambda = list(map(lambda x: x * 1.1, savings))
#
#
# print(bonus_lambda)

"""Practice from https://www.w3resource.com/python-exercises/lambda/index.php"""

"""Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and print the result."""

# r = lambda a : a + 15  # Basic ones
# print(r(10))

# r = lambda x, y : x * y
# print(r(12, 4))

# numbers = [234, 555, 674, 78]  # With lists
# plus_fifteen = list(map(lambda x: x + 15, numbers))
# print(plus_fifteen)

# more_numbers = [(15, 8), (6, 7)]
# multiples = list(map(lambda data: data[0] * data[1], more_numbers))
# print(multiples)

"""Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number"""
# So this wants a function with a lambda inside it? Looked at solution

#
# def arg_times_number(n):
#     return lambda x: x * n
#
#
# result = arg_times_number(2)
# print("Double the number of 15 =", result(15))

"""Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:"""
# li = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# # # Sorting the List of Tuples:
# # # [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# #
# li.sort(key=lambda entry: entry[1], reverse=False)  # Reverse = True will sort in desc order
# print(li)


"""Write a Python program to sort a list of dictionaries using Lambda. 
Original list of dictionaries :"""
# phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# phones.sort(key=lambda entry: entry['color'], reverse=False)
# print(phones)

"""Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_filter = list(filter(lambda x: x % 2 == 0, integers))  # map returns bools, filter returns og
# print(even_filter)
# odd_filter = list(filter(lambda x: x % 2 != 0, integers))
# print(odd_filter)

"""Write a Python program to square and cube every number in a given list of integers using Lambda."""
og = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = list(map(lambda x: x**2, og))
cube = list(map(lambda x: x**3, og))
print(square, cube)
