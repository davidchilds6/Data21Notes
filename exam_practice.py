"""1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
 between 1500 and 2700 (both included)"""
# for number in range(1500, 2701):
#     if number % 7 == 0 and number % 5 == 0:
#         print(number)

"""
2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""


# def c2f(temp_in_celsius):
#     f = (temp_in_celsius * 9 / 5) + 32
#     return f
#
#
# def f2c(temp_in_fahrenheit):
#     c = (temp_in_fahrenheit - 32) * 5 / 9
#     return c
#
#
# print(c2f(60))
# print(f2c(45))

"""3. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears 
again until the guess is correct, on successful guess, 
user will get a "Well guessed!" message, and the program will exit."""

# import random
# answer = random.randint(1, 9)
# while True:
#     guess = int(input("Pick a number between 1 and 9 inclusive"))
#     if guess == answer:
#         print("Well guessed")
#         break
#     else:
#         print("Unlucky, try again")

"""4. Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

# for i in range(5):
#     for j in range(i):
#         print ('*', end="")
#     print('')
# for i in range(5, 0, -1):
#     for j in range(i):
#         print ('*', end="")
#     print('')

"""5. Write a Python program that accepts a word from the user and reverse it."""


# def reverse_word(user_input):
#     return user_input[::-1]
#
#
# reversed_word = reverse_word(input("Type a word you would like reversed"))
# print(reversed_word)


"""6. Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_count = 0
# odd_count = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Number of even numbers: {even_count}")
# print(f"Number of odd numbers: {odd_count}")

"""7. Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]"""

# data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
#
# for i in data_list:
#     print(i, type(i))

"""8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement."""
# for x in range(6):
#     if x == 3 or x == 6:
#         continue
#     print(x, end=' ')

"""9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34"""

numbers
