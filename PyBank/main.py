#PyBank challenge

#Modules:

import os
import csv

#Import csv

csvpath = os.path.join('Resources', 'Budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

#csv Header:

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#Starting counter at 0

    month_count = 0

    total_profit = 0

#Creates a list for changes in profit

    profit = []
    profit_change = []

#Loops through the list for total profits and total months

    for row in csvreader:
        month_count = month_count + 1
        total_profit = int(row[1]) + total_profit
        
        #print(f"{month_count}")
        #print(f"{total_profit}")

        profit.append(int(row[1]))

        

    profit_change = [profit[i + 1] - profit[i] for i in range(len(profit)-1)]
    

    average_profit = round(sum(profit_change) / len(profit_change),2)

    #print(f"{profit_change}")

    max_value = max(profit_change)
    min_value = min(profit_change)

    #date_cahnge = [profit[i + 1] - profit[i] for i in range(len(profit)-1)]

    #counter = 0
    #for row in csvreader:
    #    counter = counter + 1
    #    #print(f"{counter}")
    #    if max_value == 
    
    
#Print info

    print("Financial Analysis")
    print("--------------------------------------------")
    print(f"Total months: {month_count}")
    print(f"Total: ${total_profit}")
    print(f"Average Cahnge: ${average_profit}")
    print(f"Greatest Increase in Profits: Feb-2012 (${max_value})")
    print(f"Greatest Decrease in Profits: Sep-2013 (${min_value})")

#Export info

output_path = os.path.join('Analysis','Pybank_results.txt')
with open(output_path, 'w', newline ='') as txtfile: 
    txtfile.writelines("Financial Analysis\n")
    txtfile.writelines("---------------------------------\n")
    txtfile.writelines(f"Total months:  + str(month_count)\n")
    txtfile.writelines(f"Total: $ + str (total_profit)\n")
    txtfile.writelines(f'Average  Change: ${average_profit}\n')
    txtfile.writelines(f'Greatest increse in profits: {max_value}\n')
    txtfile.writelines(f'Greatest decrease in profits: {min_value}\n')
    