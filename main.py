import csv
import datetime

DATA_FILE = "data.csv"

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

def main():
    while True:
        print("\n Personal Finance Tacker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            add_expense(amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    main()