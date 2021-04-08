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
    results_dict = {}

    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

#Votes count

    for row in csvreader:
        vote_count = vote_count + 1

        #print(f"{vote_count}")
        
        candidate = str(row[2])

        #Votes counter:

        if candidate not in candidate_list: 
            candidate_list.append(str(candidate))

        if (candidate == 'Khan'):
           khan_votes = khan_votes + 1
        elif(candidate == 'Correy'):
            correy_votes = correy_votes + 1 
        elif (candidate == 'Li'):
            li_votes = li_votes + 1
        elif(candidate == "O'Tooley"):
            otooley_votes = otooley_votes + 1


#Percents Calc:

    k_percent = round(((khan_votes * 100)/vote_count),2)
    c_percent = round(((correy_votes * 100)/vote_count),2)
    l_percent = round(((li_votes * 100)/vote_count),2)
    o_percent = round(((otooley_votes * 100)/vote_count),2)
    
    results_dict =[{"Candidate":"Khan",
                    "Votes":khan_votes,
                    "Percent":l_percent}, 
                    {"Candidate":"Li","Votes": li_votes , "Percent": l_percent}, 
                    {"Candidate":"O'tooley",
                    "Votes":otooley_votes,
                    "Percent":o_percent}, 
                    {"Candidate":"Correy",
                    "Votes":correy_votes,
                    "Percent":c_percent}]

#Winner Calc:

    for results in results_dict:
        if khan_votes > li_votes and otooley_votes and correy_votes:
            winner = "Khan"
        elif li_votes > khan_votes and otooley_votes and correy_votes:
            winner = "Li"
        elif otooley_votes > khan_votes and li_votes and correy_votes: 
            winner = "O'tooley"
        else: 
            winner = "Correy"    
            


    print("Election Results")
    print("------------------------------")
    print(f"Total votes: {vote_count}")
    print("------------------------------")
    print(f"Khan:{k_percent} ({khan_votes})")
    print(f"Khan:{c_percent} ({correy_votes})")
    print(f"Khan:{l_percent} ({li_votes})")
    print(f"Khan:{o_percent} ({otooley_votes})")
    print("------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------")


#OUTPUT:

    output_path = os.path.join('Analysis','PyPoll_results.txt')
    with open(output_path, 'w', newline ='') as txtfile: 
        txtfile.writelines("Election results\n")
        txtfile.writelines("-----------------------------------------------------\n")
        txtfile.writelines(f'Total votes: {vote_count}\n')
        txtfile.writelines("------------------------------------------------------\n")
        txtfile.writelines(f'Khan: {k_percent}  ({khan_votes})\n')
        txtfile.writelines(f'Correy: {c_percent}  ({correy_votes})\n')
        txtfile.writelines(f'Li: {l_percent}  ({li_votes})\n')
        txtfile.writelines(f'Otooley: {o_percent} ({otooley_votes})\n')
        txtfile.writelines("-------------------------------------------------------\n")
        txtfile.writelines(f"Winner: {winner}\n")
        txtfile.writelines("--------------------------------------------------------\n")
        
