def predict_expense(expenses):
    """
    Predict next expense using simple average of past expenses.
    expenses: list of tuples -> (id, date, name, category, amount)
    """
    if not expenses:
        return 0

    total = sum(exp[4] for exp in expenses)  # amount is at index 4
    avg = total / len(expenses)
    return round(avg, 2)
