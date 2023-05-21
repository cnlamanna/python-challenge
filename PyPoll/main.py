import os
import csv
election_csv = os.path.join(".","resources","election_data.csv")

#identify variables
Total_Votes = 0
Candidate_List= set()
#to calculate the percentage variable, it will use the total votes and candidate list
Tally = {}

# title plus dots
print("Election Results")
print("----------------------")

#calculationg total votes
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #skips header
    next(csvreader)
    for row in csvreader:
        votes = row[0]
        Total_Votes += 1
print("Total Votes: ", Total_Votes)

#separating dots like in result photo
print("-----------------------")

#identifying the candidates
with open(election_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        candidate = row[2]
        Candidate_List.add(candidate)

#printing individual candidate names, it's not printing in alphabetical order like the results but it still works, if I have more time i will figure out how to adjust it
for candidate_name in Candidate_List:
    #print(candidate_name)

#calculating the percentage for each candidate
    with open(election_csv) as csvfile:
        csvreader= csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            Total_Votes += 1
            candidate = row[2]
            if candidate in Tally:
                Tally[candidate] +=1
            else:
                Tally[candidate] = 1

#testing to see if tally is adding correctly
#print(f"{candidate_name}: ({Tally})")
#it produces the right #, but it produces in one line, will fix once I get percentage

#calculating percentage
for candidate_name, votes in Tally.items():
    percentage = (votes / Total_Votes) * 100
#print final time with name, percentage, tally (hopefully)
    print(candidate_name, ": {:.3f}%".format(percentage), Tally[candidate_name])
#the "tally" is repeating on each name and is repeating the names NEED TO FIX TALLY
#i think i have to add the total_votes in the same line as the candidate_name code so it doesn't repeat, i'll try it
#nope that messed it up, probably has to do with indentation, i'll play around with it
# ok, it has the right format now, but the numbers and percentages are still off
#last line of dots
print("-------------------------")
