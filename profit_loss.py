from pathlib import Path 
import csv 
# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    Profit_and_Loss=[] 

    # append day and cash on hand into the Cash_on_Hand list
    for row in reader:
        #get the day, cash on hand 
        #and append to the Cash_on_Hand list
        Profit_and_Loss.append([row[0],row[4]])   

print(Profit_and_Loss)


