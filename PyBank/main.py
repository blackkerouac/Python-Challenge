#main-pybank.py 


import csv



budgetfile =  "./budget-data.csv"
months = []
prof_loss=[]
current_month = []
last_month = 0
change =[]
with open(budgetfile, "r") as bank_data:
    reader = csv.reader(bank_data,)
    next(reader)
    total_months = 0
    net_prof = 0
    changes = 0
    rev_change = []
    total_revenue = 0
    months_count = 0
    for row in reader:
        #total months
        total_months = total_months + 1
        months.append(row[0])

        #total net profits
        net_prof += int(row[1])

        #change in revenue
        current_month = int(row[1])
        total_revenue = total_revenue + current_month
        if months_count > 1:
            changes = current_month - last_month
            rev_change.append(changes)
        last_month = current_month

sum_rev_changes = sum(rev_change)
avg_change = sum_rev_changes / (total_months - 1)


print(f"Financial Analysis")
print("----------------------------------------")
print("                                        ")
print(f'Total Months: {total_months}')
print(f'Total: ${net_prof}')
print(f"Average Revenue Change: ${avg_change}")

#this is as far I got to meet the deadline :(