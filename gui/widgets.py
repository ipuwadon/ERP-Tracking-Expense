import tkinter as tk
from tkinter import ttk

class StyledTreeview(ttk.Treeview):
    def __init__(self, parent, columns):
        super().__init__(parent, columns=columns, show="headings")
        for col in columns:
            self.heading(col, text=col, anchor="center")
            self.column(col, anchor="center", width=150)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", rowheight=25)
        style.map("Treeview", background=[("selected", "#d0e0f0")])
        self.tag_configure("oddrow", background="#f9f9f9")
        self.tag_configure("evenrow", background="#ffffff")

    def update_rows(self, data):
        for row in self.get_children():
            self.delete(row)
        for i, values in enumerate(data):
            tag = "oddrow" if i % 2 else "evenrow"
            self.insert("", "end", values=values, tags=(tag,))

class StatusBar(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Ready", anchor="w")
    def set(self, text):
        self.config(text=text)