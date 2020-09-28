def saturdays_bank_transactions(transatcions) -> (float, float):
    savings = 1096.25
    checking = 1590.80
    num = 0
    
    for value in transactions:
        temp_value = (transactions[num])
        if temp_value >= 0:
            checking += (temp_value * 0.85)
            savings += (temp_value * 0.15)
        else:
            checking += temp_value
        num += 1
    return checking, savings

if __name__ == "__main__":
    transactions = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transactions)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))
