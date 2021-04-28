import csv
# Define a function that extracts from a csv file


def extract_csv(csv_name):
    try:
        with open(csv_name) as csv_file:
            readfile = csv.reader(csv_file, delimiter=",")
            csv_list = list(readfile)
        return csv_list
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("The file does not exist")
    finally:
        print("File extracted")


def transform_csv(csv_list):
    filtered_csv = []
    try:
        for entry in csv_list:
            columns = entry[1], entry[2], entry[4]  # Select columns to filter
            filtered_csv.append(columns)
        return filtered_csv
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("The file does not exist")
    finally:
        print("File transformed")


def load_csv(old_csv, new_csv):
    transformed_file = transform_csv(extract_csv(old_csv))
    try:
        with open(new_csv, "w") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(transformed_file)
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("The file does not exist")
    finally:
        print("Transformed file loaded")


load_csv("user_details.csv", new_csv="hope_this_works.csv")