# try:
#     file = open("order.txt", "r")  # Read mode "r" doesn't need to be there, its default.
#
# except FileNotFoundError as errmsg:
#     print("There has been an error opening your file")  # Stuff like this replaces the large errors in the console
#     print(errmsg)
#     # raise # # Brings back the 'red errors in the console'

def open_and_print_file(file="order.txt"):
    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip("\n"))

        # file_line_list = opened_file.readlines() # # Don't need to do all this if we use with keyword
        # print(file_line_list)
        #
        # for line in file_line_list:
        #     print(line.rstrip('\n'))
        #
        # opened_file.close()

    except FileNotFoundError as errmsg:
        print("There has been an error opening your file")  # Stuff like this replaces the large errors in the console
        print(errmsg)
    finally:
        print("Execution complete")


# open_and_print_file("order.txt")

def write_to_file(order_item, file="order.txt"):
    try:
        with open(file, "a") as opened_file:  # a means append, w would delete everything and rewrite with only new item
            opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("e.g file cant be found")
    except FileExistsError:
        print("file already exists")


# write_to_file("lasagna")
# open_and_print_file()

# how to add multiple items
# change function so that accepts multiple items at once and append each on their own separate line


def write_to_file2(order_items, file="order.txt"):
    try:
        with open(file, "a") as task_file:
            for item in order_items:
                task_file.write('\n' + item)
    except FileNotFoundError:
        print("e.g file cant be found")
    except FileExistsError:
        print("file already exists")


# write_to_file2(["pasta", "nuts"])
# open_and_print_file()

# # This is the way that uses the least lines [opened_file.write(item + '\n') for item in list]


def write_to_file3(order_items, file="order.txt"):
    try:
        with open(file, "a") as opened_file:
            [opened_file.write(item + '\n') for item in order_items]
    except FileNotFoundError:
        print("e.g file cant be found")
    except FileExistsError:
        print("file already exists")


write_to_file3(["apples", "pears", "oranges"])
