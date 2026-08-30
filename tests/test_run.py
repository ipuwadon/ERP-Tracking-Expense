from finance.manager import FinanceManager

def run_demo():
    fm = FinanceManager()

    fm.add_saving("Bank A", 5000)
    fm.add_saving("Investment", 3000)
    fm.add_saving("Bank B", 2000)
    print("Summary1: ", fm.summary())

    fm.transfer("Bank B", "Bank A", 1000)
    print("Summary2: ", fm.summary())

    fm.add_expense("Travel", 2000, "Bank A", "Leisure")
    fm.add_expense("Dinner", 500, "Bank B", "Food")
    print("Summary3: ", fm.summary())

    fm.add_saving("Bank C", 3600)
    print("Summary4: ", fm.summary())

    fm.add_expense("Buy Mouse", 800, "Bank A", "Work")
    print("Summary5: ", fm.summary())

if __name__ == "__main__":
    run_demo()