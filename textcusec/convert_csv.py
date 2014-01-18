# Just a tiny one time script for importing the CUSEC contacts into this app.

import csv

from apps.broadtext.models import Contact


with open("./cusec.csv", "rb") as file:
    reader = csv.reader(file, delimiter=",", quotechar="|")
    next(reader, None) # Skip the header row
    for row in reader:
        timestamp, name, number, emergency_name, emergency_number, relation = row
        name = name.replace("\"", "")
        number = number.replace("\"", "")
        number = number.replace(" ", "")
        number = number.replace("-", "")
        if number[0] != "1":
            number = "1" + number
        number = "+" + number
        print(name + ", " + number)

        Contact(name=name, number=number).save()
