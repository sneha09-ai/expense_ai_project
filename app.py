from flask import Flask, render_template, request, redirect, Response, session
import datetime
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from database import (
    init_db,
    add_expense,
    get_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense,
    add_user,
    get_user
)

from advisor import give_advice
from analytics import (
    total_expense,
    category_wise,
    monthly_wise,
    highest_expense,
    average_expense,
    top_category
)
from ml_model import predict_expense
from budget import budget_status, category_budget_status

app = Flask(__name__)
app.secret_key = "expense_tracker_secret"

init_db()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            add_user(username, password)
            return redirect("/")
        except:
            return "❌ Username already exists or error occurred"

    return render_template("register.html")
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username, password)

        if user:
            session["logged_in"] = True
            return redirect("/dashboard")
        else:
            return "❌ Invalid Username or Password"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")

    search = request.args.get("search", "")
    date_filter = request.args.get("date_filter", "all")

    expenses = get_expenses()

    today = datetime.date.today()
    current_month = today.strftime("%Y-%m")

    if date_filter == "today":
        expenses = [
            e for e in expenses
            if str(e[1]) == str(today)
        ]

    elif date_filter == "month":
        expenses = [
            e for e in expenses
            if str(e[1]).startswith(current_month)
        ]
    

    if search:
        expenses = [
            e for e in expenses
            if search.lower() in e[2].lower() or search.lower() in e[3].lower()
        ]
    sort_by = request.args.get("sort_by", "default")

    if sort_by == "amount_low":
        expenses = sorted(expenses, key=lambda e: e[4])

    elif sort_by == "amount_high":
        expenses = sorted(expenses, key=lambda e: e[4], reverse=True)

    elif sort_by == "latest":
        expenses = sorted(expenses, key=lambda e: e[1], reverse=True)

    elif sort_by == "oldest":
        expenses = sorted(expenses, key=lambda e: e[1])

    total = total_expense(expenses)
    category_data = category_wise(expenses)
    top_cat, top_amount = top_category(category_data)
    category_budget_data = category_budget_status(category_data)
    monthly_data = monthly_wise(expenses)
    advice = give_advice(total, category_data)
    prediction = predict_expense(expenses)
    highest = highest_expense(expenses)
    average = average_expense(expenses)
    total_entries = len(expenses)

    monthly_budget, remaining_budget, used_percent, budget_message = budget_status(total)

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total=total,
        highest=highest,
        average=average,
        total_entries=total_entries,
        advice=advice,
        category_data=category_data,
        top_cat=top_cat,
        top_amount=top_amount,
        category_budget_data=category_budget_data,
        monthly_data=monthly_data,
        prediction=prediction,
        sort_by=sort_by,
        search=search,
        date_filter=date_filter,
        monthly_budget=monthly_budget,
        remaining_budget=remaining_budget,
        used_percent=used_percent,
        budget_message=budget_message
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if not session.get("logged_in"):
        return redirect("/")

    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        date = datetime.date.today()

        add_expense(date, name, category, amount)
        return redirect("/dashboard")

    return render_template("add_expense.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if not session.get("logged_in"):
        return redirect("/")

    expense = get_expense_by_id(id)

    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        amount = float(request.form["amount"])

        update_expense(id, name, category, amount)
        return redirect("/dashboard")

    return render_template("edit_expense.html", expense=expense)


@app.route("/delete/<int:id>")
def delete(id):
    if not session.get("logged_in"):
        return redirect("/")

    delete_expense(id)
    return redirect("/dashboard")


@app.route("/export")
def export_csv():
    if not session.get("logged_in"):
        return redirect("/")

    expenses = get_expenses()

    def generate():
        yield "ID,Date,Name,Category,Amount\n"
        for e in expenses:
            yield f"{e[0]},{e[1]},{e[2]},{e[3]},{e[4]}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=expenses.csv"}
    )


@app.route("/export_pdf")
def export_pdf():
    if not session.get("logged_in"):
        return redirect("/")

    expenses = get_expenses()
    total = total_expense(expenses)
    category_data = category_wise(expenses)
    top_cat, top_amount = top_category(category_data)
    advice = give_advice(total, category_data)
    prediction = predict_expense(expenses)

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(160, 750, "Smart Expense Tracker Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 710, f"Total Expense: Rs. {total}")
    pdf.drawString(50, 690, "AI Advice:")

    y_advice = 670
    for item in advice:
        pdf.drawString(70, y_advice, f"- {item}")
        y_advice -= 18

    pdf.drawString(50, y_advice - 10, f"Predicted Next Expense: Rs. {prediction}")

    y = y_advice - 50

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "ID")
    pdf.drawString(90, y, "Date")
    pdf.drawString(180, y, "Name")
    pdf.drawString(300, y, "Category")
    pdf.drawString(420, y, "Amount")

    y -= 20
    pdf.setFont("Helvetica", 10)

    for e in expenses:
        pdf.drawString(50, y, str(e[0]))
        pdf.drawString(90, y, str(e[1]))
        pdf.drawString(180, y, str(e[2]))
        pdf.drawString(300, y, str(e[3]))
        pdf.drawString(420, y, f"Rs. {e[4]}")
        y -= 20

        if y < 50:
            pdf.showPage()
            y = 750

    pdf.save()
    buffer.seek(0)

    return Response(
        buffer,
        mimetype="application/pdf",
        headers={"Content-Disposition": "attachment;filename=expense_report.pdf"}
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)