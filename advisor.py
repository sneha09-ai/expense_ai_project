def give_advice(total, category_data):
    advice_list = []

    if total < 3000:
        advice_list.append("✅ Excellent! Your spending is under control.")
    elif total < 6000:
        advice_list.append("🙂 Your spending is okay, but keep tracking it.")
    elif total < 10000:
        advice_list.append("⚠️ Your monthly spending is increasing.")
    else:
        advice_list.append("🚨 High spending detected. Try reducing unnecessary expenses.")

    food = category_data.get("Food", 0)
    travel = category_data.get("Travel", 0)
    shopping = category_data.get("Shopping", 0)

    if food > 3000:
        advice_list.append("🍔 Food spending is too high. Try reducing outside food.")

    if travel > 2000:
        advice_list.append("✈️ Travel budget exceeded. Try using cheaper transport.")

    if shopping > 4000:
        advice_list.append("🛍️ Shopping expenses are increasing. Avoid unnecessary purchases.")

    return advice_list
