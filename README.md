# Expense Tracker (Python)

A simple finance management tool with **CLI + JSON storage**.  
Users can add savings accounts, record expenses, transfer money between accounts, and view summaries of their financial state.

---

## 🚀 Features
- Add multiple savings accounts (Bank, Salary, Investment, etc.)
- Record expenses linked to specific accounts
- Transfer money between accounts
- Summarize current balances and total savings
- JSON-based storage for persistence
- CLI interface with Typer
- Colorful output using Rich
- Unit tests with Pytest

---

## 📂 Project Structure
expense_tracker/
├── finance/        # Core logic
├── cli/            # CLI interface
├── data/           # JSON storage
├── tests/          # Unit tests
├── requirements.txt
└── README.md


---

## ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense_tracker.git
   cd expense_tracker

2. Create and activate a virtual environment:
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

---

🖥 Usage
Run commands from the CLI:
python cli/main.py add-saving BankA 5000
python cli/main.py add-expense Travel 2000 BankA Leisure
python cli/main.py transfer BankB BankA 1000
python cli/main.py summary

---

🛠 Roadmap
- Week 1: CLI + JSON storage
- Week 2: Enhance CLI with Rich
- Week 3: Integrate MySQL backend
- Week 4: Add Tkinter GUI
- Week 5: Reports, charts, optional cloud sync


---

✨ This README gives you a professional structure and makes it easy for anyone (including future you) to understand the project quickly.  