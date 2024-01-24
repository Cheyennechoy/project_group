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

# print(Cash_on_Hand)


surplus = []
deficits = []
flunctuate = []
start = float(Cash_on_Hand[0][1])

for day in Cash_on_Hand[1:]: 
    
    COH = float(day[1])
    diff = COH - start 

    if COH > start: 
        surplus.append((diff,day[0]))
        flunctuate.append((diff,day[0]))
        start = COH

    elif COH < start: 
        deficits.append((diff,day[0]))
        flunctuate.append((diff,day[0]))
        start = COH 

# print(surplus)
# print(deficits)
# print(flunctuate)

if len(surplus) == len(Cash_on_Hand)-1: 
    surplus.sort()
    print(f"[HIGHEST CASH SURPLUS] DAY: {surplus[-1][1]}, AMOUNT: {surplus[-1][0]}")

elif len(deficits) == len(Cash_on_Hand)-1 : 
    deficits.sort()
    print(f"[HIGHEST CASH DEFICIT] DAY: {deficits[0][1]}, AMOUNT: {deficits[0][0]}")

else: 
    for day in flunctuate: 
        if day[0] < 0: 
                print(f"[CASH DEFICIT] DAY: {day[1]}, AMOUNT: SGD{abs(day[0])}")
    flunctuate.sort()
    print(f"[HIGHEST CASH DEFICIT] DAY: {flunctuate[0][1]}, AMOUNT: SGD{abs(flunctuate[0][0])}")
    print(f"[2ND HIGHEST CASH DEFICIT] DAY: {flunctuate[1][1]}, AMOUNT: SGD{abs(flunctuate[1][0])}")
    print(f"[3RD HIGHEST CASH DEFICIT] DAY: {flunctuate[2][1]}, AMOUNT: SGD{abs(flunctuate[2][0])}")



