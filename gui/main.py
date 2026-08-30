import tkinter as tk
from gui.views import ERPApp

def main():
    root = tk.Tk()
    app = ERPApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()