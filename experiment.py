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

start = 0
deficits = []

# Calculates all cash deficits and stores it in a list
for day in Cash_on_Hand:
    diff = float(day[1]) - start
    start = float(day[1])
    if diff < 0:
        deficits.append((day[0], abs(diff)))

# Sorts deficits in descending order
deficits.sort(key=lambda x:x[1],reverse=True)

# Prints all cash deficits
for day, amount in deficits:
    print(f"[CASH DEFICIT] DAY: {day},AMOUNT: SGD{amount}")

# Prints top 3 highest cash deficits
print(f"[HIGHEST CASH DEFICIT] DAY: {deficits[0][0]},AMOUNT: SGD{deficits[0][1]:.0f}")
if len(deficits) > 1:
    print(f"[2ND HIGHEST CASH DEFICIT] DAY: {deficits[1][0]},AMOUNT: SGD{deficits[1][1]:.0f}")
if len(deficits) > 2:
    print(f"[3RD HIGHEST CASH DEFICIT] DAY: {deficits[2][0]},AMOUNT: SGD{deficits[2][1]:.0f}")