from pathlib import Path 
import csv 
# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    Cash_on_Hand=[] 

    # append day and cash on hand into the Cash_on_Hand list
    for row in reader:
        #get the day, cash on hand 
        #and append to the Cash_on_Hand list
        Cash_on_Hand.append([row[0],row[1]])   

print(Cash_on_Hand)


#day is [11, 1458684], day[0] is 11, day[1] is 1458684
# start = 0

# s = 0
# # #calculates and prints cash deficit 
# for day in Cash_on_Hand: 
#     day[1] = float(day[1])
#     if day[1] > s:
#         s = day [1]

#     else: 
#         break 

start = 0

# calculates and prints cash deficit 
deficits = []

for day in Cash_on_Hand: 
    diff = float(day[1]) - start 
    start = float(day[1])
    if diff < 0: 
        print(f"[CASH DEFICIT] DAY: {day[0]}, AMOUNT: SGD{abs(diff)}")
        deficits.append((diff,day[0]))
    
deficits.sort()
print(f"[HIGHEST CASH DEFICIT] DAY: {deficits[0][1]}, AMOUNT: SGD{abs(deficits[0][0])}")
print(f"[2ND HIGHEST CASH DEFICIT] DAY: {deficits[1][1]}, AMOUNT: SGD{abs(deficits[1][0])}")
print(f"[3RD HIGHEST CASH DEFICIT] DAY: {deficits[2][1]}, AMOUNT: SGD{abs(deficits[2][0])}")