# Initialise prompts for while loops.
name_prompt = True
age_prompt = True

# variables - lists of movies for each age category. Placed them near the top to not break up the code below.
u_films = ["toddler movie 1", "toddler movie 2", "toddler movie 3"]
pg_films = ["kids movie 1"]
twelve_films = ["teenager movie 1", "teenager movie 2", "teenager movie 3", "teenager movie 4"]
fifteen_films = ["young adult movie 1", "young adult movie 2"]
eighteen_films = ["adult movie 1", "adult movie 2", "adult movie 3"]

# While loop to make sure that input is valid for the name. Capitalize will convert 'dave' into 'Dave'
while name_prompt is True:
    name = input("Please enter your name?    ").capitalize()
    if name.isalpha():
        name_prompt = False
    else:
        print("Please use only letters of the alphabet.")

# While loop to confirm valid input for age
while age_prompt is True:
    age = input(f"How old are you {name}?   ")
    if age.isdigit():
        age_prompt = False
    else:
        print(f"{name}, please insert your age as a positive whole number.")

# # This was my initial code but didn't like the way the console displayed the results.
# # Multiple if statements to determine which movies you are eligible for.
# if 0 < int(age) <= 3:
#     print(f"You can only watch: {u_films}.")
# if 3 < int(age) <= 11:
#     print(f"You can watch:", {u_films, pg_films})
# if 11 < int(age) <= 15:
#     print(f"You can watch {u_films}, {pg_films}, {twelve_films}.")
# if 16 < int(age) <= 18:
#     print(f"You can watch {u_films}, {pg_films}, {twelve_films}, {fifteen_films}.")
# if int(age) >= 18:
#     print(f"You can watch {u_films}, {pg_films}, {twelve_films}, {fifteen_films}, {eighteen_films}.")

# This is my attempt at cleaning up the lists when they print
# https://stackoverflow.com/questions/4440516/in-python-is-there-an-elegant-way-to-print-a-list-in-a-custom-format-without-ex
if 0 < int(age) <= 3:
    print(f"You can only watch:", *u_films, sep='\n- ')
if 3 < int(age) <= 11:
    print(f"You can watch:", *(*u_films, *pg_films), sep='\n- ')
if 11 < int(age) <= 15:
    print(f"You can watch:", *(*u_films, *pg_films, *twelve_films), sep='\n- ')
if 16 < int(age) <= 18:
    print(f"You can watch:", *(*u_films, *pg_films, *twelve_films, *fifteen_films), sep='\n- ')
if int(age) >= 18:
    print(f"You can watch:", *(*u_films, *pg_films, *twelve_films, *fifteen_films, *eighteen_films), sep='\n- ')
