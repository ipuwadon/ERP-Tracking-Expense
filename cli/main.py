import typer
from finance.manager import FinanceManager
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
fm = FinanceManager("data/finance.json")
console = Console()

@app.command()
def add_saving(account: str, amount: float):
    fm.add_saving(account, amount)
    #typer.echo(f"Added {amount} to {account}")
    print(f"[green]Added {amount} to {account}[/green]")

@app.command()
def add_expense(item: str, amount: float, account: str, category: str):
    fm.add_expense(item, amount, account, category)
    #typer.echo(f"Expanse '{item}' of {amount} from {account} ({category}) recorded.")
    print(f"[red]Expanse '{item}' of {amount} from {account} ({category}) recorded.[/red]")

@app.command()
def transfer(from_acc: str = typer.Option(..., help="Source account"), 
             to_acc: str = typer.Option(..., help="Destination account"), 
             amount: float = typer.Option(..., help="Amount to transfer")):
    fm.transfer(from_acc, to_acc, amount)
    #typer.echo(f"Transferred {amount} from {from_acc} to {to_acc}")
    print(f"[cyan underline]Transferred {amount} from {from_acc} to {to_acc}[/cyan underline]")

@app.command()
def summary():
    table = Table(title="Account Summary")

    table.add_column("Account", style="cyan", no_wrap=True)
    table.add_column("Balance", style="green", justify="right")

    balances = fm.summary()
    total = 0
    #typer.echo("Accounts:")
    for acc, bal in balances.items():
        table.add_row(acc, f"{bal:.2f}")
        total += bal
        #typer.echo(f" {acc}: {bal}")

    #typer.echo(f"Total: {sum(balances.values())}")
    table.add_row("----", "----")
    table.add_row("[bold]Total[/bold]", f"[bold]{total:.2f}[/bold]")

    console.print(table)

@app.command()
def list_expenses(
    category: str = typer.Option(None, help="Filter by category"),
    account: str = typer.Option(None, help="Filter by account")

):
    expenses = fm.get_expenses()
    if category:
        expenses = [exp for exp in expenses if exp["category"].lower() == category.lower()]
    if account:
        expenses = [exp for exp in expenses if exp["account"].lower() == account.lower()]

    table = Table(title="Expenses")

    table.add_column("Item", style="cyan")
    table.add_column("Amount", style="green", justify="right")
    table.add_column("Account", style="magenta")
    table.add_column("Category", style="yellow")

    total = 0
    for exp in expenses:
        total += exp["amount"]
        table.add_row(
            exp["item"],
            f"{exp['amount']:.2f}",
            exp["account"],
            exp["category"]
        )

    table.add_row("----", "----", "----", "----")
    table.add_row("[bold]Total[/bold]", f"[bold]{total:.2f}[/bold]", "-", "-")
    console.print(table)

@app.command()
def edit_expense(index: int, item: str = None, amount: float = None, account: str = None, category: str = None):
    fm.edit_expense(index, item, amount, account, category)
    print(f"[green]Expense {index} updated.[/green]")

@app.command()
def remove_expense(index: int):
    fm.remove_expense(index)
    print(f"[red]Expense {index} removed.[/red]")

@app.command()
def remove_account(account: str):
    fm.remove_account(account)
    print(f"[red]Account {account} removed.[/red]")


if __name__ == "__main__":
    app()