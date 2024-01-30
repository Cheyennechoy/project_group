from pathlib import Path 
import csv

def overheadsfunc():
    """
    Reads CSV file and finds the highest overhead category and it's value.
    """
    # create a file path to overheads csv file.
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    result = "" # Stores results

    # read the overheads csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list
        Overheads=[] 

        # append day and overheads into the list
        for row in reader:
            Overheads.append([row[0],row[1]])   

    start = 0 
    for category in Overheads: 
        value = float(category[1])
        if value > start: 
            start = value 
            highest = category[0]

    result += f"[HIGHEST OVERHEAD] {highest.upper()}: {start}%\n"    
    
    file_path = Path.cwd()/"summary_report.txt"
    # Create the text file 
    file_path.touch()

    # Write the paymentSummary information in the text file
    with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
    # Write the headings
        file.write(result)
