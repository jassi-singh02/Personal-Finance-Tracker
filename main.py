import csv
import datetime

DATA_FILE = "data.csv"
CATEGORIES = ["Food", "Rent", "Travel", "Entertainment", "Other"]

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


def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Category")
        print("4. Delete Category")
        print("5. Quit")

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
            break

        else:
            print("Invalid input, try again.")
            #just checking it works

if __name__ == "__main__":
    main()