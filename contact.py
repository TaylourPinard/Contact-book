'''
    this is a program that stores information in a 
    "contact book" in the form of a csv file and the
    phone number can be retrieved by either first or last
    name and you can optionally specify a different field
    such as "address" or "last" to be retrieved instead
'''

from sys import argv
import csv

# requires a csv file "contacts.csv" with headers
# first,last,address,phone
# in order to run properly
def main():
    if argv[1] == "get":
        if len(argv) > 3:
            read(argv[2], argv[3])
        else: read(argv[2])
    elif argv[1] == "post":
        write(argv[2], argv[3], argv[4], argv[5])

# specify a different field in the 4th argument (argv[5])
# to retrieve a specific result field other than phone number
def read(name, field="phone"):
    with open("contacts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["first"] == name.title() or row["last"] == name.title():
                print(row[field])

# all fields are required
# address must be surrounded in quotes if the address
# includes any commas
def write(first, last, address, phone):
   with open("contacts.csv", "a") as file:
        field_names = ["first", "last", "address", "phone"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow({"first": first.title(), "last": last.title(), "address": address, "phone": phone})

if __name__ == "__main__":
    main()