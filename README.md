# Simple Parking Lot Manager
#### Video Demo:  https://youtu.be/Y8rx8uXN0T4
#### Description:
This program allows the user to manage a simple parking lot by adding, removing or displaying the cars parked in a tabular format. There are 4 files in this project folder, namely:
- project.py
- test_project.py
- requirements.txt
- README.md
The project I have made is in the file called `project.py` and when run it takes in input from the user. The file called `test_project.py` file tests the 3 funtions `park_car()`, `remove_car()` and `total_car_parked()` from `project.py`. The file called `requirement.txt` has the command-line argument for installing the required library for this project. Finally, the file called `README.md` gives the detailed description of the project.

The only file needed to run this project is `project.py`. When the file is run, it asks the user for 3 choices:
1. Park your car
2. Remove car from the parking lot
3. Total cars parked in the lot today

If the user chooses 1, then the program asks the user to enter the license plate number, name and number of hours the user wants to park the car. Incase the user fails to provide the license plate number or name, then the program exits saying `Not a plate or name`. If the user provides invalid hour then the program exits saying `Not a valid input`. If the user tries to enter a duplicate entry, then the program exits with a message saying `This entry already exits`. All these functionalities are included in the `park_car()` function. `def park_car(plate, p_name = None, p_hour = None)` this line of code might might confuse some people but as you will also see in other places of the program, I have done this so that I can avoid working on a logic in `test_project.py` which would ask me to give inputs. I have also used the `seek()` method in this function to start reading the file from top to bottom. Finally, if all the necessary inputs are given correctly, the car is 'parked in the lot', i.e., a new entry is stored in a file called `parking.csv`.

If the user chooses 2, then the program asks the user to enter the license plate of the car that the user wants to remove. Incase the user fails to provide a license plate number, the program exits showing a message that says `Not a valid plate`. If the license plate entered by the user is not parked then the program exits showing the message `No such car found`. If the car is found in the parking lot then the program tells the user the amount of money they owe and also the "the car is removed from the parking lot", i.e., the cars entry is deleted from `parking.csv`. All these functionalities are included in the `remove_car()` function. This function took me the most time to figure, and that is because I had to come up with a way to read a file, search for the entry I wanted, delete and then update the file making sure that I haven't left any gaps in the csv.

If the user chooses 3, then one of two things could happen:
1. If there are no entries in the csv file then the program exits showing a message that says `No cars parked`
2. If there is any car parked in the lot, i.e., there is an entry present in the file called `parking.csv`, then all the entries are displayed in a tabular format
I took inspiration for this function from `Problem set 6, Pizza Py`. I have used the library called tabulate which needs to be installed before running the program using `-pip install tabulate`.

This sums up the project I have created, challenges I faced while working on it and also how it solved them. I had a really fun time coming up with this project and woking on it. This CS50 course has taught me a lot.
