import csv
import pandas as pd
def has_visited(filename, country, city):
    with open("Desktop/coding_test_preparation/trips.csv", "r",) as opened_file:
        my_reader = csv.reader(opened_file)
        for row in my_reader:
            if row[0] == country and row[1] == city:
                return True
    return False

print(has_visited("Desktop/coding_test_preparation/trips.csv", "Denmark", "Aarhus"))