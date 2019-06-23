#main-pybank.py 


import csv

budgetfile =  "./budget-data.csv"

total_months = 0
net_prof = 0
changes = 0
total_revenue = 0
months_count = 0
last_month = 0
great_inc = 0
great_los = 0
inc_month = ""
los_month = ""
rev_change = []
months = []
prof_loss=[]
current_month = []
change =[]
with open(budgetfile, "r") as bank_data:
    reader = csv.reader(bank_data,)
    next(reader)
   
    for row in reader:
        #total months
        total_months = total_months + 1
        months.append(row[0])

        #total net profits
        net_prof += int(row[1])

        #change in revenue
        current_month = int(row[1])
        total_revenue = total_revenue + current_month
        if months_count > 0:
            changes = current_month - last_month
            rev_change.append(changes)
            if changes > great_inc:
                great_inc = changes
                inc_month = row[0]
            elif changes < great_los:
                great_los = changes
                los_month = row[0]
        else:
            months_count += 1 
        last_month = current_month
        
sum_rev_changes = sum(rev_change)
avg_change = sum_rev_changes / (total_months - 1)

print(sum(rev_change) / len(rev_change))
print(f"Financial Analysis")
print("----------------------------------------")
print("                                        ")
print(f'Total Months: {total_months}')
print(f'Total: ${net_prof}')
print(f"Average Revenue Change: ${avg_change}")
print(los_month)
print (inc_month)
#this is as far I got to meet the deadline :(