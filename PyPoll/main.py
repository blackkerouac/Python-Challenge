import csv

#Set counters
tot_votes = 0
winner_votes = 0 

#set null strings
winner = ""
candid = ""

#set empty dictionaries
candid_votes = {}
candid_percent ={}

# open file
election_csv = ('./election_data.csv')
with open(election_csv,'r') as file:
    reader = csv.reader(file)

    next(reader)
    # for each row in file, count each candidates votes
    for row in reader:
        
        if candid in candid_votes:
            candid_votes[candid] = candid_votes[candid] + 1
        else:
            candid_votes[candid] = 1

        tot_votes = tot_votes + 1
        candid = row[2]
        


for i, votes in candid_votes.items():
    candid_percent[i] = '{0:.0%}'.format(votes / tot_votes)
    if votes > winner_votes:
        winner_votes = votes
        winner = i

# print out results

print("Election Results")
print("------------------------------------")
print(f"Total Votes: {tot_votes}")
print("------------------------------------")
print("                                    ")

for i, votes in candid_votes.items():
    print(f"{i}: {candid_percent[i]} ({votes})")
print(f"Winner: {winner}")
