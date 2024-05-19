# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = "resources/budget_data.csv"

# variable
month_count = 0
total_profit = 0

# for changes 
last_month_profit = None
changes = []
# Open the CSV using the UTF-8 encoding
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

       

        # Read each row of data after the header
        for row in csvreader:
                print(row)

                
                 # count months
                month_count = month_count + 1

                 # add profit
             
                total_profit = total_profit + int(row[1])
                
                # last month profit
                # subtract this month profit - last month profit
                # APPEND that change to the list
                
                # IF first row, there is no change
                if (month_count == 1): 
                    # by definition, this is the first row
                    # no change 
                    last_month_profit = int(row[1])
                else:
                    change = int(row[1]) - last_month_profit
                    changes.append(change)
        print(month_count)
        print(total_profit)
        print(len(changes))

output = f'''
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

print(output)