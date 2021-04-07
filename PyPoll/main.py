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

    for row in csvreader:
        vote_count = vote_count + 1

        #print(f"{vote_count}")

    print(f"{vote_count}")

