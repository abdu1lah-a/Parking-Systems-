import sys
import csv
from tabulate import tabulate

def main():
    choice = input("Choose one of the following options:\n1) Park your car\n2) Remove car from the parking lot\n3) Total cars parked in the lot today\nEnter your choice: ")
    if choice == "1":
        print("Our prices --> Every hour costs $2.50")
        plate = input("Enter you license plate number: ")
        park_car(plate)
    elif choice == "2":
        remove_car()
    elif choice == "3":
        total_car_parked()
    else:
        sys.exit("Not a valid choice")

def park_car(plate, p_name = None, p_hour = None):
    with open("parking.csv", "a+") as file:
        file.seek(0)
        reader = csv.reader(file)
        for row in reader:
            if row[0] == plate:
                sys.exit("This entry already exits")
        if p_name != None:
            name = p_name
        else:
            name = input("Enter your name: ")
        if plate == "" or name == "":
            sys.exit("Not a plate or name")
        if p_hour != None:
            hours = p_hour
        else:
            try:
                hours = int(input("Enter the number of hours you want to park the car for: "))
            except ValueError:
                sys.exit("Not a valid input")
        cost = hours * 2.5
        writer = csv.writer(file)
        writer.writerow([plate,name,hours,cost])
    print("Your car is parked!")
    print(f"You will have to pay ${cost:.2f} once you remove the car")

def remove_car(p_plate=None):
    with open("parking.csv") as file:
        reader = csv.reader(file)
        rows = list(reader)
    if not rows:
        sys.exit("No car parked in the lot")
    if p_plate is not None:
        plate = p_plate
    else:
        plate = input("Enter the license plate of the car you want to remove from the lot: ")
        if plate == "":
            sys.exit("Not a valid plate")
    found = False
    lst = []
    for row in rows:
        if row[0] == plate:
            found = True
            found_row = row
        else:
            lst.append(row)
    if not found:
        sys.exit("No such car found")
    else:
        cost = float(found_row[3])
        print(f"You have to pay ${cost:.2f}")
        with open("parking.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lst)
        sys.exit("Your car has successfully been removed from the lot!")

def total_car_parked():
        items = []
        with open("parking.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                items.append(row)
            if len(items) == 0:
                sys.exit("No cars parked")
            print(tabulate(items, headers = ["plate", "name", "hour", "cost"], tablefmt = "grid"))


if __name__ == "__main__":
    main()
