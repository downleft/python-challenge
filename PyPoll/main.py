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
        votercount += 1

        #Track votes for first candidate
        if row[2] == candidate1:
            candidate1_vote += 1
        
        #Track votes for second candidate
        elif row[2] == candidate2:
            candidate2_vote += 1

        #Track votes for third candidate
        elif row[2] == candidate3:
            candidate3_vote += 1

    #Calculate percentages
    candidate1_percent = candidate1_vote/votercount
    candidate1_percent = round(candidate1_percent*100,3)
    candidate2_percent = candidate2_vote/votercount
    candidate2_percent = round(candidate2_percent*100,3)
    candidate3_percent = candidate3_vote/votercount
    candidate3_percent = round(candidate3_percent*100,3)

    #Print out results of various calculations
    print(" ")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votercount}")
    print(f"{candidate1}: {candidate1_percent}% ({candidate1_vote})")
    print(f"{candidate2}: {candidate2_percent}% ({candidate2_vote})")
    print(f"{candidate3}: {candidate3_percent}% ({candidate3_vote})")
    print("-------------------------")

    #Determine winner
    if candidate1_vote > candidate2_vote and candidate1_vote > candidate3_vote:
        winner = candidate1
    elif candidate2_vote > candidate3_vote:
        winner = candidate2
    else:
        winner = candidate3
    
    print(f"Winner: {winner}")
    print("-------------------------")

#Set up file to export summative data to
output_path = os.path.join("analysis", "election_results.txt")

#Export summative data to text file
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {votercount}\n")
    txtfile.write(f"{candidate1}: {candidate1_percent}% ({candidate1_vote})\n")
    txtfile.write(f"{candidate2}: {candidate2_percent}% ({candidate2_vote})\n")
    txtfile.write(f"{candidate3}: {candidate3_percent}% ({candidate3_vote})\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------")