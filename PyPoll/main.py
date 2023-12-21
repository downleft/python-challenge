#Code for PyPoll

# import needed libraries to access CSV files
import os
import csv

#Access the election_data.csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Establish candidate variables and counts
totalvote = 0
candidate1 = "Charles Casper Stockham"
candidate1_vote = 0
candidate2 = "Diana DeGette"
candidate2_vote = 0
candidate3 = "Raymon Anthony Doane"
candidate3_vote = 0
othervote = 0


#Establish various tickers
votercount = 0 #Use this variable to count the number of voters

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        #Track number of voters
        votercount = votercount + 1

        #Track votes for first candidate
        if row[2] == candidate1:
            candidate1_vote = candidate1_vote + 1
        
        #Track votes for second candidate
        elif row[2] == candidate2:
            candidate2_vote = candidate2_vote + 1

        #Track votes for third candidate
        elif row[2] == candidate3:
            candidate3_vote = candidate3_vote + 1

    #Print out results of various calculations
    print(" ")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votercount}")
    print(f"{candidate1}: {candidate1_vote}")
    print(f"{candidate2}: {candidate2_vote}")
    print(f"{candidate3}: {candidate3_vote}")