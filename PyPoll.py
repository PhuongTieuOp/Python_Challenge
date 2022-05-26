#  This program performs the following:
#   . Read a data file
#   . Calculate total months, total profits/loss, average change, greatest increase and decrease in profits
#   . Display calculation result on terminal
#   . Save calculation result into a text file
#  
import os
import csv

total_vote_count = 0
candidate_vote_count = 0
pct_vote = 0.0
max_vote = 0
max_name = ''

def print_hyphen_line ():
    print("-" * 79 + "\n")

# election_csv = os.path.join("..", "Resources", "election_data.csv")
election_csv = os.path.join("Resources", "election_data.csv")

candidate_dict = {} 
candidate_list = []

# Loop thru to assign value to candiate list
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    next(csv_file)
 
     # Loop thru create a list
    for row in csv_reader:
        candidate_list.append(row[2])

total_vote_count = len(candidate_list)

# Loop thru the list to create a dictionary
for i in candidate_list:
    if  i in candidate_dict.keys():
        candidate_dict[i] = candidate_dict[i]+1
    else:
        candidate_dict[i]  = 1

# Print out election results
print_hyphen_line()
print("Election Results" + "\n")
print_hyphen_line()
print("Total Votes:  " + str(total_vote_count) )
print_hyphen_line()

max_vote = max(candidate_dict.values())
for i in candidate_dict:    
    pct_vote = float(candidate_dict[i]) / total_vote_count
    print(i + ":  "+ format((pct_vote * 100), ",.3f") + "% (" + str(candidate_dict[i])+ ")")
    if candidate_dict[i] == max_vote:
        max_name = i

print_hyphen_line()
print("Winner: " + max_name)
print_hyphen_line()