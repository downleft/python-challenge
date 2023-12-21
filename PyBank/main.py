# import needed libraries to access CSV files
import os
import csv

#Access the budget_data.csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Establish various tickers
monthcount = 0 #Use this variable to count the number of months
nettotal = 0 #Use this variable to count the net total amount of Profit/Loss
profitchange = 0 #Use to track the change in Profit/Loss
setmonth = 0
maxIncrease = 0 #Use to track the greatest increase in profits
maxDecrease = 0 #Use to track the greatest decrease in profits

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #row = list(csvreader)
    #print(row[0][1])

    for row in csvreader:
        currentmonth = int(row[1])
        if monthcount == 0:
            profitchange = currentmonth

        if currentmonth - setmonth > maxIncrease:
            maxIncrease = currentmonth - setmonth
        elif currentmonth - setmonth < maxDecrease:
            maxDecrease = currentmonth - setmonth
        #Track the number of months
        monthcount = monthcount + 1
        setmonth = int(row[1])

        #Track the net total Profit/Losses
        nettotal = nettotal + int(row[1])

    #Track the change in Profit/Loss
    profitchange = (profitchange - int(row[1]))/(monthcount-1)
    profitchange = round(profitchange,2)


    print(f"Total Months: {monthcount}")
    print(f"Total Profit: ${nettotal}")
    print(f"Average Change S{profitchange} per month.")
    print(f"Greatest increases in profits {maxIncrease}")
    print(f"Greatest decrerase in profits {maxDecrease}")