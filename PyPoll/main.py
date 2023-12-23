#Code for PyPoll

# import needed libraries to access CSV files
import os
import csv

#Access the election_data.csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Establish candidate variables and counts
#Note, if using this code for other elections, can change candidate names as needed
#Note, if there are more candidates with the election, can create lines here for candidate4, etc
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

        #If more than 3 candidates, can update the ticker here with similar elif statements as above, swapping out then candidate#

    #Calculate percentages, round to 3 decimal places
    #Include percentage calculations for additional candidates as needed
    candidate1_percent = round(candidate1_vote/votercount*100,3)
    candidate2_percent = round(candidate2_vote/votercount*100,3)
    candidate3_percent = round(candidate3_vote/votercount*100,3)

    #Determine winner
    if candidate1_vote > candidate2_vote and candidate1_vote > candidate3_vote:
        winner = candidate1
    elif candidate2_vote > candidate3_vote:
        winner = candidate2
    else:
        winner = candidate3

    #Print out results of the election
    print(" ")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votercount}")
    print(f"{candidate1}: {candidate1_percent}% ({candidate1_vote})")
    print(f"{candidate2}: {candidate2_percent}% ({candidate2_vote})")
    print(f"{candidate3}: {candidate3_percent}% ({candidate3_vote})")
    print("-------------------------")
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