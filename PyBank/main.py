# The dataset is composed of two columns: `Date` and `Profit/Losses`
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The average of the changes in "Profit/Losses" over the entire period
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in losses (date and amount) over the entire period
# * In addition, your final script should both print the analysis to the terminal
# * Export a text file with the results

# Modules 
import os
import csv

# Set path for file  PayBank/Resources 
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# Lists 
total_months = []
total_profit_losses = []
change_profit_losses = []

# Open the CSV --budget_data.csv
with open(csvpath,newline="", encoding="utf-8") as csvpath:
   csvreader = csv.reader(csvpath,delimiter=",")

# Remove header 
   header = next(csvreader)

# Loop for rows
   for row in csvreader:

       total_months.append(row[0])
       total_profit_losses.append(int(row[1]))

   # Loop through the profit_losses list to get the monthly change
   # Take the difference btw two months and .append to change_profit_losses
   for i in range(len(total_profit_losses)-1):
       change_profit_losses.append(total_profit_losses[i+1]-total_profit_losses[i])

# The max increase in profits (date and amount) 
max_increase_value = max(change_profit_losses)
max_increase_month = change_profit_losses.index(max(change_profit_losses)) + 1

# The max decrease in profits (date and amount) 
max_decrease_value = min(change_profit_losses)
max_decrease_month = change_profit_losses.index(min(change_profit_losses)) + 1

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: $ {sum(total_profit_losses)}")
print(f"Average Change: $ {round(sum(change_profit_losses)/len(change_profit_losses),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} ($ {(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ($ {(str(max_decrease_value))})")


#Export a text file with the results
textfile_path = os.path.join('.','Resources','Final_Results.txt')

with open (textfile_path, 'w') as txtfile:
    txtfile.write(f"Financial Analysis")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {len(total_months)}")
    txtfile.write("\n")
    txtfile.write(f"Total: $ {sum(total_profit_losses)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: $ {round(sum(change_profit_losses)/len(change_profit_losses),2)}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} ($ {(str(max_increase_value))})") 
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ($ {(str(max_decrease_value))})")


# END :) 

