def total_expense(data):
    total = 0

    for row in data:
        total += row[4]

    return total


def category_wise(data):
    result = {}

    for row in data:
        category = row[3]
        amount = row[4]

        result[category] = result.get(category, 0) + amount

    return result


def monthly_wise(data):
    result = {}

    for row in data:
        date = str(row[1])
        month = date[:7]

        amount = row[4]

        result[month] = result.get(month, 0) + amount

    return result


def highest_expense(data):
    if not data:
        return 0

    return max(row[4] for row in data)


def average_expense(data):
    if not data:
        return 0

    return round(total_expense(data) / len(data), 2)

def top_category(category_data):
    if not category_data:
        return "No Data", 0

    category = max(category_data, key=category_data.get)
    amount = category_data[category]

    return category, amount