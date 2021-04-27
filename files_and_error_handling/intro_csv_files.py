import csv

with open("user_details.csv") as ud:
    readfile = csv.reader(ud, delimiter=",")

# # for displaying rows in csv
    # iterable_csv = iter(readfile)
    # next(iterable_csv)
    # for row in iterable_csv:  # excludes headers
    #     print(row)


# def open_csv_file(): # # not sure whats going on here
#     with open(csv_name) as csvfile:
#         csv_name = csv.reader(csvfile, delimiter=",")


def transform_user_details(csv_name):
    filtered_csv = []
    with open(csv_name) as csvfile:
        csv_name = csv.reader(csvfile, delimiter=",")
        iterable_csv = iter(csv_name)
        next(iterable_csv) # # skips first entry, in this case the headers
        for entry in iterable_csv:
            filtered_csv.append([entry[1], entry[2], entry[4]])  # Select columns to filter
        return filtered_csv


print(transform_user_details("user_details.csv"))


def create_csv_file(old_user_details="user_details.csv", new_file_name="new_details.csv"):
    new_user_details = transform_user_details(old_user_details)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)


create_csv_file()
