# ERP Tracking Expense

An ERP‑style Expense Tracker built with **Python + Tkinter**.  
This project provides a clean, modular interface for managing accounts and expenses, designed to look and feel like a lightweight ERP system.

---

## 🚀 Features
- ERP‑style **tabbed interface** (Accounts, Expenses).
- **Styled tables** with alternating row colors and bold headers.
- **Popups for forms** (Add Account, Add Expense).
- **Toolbar buttons** for Refresh / Add actions.
- **Status bar** showing last update.
- **Menu bar** (File, Help).

---

## 📂 Project Structure
expense_tracker/
- cli/            # Command-line interface
   - main.py
- data/           # Data storage
   - finance.json
- env/            # Virtual environment (excluded via .gitignore)
- finance/        # Core business logic
   - manager.py   # Handles accounts & expenses
   - storage.py   # JSON storage utilities
- gui/            #ERP-style graphical interface
   - main.py      # Entry point
   - views.py     # Layout & logic (tabs, popups)
   - widgets.py   # Styled reusable components
- tests/          # Unit Tests
   - test_run.py

- .gitignore      # Excludes env/, __pycache__, temp files
- prepare-project.MD # Setup notes
- README.md       # Project documentation
- requirements.txt # Dependencies

---

## 🖥 Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/ipuwadon/ERP-Tracking-Expense.git
   cd ERP-Tracking-Expense
2. Create and activate a virtual environment:
   python -m venv env
   .\env\Scripts\activate
3. Install dependencies (if any):
   pip install -r requirements.txt
4. Run the app:
   python -m gui.main
   
---

📸 Screenshots
Here you can showcase the interface with examples:

Accounts Tab
<img width="895" height="647" alt="image" src="https://github.com/user-attachments/assets/60559bfc-a2b2-4ec0-88c0-98da46e7b657" />

<img width="422" height="238" alt="image" src="https://github.com/user-attachments/assets/07f53f4c-14cf-41c2-bdc4-2f192e887d4e" />

Expenses Tab
<img width="892" height="647" alt="image" src="https://github.com/user-attachments/assets/968bbef8-04c6-47f6-aed7-68e5bdbc1e3d" />

<img width="515" height="343" alt="image" src="https://github.com/user-attachments/assets/74c3ec2f-1d0b-4065-873c-9377d77e8df2" />

---

🛠 Future Enhancements
- Reports tab with charts (expenses by category).
- Edit/Delete functionality for accounts and expenses.
- Export to CSV/Excel.

---

📜 License
MIT License — feel free to use and adapt.

---
