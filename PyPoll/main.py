#PyPoll Challenge

#Modules

import os
import csv

#import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    vote_count = 0
    candidate_list = []
    results = {}

    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csvreader:
        vote_count = vote_count + 1

        #print(f"{vote_count}")
        candidate = str(row[2])

        if candidate not in candidate_list: 
            candidate_list.append(str(candidate))

        if (candidate == 'Khan'):
           Khan_votes += 1
        elif(candidate == 'Correy'):
            Correy_votes = Correy_votes +1 
        elif (candidate == 'Li'):
            Li_votes = Li_votes + 1
        elif(candidate == "O'Tooley"):
            Otooley_votes +=1
            

    

    print("Election Results")
    print("------------------------------")
    print(f"Total votes: {vote_count}")
    print("------------------------------")

