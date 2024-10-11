from project import park_car, remove_car, total_car_parked
import csv
import pytest

def test_park_car():
    with open("parking.csv", "w") as file:
        pass
    park_car("test_plate", p_name = "test_name", p_hour = 1)
    with open("parking.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            assert row[0] == "test_plate"
            assert row[1] == "test_name"
            assert row[2] == "1"
            with pytest.raises(SystemExit):
                park_car("test_plate", p_name = "test_name", p_hour = 1)

def test_remove_car():
    with open("parking.csv", "w") as file:
        pass
    with pytest.raises(SystemExit):
        remove_car("test_plate")
    with open("parking.csv", "w") as file:
        writer = csv.writer(file)
        row = ["test_plate", "test_name", 2, 5]
        writer.writerow(row)
    with pytest.raises(SystemExit):
        remove_car("test_wrong_plate")
    with pytest.raises(SystemExit):
        remove_car("test_plate")

def test_total_car_parked():
    with open("parking.csv", "w") as file:
        pass
    with pytest.raises(SystemExit):
        total_car_parked()
