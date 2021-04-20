# Using if
age = 19

# if true:
#     print("this statement will print, if false, the console will do nothing")

if age > 18:
    print("you are older than 18")

# Can use elif and else to consider more than one condition and output a different statement for each
# If you use a bunch of ifs then it will output all conditions that are true
if age > 18:
    print("you are older than 18")
if age > 50:
    print("you are older than 50")
else:
    print("you are not older than 18")

# Elif will only return the first condition that is satisfied. ie age = 51 will return "you are older than 18" only
if age > 18:
    print("you are older than 18")
elif age > 50:
    print("you are older than 50")
else:
    print("you are not older than 18")

