import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

def analyze_financial_data(csvpath):
    with open(csvpath) as budget_file:
        csvreader = csv.reader(budget_file, delimiter=',')
        csv_header = next(csvreader)

        
        months = []
        profit_loss = []

        for row in csvreader:
            months.append(row[0])
            profit_loss.append(int(row[1]))

    moneylist = []  
    avglist = []    

    for i in range(0, len(profit_loss)):
        val1 = profit_loss[i]
        val2 = profit_loss[i-1]
        moneylist.append(val1)

        if i > 0:  # avoid first month's average change calculation
            avg_1 = val1 - val2
            avglist.append(avg_1)

    sumtotal = sum(moneylist)  

    greatest_increase = max(avglist)
    greatest_decrease = min(avglist)

    # avglist starts from the second month, so we add 1 to the index
    greatest_increase_month = months[avglist.index(greatest_increase) + 1]
    greatest_decrease_month = months[avglist.index(greatest_decrease) + 1]

    
    output = [
        "----------------------------",
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {len(months)}",
        f"Total:  ${sumtotal}",
        f"Average Change: ${round(sum(avglist)/len(avglist), 2)}",
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})",
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
    ]

    return output


# Write the output to a text file

output_path = os.path.join('..', 'analysis', 'financial_analysis_output.txt')

output = analyze_financial_data(csvpath)


with open(output_path, mode='w') as output_file:
    for line in output:
        output_file.write(line + '\n')

for line in output:
    print(line)

     

     




