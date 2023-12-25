#Code for PyPoll

# import needed libraries to access CSV files
import os
import csv

#Establish candidate variables and counts
#Note, if using this code for other elections, can change or add candidate names as needed
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidatecount = []
for name in candidates:
    candidatecount.append(0)
votercount = 0 

#Access the election_data.csv file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #Reads header row

    for row in csvreader:
        #Track total votes and candidate votes
        votercount += 1
        nameticker = 0
        for name in candidates:
            if row[2] == name:
                candidatecount[nameticker] += 1
            else:
                nameticker += 1

#Set up file to export summative data to
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as txtfile:

    #Print out results of the election and send them to txt file
    print(" ")
    print("Election Results")
    txtfile.write("Election Results\n")
    print("-------------------------")
    txtfile.write("-------------------------\n")
    print(f"Total Votes: {votercount}")
    txtfile.write(f"Total Votes: {votercount}\n")

    #Determine and announce winner
    winticker = 0
    votepercent = []
    winningcount = 0
    for name in candidates:
        votepercent.append(round(candidatecount[winticker]/votercount*100,3))
        if candidatecount[winticker] > winningcount:
            winner = candidates[winticker]
            winningcount = candidatecount[winticker]
        print(f"{name}: {votepercent[winticker]}% ({candidatecount[winticker]})")
        txtfile.write(f"{name}: {votepercent[winticker]}% ({candidatecount[winticker]})\n")
        winticker += 1
    print("-------------------------")
    txtfile.write("-------------------------\n")
    print(f"Winner: {winner}")
    txtfile.write(f"Winner: {winner}\n")
    print("-------------------------")
    txtfile.write("-------------------------")