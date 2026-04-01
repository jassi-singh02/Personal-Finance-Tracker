import csv
import datetime
import matplotlib.pyplot as plt

DATA_FILE = "data.csv"
CATEGORIES = ["Food", "Rent", "Travel", "Entertainment", "Other"]

"check in + 12"

def add_expense(amount, category, description=""):
    date = datetime.date.today().isoformat()
    with open(DATA_FILE, mode = "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
        print(f"Added expense: ${amount} | {category} | {description}")

def view_expenses():
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            print("Date       | Amount    | Category    | Description")
            print("-"*50)
            for row in reader:
                print(f"{row[0]:10} | ${row[1]:6} | {row[2]:13} | {row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def add_categories():
    "Function to add categories to list if needed"
    new_category = input("Enter a new category: ").strip()
    cleaned_categories = [category.lower().strip() for category in CATEGORIES]

    if new_category.lower() not in cleaned_categories:
        CATEGORIES.append(new_category.strip())
        print(f"Added new category: {new_category}")
    else:
        print("Category already exists.")

def delete_categories():
    "Function to delete categories from list if needed"
    deleted_category = input("Which category to delete: ").strip()
    cleaned_categories = [category.lower().strip() for category in CATEGORIES]

    if deleted_category.lower() in cleaned_categories:
        # find the actual category in original list and remove it
        for cat in CATEGORIES:
            if cat.lower().strip() == deleted_category.lower():
                CATEGORIES.remove(cat)
                print(f"Deleted category: {cat}")
                break
    else:
        print("Category does not exist.")

def show_dashboard():
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

        if not expenses:
            print("No data to display in dashboard.")
            return

        # Parse data
        dates = []
        amounts = []
        categories = []
        for row in expenses:
            date, amount, category, description = row
            dates.append(datetime.datetime.fromisoformat(date))
            amounts.append(float(amount))
            categories.append(category)

        # --- Pie Chart (expenses by category) ---
        category_totals = {}
        for cat, amt in zip(categories, amounts):
            category_totals[cat] = category_totals.get(cat, 0) + amt

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)  # 1 row, 2 cols, first chart
        plt.pie(category_totals.values(), labels=category_totals.keys(), autopct="%1.1f%%")
        plt.title("Expenses by Category")

        # --- Line Chart (expenses over time) ---
        plt.subplot(1, 2, 2)  # second chart
        plt.plot(dates, amounts, marker="o")
        plt.title("Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Category")
        print("4. Delete Category")
        print("5. Show Dashboard")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))

            print("\nAvailable categories:")
            for i, cat in enumerate(CATEGORIES, start=1):
                print(f"{i}. {cat}")
            cat_choice = int(input("Pick a category number: "))
            category = CATEGORIES[cat_choice - 1]

            description = input("Enter description (optional): ")
            add_expense(amount, category, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            add_categories()

        elif choice == "4":
            delete_categories()

        elif choice == "5":
            show_dashboard()

        elif choice == "6":
            break

        else:
            print("Invalid input, try again.")
            #just checking it works

if __name__ == "__main__":
    main()