import os
import csv
budget_csv = os.path.join(".","resources","budget_data.csv")

Total_Months = 0
Total = 0
Average_Change = 0
Greatest_Income = 0
Greatest_Decrease = 0
Profit_Loss_List=[]
Previous_Value = 0
First_Row = True
Greatest_Increase = 0
Greatest_Increase_Month = 0
#a variable that will help identify the largest increase
Prior_Month_Value = 0
profit_increase = 0

with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        date = row[0]
        Total_Months +=1
print("Total Months: ", Total_Months)

#calculate total profit
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        profitlosses=int(row[1])
        Total += profitlosses
print("Total: ", Total)

#calculate average change
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        profitlosses=int(row[1])
        if not First_Row:
            Change=profitlosses - Previous_Value
            Profit_Loss_List.append(Change)
        else:
            First_Row = False
        Previous_Value = profitlosses
    if Profit_Loss_List:
        Average_Change = sum(Profit_Loss_List) / len(Profit_Loss_List)
        #shortening the average change value to 2 decimals and adding a dollar sign
        Average_Change_Dollars = "${:,.2f}".format(Average_Change)
print("Average Change: ", Average_Change_Dollars)

#find the greatest increase in profits, including the date and $
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        date = row[0]
        Amount=int(row[1])

        profit_increase = Amount - date

        if profit_increase > Greatest_Increase:
            Greatest_Increase = profit_increase
            Greatest_Increase_Month = date

            Prior_Month_Value = Amount
print(f"Greatest Increase in Profits: {date} ({profit_increase})")



