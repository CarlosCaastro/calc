import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("300x350")
        self.root.resizable(False, False)

        self.calculator = Calculator()

        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()

        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 16), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2),
            ("\u221A", 1, 4), ("x^y", 2, 4), ("log", 3, 4), ("n!", 4, 4),
        ]

        for btn_text, row, col in buttons:
            btn = tk.Button(self.root, text=btn_text, font=("Arial", 16), command=lambda t=btn_text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        equals_btn = tk.Button(self.root, text="=", font=("Arial", 16), command=self.calculate_result)
        equals_btn.grid(row=5, column=3, columnspan=2, padx=10, pady=10, ipady=5, sticky="nsew")

        clear_btn = tk.Button(self.root, text="C", font=("Arial", 16), command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=3, padx=10, pady=10, ipady=5, sticky="nsew")

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_value = self.result_var.get()
        if value == "=":
            self.calculate_result()
        elif value == "\u221A":
            self.result_var.set("math.sqrt(" + current_value + ")")
        elif value == "x^y":
            self.result_var.set(current_value + "**")
        elif value == "log":
            self.result_var.set("math.log(" + current_value + ", 10)")
        elif value == "n!":
            self.result_var.set("math.factorial(" + current_value + ")")
        else:
            self.result_var.set(current_value + value)

    def calculate_result(self):
        try:
            result = self.calculator.evaluate_expression(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Erro")

    def clear(self):
        self.result_var.set("")

def main():
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
