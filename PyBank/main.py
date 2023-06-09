import os
import csv
budget_csv = os.path.join(".","resources","budget_data.csv")

#identifying all variables used
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
# variables for largest decrease
Greatest_Decrease = 0
Greatest_Decrease_Month= 0

# first print line and dots
print("Financial Analysis")
print("---------------------------------------")

#calculated total montshs
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #skips header
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
        #adding $ signs
        Total_Dollars = "${:,.0f}".format(Total)
print("Total: ", Total_Dollars)

#calculate average change, you got this!!! Ask one of TA's to review to see if i'm doing too many extra steps
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

        profit_increase = Amount - Previous_Value

        if profit_increase > Greatest_Increase:
            Greatest_Increase = profit_increase
            Greatest_Increase_Month = date

        Previous_Value = Amount
        #adding dollar signs
        greatest_increase_dollars = "${:,.0f}".format(Greatest_Increase)
print(f"Greatest Increase in Profits: {Greatest_Increase_Month} ({greatest_increase_dollars})")

#finding the greatest decrease in profits, including the date and $
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        date = row[0]
        Amount=int(row[1])

        profit_decrease = Amount - Previous_Value

        if profit_decrease < Greatest_Decrease:
            Greatest_Decrease = profit_decrease
            Greatest_Decrease_Month = date
        
        Previous_Value = Amount
        #adding $$ signs
        greatest_decrease_dollars = "${:,.0f}".format(Greatest_Decrease)
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} ({greatest_decrease_dollars})")

#trying to export the analysis 

#identifying the txt file
PyBank_Export_File = "PyBank_Analysis.txt"
export_path = os.path.join(".", "analysis", PyBank_Export_File)

with open(export_path, "w") as file:
    #after finishing pypoll, finally figured out the line break, writing here and finishing later (\n) and place before end of ""
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {Total_Months}\n")
    file.write(f"Total: {Total_Dollars}\n")
    file.write(f"Average Change: {Average_Change_Dollars}\n")
    file.write(f"Greatest Increase in Profits: {Greatest_Increase_Month} ({greatest_increase_dollars})\n")
    file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} ({greatest_decrease_dollars})\n")
        
  #finished!!! the above code  export a text file to the analsysis folder in PyBank, if have extra time, try and break up the text to make it look nicer      
# just realized i don't have dollar signs on total, greatest increase, or greatest decrease, if i have time i will add, it is on average change so i should be able to easily copy/paste
