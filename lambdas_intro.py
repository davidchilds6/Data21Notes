# # Demonstration of a lambda function.
def addition(num1, num2):  # A func we want to represent as a lambda func
    return num1 + num2


add = lambda num1, num2: num1 + num2  # Lambda func

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
savings = [234, 555, 674, 78]

print(savings)
bonus_lambda = list(map(lambda x: x * 1.1, savings))




print(bonus_lambda)
