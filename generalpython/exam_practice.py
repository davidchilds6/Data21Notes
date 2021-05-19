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

# x = 0
# while x + 1 < 50:
#     print(x+1)
#     x, (x + 1) = x + 1, x + x + 1
#

# x, y = 0, 1
# while y < 50:
#     print(y)
#     x, y = y, x + y

"""CLASSES PRACTICE"""

"""https://campus.datacamp.com/courses/object-oriented-programming-in-python/oop-fundamentals?ex=5"""

"""Write the code for a Python function expand(x) that takes a list of strings,
concatenates them, and returns the resulting string repeated three times."""


# def expand(x):  # not very good solution, doesn't actually return a string
#     for i in range(3):
#         for j in x:
#             print(j, end="")
#
#
# def expand2(x):
#     return ''.join(x) * 3


"""Question from the exam to help ab 
Write the body of the function is_on_even_index(list, value).
The function should return True if value is contained in list at an
even index, False otherwise.
To test run this:
t = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(is_on_even_position(t, 6))  # it should return False
print(is_on_even_position(t, 3))  # it should return True
t = [1, 1]
print(is_on_even_position(t, 1))  # it should return True"""


# def is_on_even_index(list, value):
#     if value in list[0::2]:
#         return True
#     else:
#         return False
#
#
# t = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(is_on_even_index(t, 6))
# print(is_on_even_index(t, 3))
# t = [1, 1]
# print(is_on_even_index(t, 1))
#
#
# def is_on_even_index2(list, value):
#     index = list.index(value)
#     if index % 2 == 0:
#         return True
#     else:
#         return False
#
#
# t = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(is_on_even_index2(t, 6))
# print(is_on_even_index2(t, 3))
# t = [1, 1]
# print(is_on_even_index2(t, 1))

"""In this task, you will find a function called odd_even_counter that takes an argument of number.
You will need to implement the below details to solve the problem:
Implement a list - Consider that the list will need to be set i.e. not blank []:	
    The list at index 0 will relate to even numbers and at a list index 1 odd numbers
    You will need to iterate on any given number until it reaches 0
    Within the loop, you will need to evaluate whether the number is even or odd and add it to the appropriate list 
    index ensuring that it does not overwrite the number but adds to it
Remember to manage a counter in your loop
You will need to only return the array
An example:
If you run the test, which is being given the number 5 -> oddEvenCounter(5) it should print 6 and 9
This is because the array returns [6,9] because of the even totals 2+4 = 6 and the odd totals 1+3+5 = 9"""


# def odd_even_counter(number):
#     number_list = ([num for num in range(number + 1) if num % 2 == 0],
#                    [num for num in range(number + 1) if num % 2 != 0])
#     return sum(number_list[0]), sum(number_list[1])
#
#
# print(odd_even_counter(5))


# def odd_even_counter2(number):
#     even_list = [num for num in range(number + 1) if num % 2 == 0]
#     odd_list = [num for num in range(number + 1) if num % 2 != 0]
#     return even_list, odd_list
#
#
# print(odd_even_counter2(5))


# def odd_even_counter3(number):
#     array = [[0], [0]]
#     for nums in range(number):
#         if nums % 2 == 0:
#             array[0].append(nums)
#         elif nums % 2 != 0:
#             array[1].append(nums)
#         else:
#             print("problem")
#     return sum(array[0]), sum(array[1])
#
#
# print(odd_even_counter3(5))

