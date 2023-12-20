# import needed libraries to access CSV files
import os
import csv

#Access the budget_data.csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")