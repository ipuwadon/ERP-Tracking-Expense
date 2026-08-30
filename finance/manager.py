from .storage import Storage

class FinanceManager:
    def __init__(self, storage_file="data/finance.json"):
        self.storage = Storage(storage_file)
        self.data = self.storage.load()

    def add_saving(self, account, amount):
        self.data["accounts"].setdefault(account, 0)
        self.data["accounts"][account] += amount
        self.storage.save(self.data)

    def add_expense(self, item, amount, account, category):
        if account not in self.data["accounts"]:
            raise ValueError("Account does not exist")

        self.data["accounts"][account] -= amount
        self.data["expenses"].append({
            "item": item,
            "amount": amount,
            "account": account,
            "category": category
        })
        self.storage.save(self.data)

    def transfer(self, from_acc, to_acc, amount):
        self.data["accounts"][from_acc] -= amount
        self.data["accounts"][to_acc] += amount
        self.storage.save(self.data)

    def summary(self):
        return self.data["accounts"]

    def get_expenses(self):
        return self.data["expenses"]

    def edit_expense(self, index: int, item=None, amount=None, account=None, category=None):
        try:
            exp = self.data["expenses"][index]

            old_account = exp["account"]
            old_amount = exp["amount"]
            if old_account in self.data["accounts"]:
                self.data["accounts"][old_account] += old_amount

            if item: exp["item"] = item
            if amount: exp["amount"] = amount
            if account: exp["account"] = account
            if category: exp["category"] = category

            new_account = exp["account"]
            new_amount = exp["amount"]
            if new_account in self.data["accounts"]:
                self.data["accounts"][new_account] -= new_amount

            self.storage.save(self.data)
        except IndexError:
            raise ValueError("Expense not found")

    def remove_expense(self, index: int):
        try:
            exp = self.data["expenses"].pup(index)

            account = exp["account"]
            amount = exp["amount"]

            if account in self.data["accounts"]:
                self.data["accounts"][account] += amount

            self.storage.save(self.data)
        except IndexError:
            raise ValueError("Expense not found")

    def remove_account(self, account: str):
        if account in self.data["accounts"]:
            if self.data["accounts"][account] == 0:
                del self.data["accounts"][account]
                self.storage.save(self.data)
            else:
                raise ValueError("Account balance must be zero before removal")
