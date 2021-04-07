#PyPoll Challenge

#Modules

import os
import csv

#import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    vote_count = 0


    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for  row in csvreader:
        if str(row[2]) = str("Khan")
            khan_votes = khan_votes + 1
            
    print(f"{khan_votes}")

    for row in csvreader:
        vote_count = vote_count + 1

        #print(f"{vote_count}")

    print("Election Results")
    print("------------------------------")
    print(f"Total votes: {vote_count}")
    print("------------------------------")

