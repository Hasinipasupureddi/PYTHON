import tkinter as tk# tool kit for creating the interfcace
from tkinter import messagebox, ttk#for showing alert#themed widgets
import json#to load or save data from JSON file
from datetime import datetime#to import date and time
import matplotlib.pyplot as plt#to display charts
'''File Handling Functions'''

FILE_NAME = "expenses.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"transactions": []}
# loads data from JSON file and returns an empty list of transactions if file not found
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
        #saves updated data  back into the file

root = tk.Tk()
root.title("Personal Expense Tracker")
#creates a main window and sets title
frame = tk.Frame(root)
frame.pack(pady=20)
#adds a frame(container) to hold widgets with padding(adding extra data)

amount_var = tk.DoubleVar()
category_var = tk.StringVar()
type_var = tk.StringVar(value="expense")
#tkinter variable to store user input
def add_transaction():
    amount = amount_var.get()
    category = category_var.get()
    type_ = type_var.get()
#collects input values
    if not amount or not category:
        messagebox.showwarning("Input Error", "Please fill in both amount and category.")
        return
#validates them
    data = load_data()
    transaction = {
        "amount": amount,
        "category": category,
        "type": type_,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#adds time and date
    }
    data["transactions"].append(transaction)
    save_data(data)
    load_transactions()
    update_balance()
#saves and refreshes the table and balance
def load_transactions(transactions=None):
    for row in tree.get_children():
        tree.delete(row)
#clears the current table
    data = load_data()
    transactions = transactions if transactions else data["transactions"]
#Loads all or filtered transactions
    for t in transactions:
        tree.insert("", "end", values=(t["date"], t["type"].capitalize(), t["category"], f"Rs.{t['amount']}"))
#insert them into the tree view
def update_balance():
    data = load_data()
    balance = sum(t['amount'] if t['type'] == 'income' else -t['amount'] for t in data["transactions"])
    balance_label.config(text=f"Balance: Rs.{balance}")
#sums up income and subtracts expenses   
def delete_transaction():
    selected = tree.focus()#gets selected row
    if not selected:
        messagebox.showwarning("Select Entry", "Please select a transaction to delete.")
        return

    values = tree.item(selected, "values")
    date = values[0]
    amount = float(values[3].replace("Rs.", ""))

    data = load_data()
    transactions = data["transactions"]
    for i, t in enumerate(transactions):
        if t["date"] == date and t["amount"] == amount:
            del transactions[i]
            break
#matches date + amount to identify the transaction
    save_data(data)
    load_transactions()
    update_balance()
    messagebox.showinfo("Deleted", "Transaction deleted.")
#deletesthe transaction and refreshes the table
def edit_transaction():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select Entry", "Please select a transaction to edit.")
        return

    values = tree.item(selected, "values")
    old_date = values[0]
    old_amount = float(values[3].replace("Rs.", ""))
    old_category = values[2]
    old_type = values[1].lower()
#gets selected row and current values
    new_amount = amount_entry.get()
    new_category = category_entry.get()
    new_type = type_var.get()

    if not new_amount or not new_category:
        messagebox.showwarning("Input Error", "Please fill in both amount and category.")
        return

    data = load_data()
    transactions = data["transactions"]

    for t in transactions:
        if t["date"] == old_date and t["amount"] == old_amount:
            t["amount"] = float(new_amount)
            t["category"] = new_category
            t["type"] = new_type
            break
#uses input from entry fields to update
    save_data(data)
    load_transactions()
    update_balance()

    messagebox.showinfo("Updated", "Transaction updated successfully!")
#saves and reloads data
def filter_transactions():
    filter_window = tk.Toplevel(root)#opens a new window from the main tkinter root
    filter_window.title("Filter Transactions")#sets title for window

    tk.Label(filter_window, text="Filter by:").grid(row=0, column=0)
    filter_type = ttk.Combobox(filter_window, values=["Category", "Date"], state="readonly")
    filter_type.grid(row=0, column=1)
    filter_type.set("Category")
#user to select the filter type either category or date ,deafulting to category
    filter_entry = tk.Entry(filter_window)
    filter_entry.grid(row=1, column=0, columnspan=2)
#to input filter value
    def apply_filter():
        data = load_data()#fetches all the saved data
        filter_value = filter_entry.get()
        filter_by = filter_type.get()

        filtered = []

        if filter_by == "Category":
            filtered = [t for t in data["transactions"] if filter_value.lower() in t["category"].lower()]
        elif filter_by == "Date":
            filtered = [t for t in data["transactions"] if filter_value in t["date"]]

        load_transactions(filtered)
#displays the filtered transactions
    tk.Button(filter_window, text="Apply Filter", command=apply_filter).grid(row=2, column=0, columnspan=2, pady=5)
#adds a button labeled "apply filter"
def show_charts():
    data = load_data()
    categories = {}
    for t in data["transactions"]:
        if t["type"] == "expense":#  filters only expense not income
            if t["category"] in categories:
                categories[t["category"]] += t["amount"]#if the category already exists add current transaction amount to total
            else:
                categories[t["category"]] = t["amount"]#if does not intiliaze it with cureent amount

    if not categories:
        messagebox.showwarning("No Expenses", "No expenses to display in chart.")
        return
#if no expenses were found show a warning message
    labels = categories.keys()#category names
    sizes = categories.values()# total amount for category 

    fig, ax = plt.subplots()#creates a figure and axes object for plotting
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#sizes:amount,lables:category names,autopct:format for displaying percentage
#startangle:rotates chart so first slice starts from top
    ax.axis('equal')#ensures it's a cicle not a ellipse
    plt.title("Expenses by Category")
    plt.show()          # Show the chart
    plt.close(fig)      # ✅ Close it after showing
  #sets a title and displays it in a new window
# Entry for Amount
amount_label = tk.Label(frame, text="Amount:")#creates a lbel that says "amount" and place it inside a frame
amount_label.grid(row=0, column=0, sticky="w")#places in row=0 and column=0 
amount_entry = tk.Entry(frame, textvariable=amount_var)
amount_entry.grid(row=0, column=1)

# Entry for Category
category_label = tk.Label(frame, text="Category:")
category_label.grid(row=1, column=0, sticky="w")
category_entry = tk.Entry(frame, textvariable=category_var)
category_entry.grid(row=1, column=1)

# Radio Buttons for Type (Income or Expense)
tk.Radiobutton(frame, text="Income", variable=type_var, value="income").grid(row=2, column=0)
tk.Radiobutton(frame, text="Expense", variable=type_var, value="expense").grid(row=2, column=1)

# Buttons for Add, Delete, Edit, Filter, Show Chart
tk.Button(frame, text="Add Transaction", command=add_transaction).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Delete Selected", command=delete_transaction).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Edit Selected", command=edit_transaction).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Filter", command=filter_transactions).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(frame, text="Show Chart", command=show_charts).grid(row=7, column=0, columnspan=2, pady=5)

# Table to show transactions
columns = ("Date", "Type", "Category", "Amount")#column names
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=8, column=0, columnspan=2)#placing tree view widget

# Balance Label
balance_label = tk.Label(frame, text="Balance: Rs.0")
balance_label.grid(row=9, column=0, columnspan=2, pady=10)

# Load initial data
load_transactions()
update_balance()

root.mainloop()
'''How It Works:
Add Transaction: Adds income or expense to the tracker.

Delete/Edit Transaction: Select a row from the table and delete or edit it.

Filter: Filter by category or date.

Show Chart: Shows a pie chart for expenses by category.

Next Steps:
Run the App and test each feature.

You can improve it by adding additional charts or even more filters (like by month).

'''
