# for number in num_list:
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# to make fizzbuzz into a function with no print statements, initialise an empty list and append each result to it
# as the range is iterated through
def fizzbuzz(lower, higher):
    result = []
    for number in range(lower, higher):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return '\n'.join(result)


# print(fizzbuzz(1, 31))
