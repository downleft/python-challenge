#Code for PyBank

# import needed libraries to access CSV files
import os
import csv

#Access the budget_data.csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Establish various tickers
monthcount = 0 #Use this variable to count the number of months
nettotal = 0 #Use this variable to count the net total amount of Profit/Loss
previousmonth = 0 #Used to save a value of a row in order to use it in a later calculation
maxIncrease = 0 #Use to track the greatest increase in profits
maxDecrease = 0 #Use to track the greatest decrease in profits

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)

    for row in csvreader:

        #Track number of months
        currentmonth = int(row[1])

        #Save initial value as firstmonth
        if monthcount == 0:
            firstmonth = currentmonth

        #Track greatest increase and decrease
        if currentmonth - previousmonth > maxIncrease:
            maxIncrease = currentmonth - previousmonth
            monthOfIncrease = row[0]
        elif currentmonth - previousmonth < maxDecrease:
            maxDecrease = currentmonth - previousmonth
            monthOfDecrease = row[0]
        
        #Track the number of months
        monthcount += 1

        #Save Profit/Loss value before rolling to next row
        previousmonth = int(row[1])

        #Track the net total Profit/Losses
        nettotal += int(row[1])

    #Track the change in Profit/Loss
    profitchange = (int(row[1]) - firstmonth)/(monthcount-1)
    profitchange = round(profitchange,2)

    #Print out results of various calculations
    print(" ")
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {monthcount}")
    print(f"Total Profit: ${nettotal}")
    print(f"Average Change: ${profitchange} per month.")
    print(f"Greatest Increases in Profits: {monthOfIncrease} (${maxIncrease})")
    print(f"Greatest Decrerase in Profits: {monthOfDecrease} (${maxDecrease})")

#Set up file to export summative data to
output_path = os.path.join("analysis", "finanalysis.txt")

#Export summative data to text file
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {monthcount}\n")
    txtfile.write(f"Total Profit: ${nettotal}\n")
    txtfile.write(f"Average Change: ${profitchange} per month.\n")
    txtfile.write(f"Greatest Increases in Profits: {monthOfIncrease} (${maxIncrease})\n")
    txtfile.write(f"Greatest Decrerase in Profits: {monthOfDecrease} (${maxDecrease})")