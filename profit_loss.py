from pathlib import Path
import csv

def profitandloss():
   
    # Create a file path to csv file     
    fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"
    # Read the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

        # Create an empty list
        profitloss = []

        # Append day and profit and loss into the profitloss list
        for row in reader:
            # Get the day, cash on hand 
            # And append to the profit and loss list
            profitloss.append([row[0],row[4]])

    # Create Lists for cash surplus, deficits and fluctuations
    surplus = []
    deficits = []
    fluctuate = []

    start = float(profitloss[0][1])

    # Calculate changes in profit and loss for each day
    for day in profitloss[1:]: 
        
        PAL = float(day[1]) # Make profit and lost a float
        diff = round(PAL - start) # Calculate change in profit and loss and round to 0dp

        # Check for an increase in profit and loss/surplus
        if PAL > start: 
            surplus.append((diff,day[0]))
            fluctuate.append((diff,day[0]))
            start = PAL

        # Check for an decrease in profit and loss/deficit
        elif PAL < start: 
            deficits.append((diff,day[0]))
            fluctuate.append((diff,day[0]))
            start = PAL
    # return the surplus, deficits and fluctuations

    # Prints results based on the scenarios
    # If profit and loss is always increasing
    if len(surplus) == len(profitloss)-1: 
        surplus.sort()
        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THEN THE PREVIOUS DAY")
        print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {surplus[-1][1]}, AMOUNT: SGD {abs(surplus[-1][0])}")

    # If profit and loss is always decreasing
    elif len(deficits) == len(profitloss)-1 : 
        deficits.sort()
        print("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THEN THE PREVIOUS DAY")
        print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {deficits[0][1]}, AMOUNT: SGD {abs(deficits[0][0])}")

    # If profit and loss fluctuates
    else: 
        # Lists all days with a deficit and the amount
        for day in fluctuate: 
            if day[0] < 0: 
                    print(f"[NET PROFIT DEFICIT] DAY: {day[1]}, AMOUNT: SGD {abs(day[0])}")
        # Sorts and prints the top 3 highest deficits
        fluctuate.sort()
        print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[0][1]}, AMOUNT: SGD {abs(fluctuate[0][0])}")
        print(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[1][1]}, AMOUNT: SGD {abs(fluctuate[1][0])}")
        print(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[2][1]}, AMOUNT: SGD {abs(fluctuate[2][0])}")

# Test
print(profitandloss())