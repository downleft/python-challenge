# import needed libraries to access CSV files
import os
import csv

#Access the budget_data.csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Establish various tickers
monthcount = 0 #Use this variable to count the number of months
nettotal = 0 #Use this variable to count the net total amount of Profit/Loss
profitchange = 0 #Use to track the change in Profit/Loss
maxIncrease = 0 #Use to track the greatest increase in profits
maxDecrease = 0 #Use to track the greatest decrease in profits

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        monthcount = monthcount + 1

    print(f"The total number of months is {monthcount} months.")