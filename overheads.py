from pathlib import Path 
import csv 
# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    Overheads=[] 

    # append day and cash on hand into the Cash_on_Hand list
    for row in reader:
        #get the day, cash on hand 
        #and append to the Cash_on_Hand list
        Overheads.append([row[0],row[1]])   

# print(Overheads)

start = 0 
for category in Overheads: 
    value = float(category[1])
    if value > start: 
        start = value 
        highest = category[0]

print(f"[HIGHEST OVERHEAD] {highest.upper()}: {start}%")