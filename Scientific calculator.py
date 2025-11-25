import tkinter as tk
import math

class Calculator:
    def __init__(self, window):
        self.window = window
        window.title("Scientific Calculator")
        window.resizable(False, False)

        self.bg = "#202020"
        self.display_bg = "#1E1E1E"
        self.num_bg = "#2D2D2D"
        self.op_bg = "#4C4C4C"
        self.sci_bg = "#333333"
        self.equal_bg = "#0184FE"
        self.text_color = "white"

        window.configure(bg=self.bg)

        self.expression = ""

        self.label = tk.Label(
            window, text="0", font=("Segoe UI", 35),
            bg=self.display_bg, fg=self.text_color,
            anchor="e", padx=15
        )
        self.label.grid(row=0, column=0, columnspan=6, sticky="we", pady=5)

        self.buttons = [
            ["sin", "cos", "tan", "log", "xʸ", "exp"],
            ["7", "8", "9", "÷", "sqrt", "1/x"],
            ["4", "5", "6", "×", "^2", "π"],
            ["1", "2", "3", "-", "x!", "10ˣ"],
            ["0", ".", "AC", "+/-", "%", "="]
        ]

        self.create_buttons()

        window.update()
        w, h = window.winfo_width(), window.winfo_height()
        sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
        window.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def create_buttons(self):
        for r, row in enumerate(self.buttons):
            for c, value in enumerate(row):
                btn = tk.Button(
                    self.window, text=value, font=("Segoe UI", 18),
                    fg=self.text_color, width=5, height=2,
                    bd=0,
                    command=lambda v=value: self.clicked(v)
                )

                if value in ["+", "-", "×", "÷"]:
                    btn.configure(bg=self.op_bg)
                elif value == "=":
                    btn.configure(bg=self.equal_bg)
                elif value in ["sin", "cos", "tan", "log", "sqrt", "1/x", "x!", "xʸ", "10ˣ", "exp", "^2", "π"]:
                    btn.configure(bg=self.sci_bg)
                elif value in ["AC", "+/-", "%"]:
                    btn.configure(bg=self.op_bg)
                else:
                    btn.configure(bg=self.num_bg)

                btn.grid(row=r+1, column=c, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.window.columnconfigure(i, weight=1)

    def update_display(self, text):
        self.label.config(text=text)

    def clicked(self, value):
        text = self.label["text"]

        if value == "AC":
            self.expression = ""
            self.update_display("0")
            return

        if value == "+/-":
            try:
                self.update_display(str(-float(text)))
            except:
                self.update_display("Error")
            return

        if value == "%":
            try:
                self.update_display(str(float(text) / 100))
            except:
                self.update_display("Error")
            return

        if value == "π":
            self.update_display(str(math.pi))
            return

        try:
            num = float(text)

            if value == "sin":
                self.update_display(str(math.sin(math.radians(num))))
                return
            if value == "cos":
                self.update_display(str(math.cos(math.radians(num))))
                return
            if value == "tan":
                self.update_display(str(math.tan(math.radians(num))))
                return
            if value == "log":
                self.update_display(str(math.log10(num)))
                return
            if value == "sqrt":
                self.update_display(str(math.sqrt(num)))
                return
            if value == "1/x":
                self.update_display(str(1 / num))
                return
            if value == "x!":
                self.update_display(str(math.factorial(int(num))))
                return
            if value == "^2":
                self.update_display(str(num ** 2))
                return
            if value == "10ˣ":
                self.update_display(str(10 ** num))
                return
            if value == "exp":
                self.update_display(str(math.exp(num)))
                return
        except:
            pass  

        if value == "xʸ":
            self.expression += text + "**"
            self.update_display("0")
            return

        if value in ["+", "-", "×", "÷"]:
            op = value.replace("×", "*").replace("÷", "/")
            self.expression += text + op
            self.update_display("0")
            return

        if value == "=":
            self.expression += text
            try:
                result = eval(self.expression)
                self.update_display(str(result))
            except:
                self.update_display("Error")
            self.expression = ""
            return

        if text == "0" and value not in ["." ]:
            self.update_display(value)
        else:
            self.update_display(text + value)


window = tk.Tk()
Calculator(window)
window.mainloop()
