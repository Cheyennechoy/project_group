from pathlib import Path
import csv

def profitandloss():
    """
    Reads from CSV file and calculates the day to day diffrence in net profit.
    - If the net profit is always increasing: it finds out the day and amount the highest increment occurs.
    - If the net profit is always decreasing: it finds out the day and amount the highest decrement occurs. 
    - If the net profit fluctuates: it lists down all the days and amounts when a deficit occurs, also finds out the top 3 highest deficit amounts and the days it occured.
    """
    # Create a file path to csv file     
    fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"
    # Read the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

        # Create an empty list
        profitloss = []

        # Append day and net profit into the profitloss list
        for row in reader:
            # Get the day, net profit 
            # And append to the profit and loss list
            profitloss.append([row[0],row[4]])


    # Create Lists for net profit surplus, deficits and fluctuations
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

    result="" # Stores results
    
    # Prints results based on the scenarios
    # If profit and loss is always increasing
    if len(surplus) == len(profitloss)-1: 
        surplus.sort()
        result += "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THEN THE PREVIOUS DAY\n"
        result += f"[HIGHEST NET PROFIT SURPLUS] DAY: {surplus[-1][1]}, AMOUNT: SGD {abs(surplus[-1][0])}\n"

    # If profit and loss is always decreasing
    elif len(deficits) == len(profitloss)-1 : 
        deficits.sort()
        result += "[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THEN THE PREVIOUS DAY\n"
        result += f"[HIGHEST NET PROFIT DEFICIT] DAY: {deficits[0][1]}, AMOUNT: SGD {abs(deficits[0][0])}\n"

    # If profit and loss fluctuates
    else: 
        # Lists all days with a deficit and the amount
        for day in fluctuate: 
            if day[0] < 0: 
                result += f"[NET PROFIT DEFICIT] DAY: {day[1]}, AMOUNT: SGD {abs(day[0])}\n"
        # Sorts and prints the top 3 highest deficits
        fluctuate.sort()
        result += f"[HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[0][1]}, AMOUNT: SGD {abs(fluctuate[0][0])}\n"
        result += f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[1][1]}, AMOUNT: SGD {abs(fluctuate[1][0])}\n"
        result += f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {fluctuate[2][1]}, AMOUNT: SGD {abs(fluctuate[2][0])}\n"

    file_path = Path.cwd()/"Summary_report.txt"
    
    with file_path.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(result)
        # Writes results into txt file