from pathlib import Path 
import csv

def cashonhand():
    """
    Reads from CSV file and calculates the day to day diffrence in cash on hand.
    - If the cash-on-hand is always increasing: it finds out the day and amount the highest increment occurs.
    - If the cash-on-hand is always decreasing: it finds out the day and amount the highest decrement occurs. 
    - If the cash-on-hand fluctuates: it lists down all the days and amounts when a deficit occurs, also finds out the top 3 highest deficit amounts and the days it occured.
    """
    # Create a file path to csv file.
    fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

    # Read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

        # Create an empty list
        Cash_on_Hand=[] 

        # Append day and cash on hand into the Cash_on_Hand list
        for row in reader:
            # Get the day, cash on hand 
            # And append to the Cash_on_Hand list
            Cash_on_Hand.append([row[0],row[1]])

    # Create Lists for cash surplus, deficits and fluctuations
    surplus = []
    deficits = []
    fluctuate = []

    start = float(Cash_on_Hand[0][1]) 

    # Calculate changes in cash on hand for each day
    for day in Cash_on_Hand[1:]: 
        
        COH = float(day[1]) # Make cash on hand a float
        diff = round(COH - start) # Calculate change in cash on hand and round to 0dp

        # Check for an increase in cash in hand/surplus
        if COH > start: 
            surplus.append((diff,day[0]))
            fluctuate.append((diff,day[0]))
            start = COH

        # Check for an decrease in cash in hand/deficit
        elif COH < start: 
            deficits.append((diff,day[0]))
            fluctuate.append((diff,day[0]))
            start = COH 

    # Prints results based on the scenarios
    result = "" # Stores results
    # If cash on hand is always increasing
    if len(surplus) == len(Cash_on_Hand)-1: 
        surplus.sort()
        result += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THEN THE PREVIOUS DAY\n"
        result += f"[HIGHEST CASH SURPLUS] DAY: {surplus[-1][1]}, AMOUNT: SGD {abs(surplus[0][0])}\n"

    # If cash on hand is always decreasing
    elif len(deficits) == len(Cash_on_Hand)-1 : 
        deficits.sort()
        result += f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THEN THE PREVIOUS DAY\n"
        result += f"[HIGHEST CASH DEFICIT] DAY: {deficits[0][1]}, AMOUNT: SGD {abs(deficits[0][0])}\n"

    # If cash on hand fluctuates
    else: 
        # Lists all days with a deficit and the amount
        for day in fluctuate: 
            if day[0] < 0: 
                    result += f"[CASH DEFICIT] DAY: {day[1]}, AMOUNT: SGD {abs(day[0])}\n"
        # Sorts and prints the top 3 highest deficits
        fluctuate.sort()
        result += f"[HIGHEST CASH DEFICIT] DAY: {fluctuate[0][1]}, AMOUNT: SGD {abs(fluctuate[0][0])}\n"
        result += f"[2ND HIGHEST CASH DEFICIT] DAY: {fluctuate[1][1]}, AMOUNT: SGD {abs(fluctuate[1][0])}\n"
        result += f"[3RD HIGHEST CASH DEFICIT] DAY: {fluctuate[2][1]}, AMOUNT: SGD {abs(fluctuate[2][0])}\n"
    
    return result