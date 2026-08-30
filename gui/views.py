import tkinter as tk
from tkinter import ttk, messagebox
from finance.manager import FinanceManager
from gui.widgets import StyledTreeview, StatusBar

class ERPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker ERP")
        self.root.geometry("900x600")

        # Backend
        self.fm = FinanceManager("data/finance.json")

        # Menu bar
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Expense Tracker ERP v1.0"))
        menubar.add_cascade(label="Help", menu=help_menu)
        root.config(menu=menubar)

        # Notebook (Tabs)
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        # Accounts Tab
        accounts_frame = ttk.Frame(notebook)
        notebook.add(accounts_frame, text="Accounts")
        self.accounts_table = StyledTreeview(accounts_frame, ["Account", "Balance"])
        self.accounts_table.pack(fill="both", expand=True, padx=10, pady=10)
        toolbar_acc = ttk.Frame(accounts_frame)
        toolbar_acc.pack(fill="x")
        ttk.Button(toolbar_acc, text="Refresh", command=self.show_accounts).pack(side="left", padx=5)
        ttk.Button(toolbar_acc, text="Add Account", command=self.open_add_account).pack(side="left", padx=5)

        # Expenses Tab
        expenses_frame = ttk.Frame(notebook)
        notebook.add(expenses_frame, text="Expenses")
        self.expenses_table = StyledTreeview(expenses_frame, ["Item", "Amount", "Account", "Category"])
        self.expenses_table.pack(fill="both", expand=True, padx=10, pady=10)
        toolbar_exp = ttk.Frame(expenses_frame)
        toolbar_exp.pack(fill="x")
        ttk.Button(toolbar_exp, text="Refresh", command=self.show_expenses).pack(side="left", padx=5)
        ttk.Button(toolbar_exp, text="Add Expense", command=self.open_add_expense).pack(side="left", padx=5)

        # Status Bar
        self.status = StatusBar(root)
        self.status.pack(fill="x")

        # Initial load
        self.show_accounts()
        self.show_expenses()

    def show_accounts(self):
        balances = self.fm.summary()
        rows = [(acc, f"{bal:.2f}") for acc, bal in balances.items()]
        self.accounts_table.update_rows(rows)
        self.status.set("Accounts refreshed")

    def show_expenses(self):
        expenses = self.fm.get_expenses()
        rows = [(exp["item"], exp["amount"], exp["account"], exp["category"]) for exp in expenses]
        self.expenses_table.update_rows(rows)
        self.status.set("Expenses refreshed")

    def open_add_account(self):
        win = tk.Toplevel(self.root)
        win.title("Add Account")
        win.geometry("400x200")

        tk.Label(win, text="Account Name").grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(win, width=30)
        name_entry.grid(row=0, column=1)

        tk.Label(win, text="Initial Balance").grid(row=1, column=0, padx=10, pady=5)
        balance_entry = tk.Entry(win, width=30)
        balance_entry.grid(row=1, column=1)

        def add_account():
            try:
                name = name_entry.get()
                balance = float(balance_entry.get())
                self.fm.add_account(name, balance)
                self.show_accounts()
                self.status.set(f"Account {name} added")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid balance")

        ttk.Button(win, text="Add", command=add_account).grid(row=2, columnspan=2, pady=10)

    def open_add_expense(self):
        win = tk.Toplevel(self.root)
        win.title("Add Expense")
        win.geometry("500x300")

        tk.Label(win, text="Item").grid(row=0, column=0, padx=10, pady=5)
        item_entry = tk.Entry(win, width=40)
        item_entry.grid(row=0, column=1)

        tk.Label(win, text="Amount").grid(row=1, column=0, padx=10, pady=5)
        amount_entry = tk.Entry(win, width=40)
        amount_entry.grid(row=1, column=1)

        tk.Label(win, text="Account").grid(row=2, column=0, padx=10, pady=5)
        account_combo = ttk.Combobox(win, values=list(self.fm.data["accounts"].keys()), width=37)
        account_combo.grid(row=2, column=1)

        tk.Label(win, text="Category").grid(row=3, column=0, padx=10, pady=5)
        category_entry = tk.Entry(win, width=40)
        category_entry.grid(row=3, column=1)

        def add_expense():
            try:
                item = item_entry.get()
                amount = float(amount_entry.get())
                account = account_combo.get()
                category = category_entry.get()
                self.fm.add_expense(item, amount, account, category)
                self.show_expenses()
                self.status.set(f"Expense {item} added")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")

        ttk.Button(win, text="Add", command=add_expense).grid(row=4, columnspan=2, pady=10)