#  This program performs the following:
#   . Read a data file
#   . Calculate total months, total profits/loss, average change, greatest increase and decrease in profits
#   . Display calculation result on terminal
#   . Save calculation result into a text file
#  
import os
import csv

mth_count = 0
pl_total = 0.0
pl_previous = 0.0
pl_current = 0.0 
pl_increase = 0.0
pl_increase_date = ""
pl_decrease = 0.0
pl_decrease_date = ""
pl_avg_change = 0.0
amt_increase = 0.0
amt_decrease = 0.0
first_record = True
pl_first = 0.0

# budget_csv = os.path.join("..", "Resources", "budget_data.csv")
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    next(csv_file)
 
     # Read through each row of data after the header
    for row in csv_reader:

        pl_current = float(row[1])

        # Count months
        mth_count += 1
        
        # Calculate profit and loss total
        pl_total += pl_current

        # Save first record's profit and lost for later calculation
        if first_record == True:
            pl_first = pl_current
    
        # Find greatest increase in profits
        if  pl_increase < pl_current:
            pl_increase = pl_current
            pl_increase_date = row[0]
            amt_increase = pl_increase - pl_previous
 
         # Find greatest decrease in profits
        if  pl_decrease > pl_current:
            pl_decrease = pl_current
            pl_decrease_date = row[0]
            amt_decrease = pl_decrease - pl_previous

        pl_previous = pl_current
        first_record = False

# Calculate average change 
pl_avg_change = (pl_current - pl_first)/(mth_count-1)

# Print results on the terminal
print("-" * 79 + "\n")
print("Financial Analysis Report" + "\n")
print("-" * 79 + "\n")
print("Total months: \t\t\t", str(mth_count))
print("Total profit/loss: \t\t", "$", format(pl_total, ",.2f"))
print("Average change: \t\t", "$", format(pl_avg_change, ",.2f"))
print("Greatest Increase in Profits: \t", str(pl_increase_date), "  $", format(amt_increase,",.2f"))
print("Greatest decrease in Profits: \t", str(pl_decrease_date), "  $", format(amt_decrease, ",.2f"))
print("-" * 79 + "\n")

# Save results to a report file
report = open("PyBank_Report.txt", "w")

report.write("-" * 79 + "\n")
report.write("Financial Analysis Report" + "\n")
report.write("-" * 79 + "\n")
report.write("Total months: \t\t\t" + str(mth_count) + "\n")
report.write("Total profit/loss: \t\t" + "$" + format(pl_total, ",.2f") + "\n")
report.write("Average change: \t\t" + "$" + format(pl_avg_change, ",.2f") + "\n")
report.write("Greatest Increase in Profits: \t" + str(pl_increase_date) + "  $" + format(amt_increase,",.2f") + "\n")
report.write("Greatest decrease in Profits: \t" + str(pl_decrease_date) + "  $" + format(amt_decrease, ",.2f") + "\n")
report.write("-" * 79 + "\n")

report.close()