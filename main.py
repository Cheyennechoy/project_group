import profit_loss,cash_on_hand,overheads

def main():
    """
    Writes the reults of profit_loss.py, cash_on_hand.py and overheads.py to a text file summary_report.txt
    """
    overheads_result = overheads.overheadsfunc()
    cash_on_hand_result = cash_on_hand.cashonhand()
    profit_loss_result = profit_loss.profitandloss()

    with open("summary_report.txt","w") as file:
        file.write(overheads_result)
        file.write(cash_on_hand_result)
        file.write(profit_loss_result)

if __name__ == "__main__":
    main()