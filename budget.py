def budget_status(total):
    monthly_budget = 10000

    remaining = monthly_budget - total
    used_percent = (total / monthly_budget) * 100

    if total > monthly_budget:
        message = "⚠️ You crossed your monthly budget!"
    elif total >= monthly_budget * 0.8:
        message = "⚠️ You used more than 80% of your budget."
    else:
        message = "✅ Your spending is under control."

    return monthly_budget, remaining, round(used_percent, 2), message


def category_budget_status(category_data):
    category_budgets = {
        "Food": 3000,
        "Travel": 2000,
        "Shopping": 4000,
        "Bills": 3000,
        "Other": 2000
    }

    result = {}

    for category, spent in category_data.items():
        budget = category_budgets.get(category, 2000)
        remaining = budget - spent

        if spent > budget:
            message = f"⚠️ {category} budget exceeded by ₹{spent - budget}"
        else:
            message = f"✅ ₹{remaining} remaining for {category}"

        result[category] = {
            "budget": budget,
            "spent": spent,
            "remaining": remaining,
            "message": message
        }

    return result