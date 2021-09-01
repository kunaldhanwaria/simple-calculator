import tkinter as tk
from math import sqrt

class Calculator():
    expression = ""

    def __init__(self, window):
        self.input_field = tk.Entry(window, width=48, border=8)
        self.input_field.grid(row=0, column=0,columnspan=4, padx=10, pady=10)
        self.input_field.focus_set()

        #Creating Frame for placing buttons
        self.frame = tk.Frame(window, padx=5, pady=5, bg="#808080")
        self.frame.grid(row=1, column=0, columnspan=4, padx=5, pady=10)

        #Creating Number Buttons (0 to 9)
        button_1 = tk.Button(self.frame, text="1", command=lambda: self.action(1))
        button_2 = tk.Button(self.frame, text="2", command=lambda: self.action(2))
        button_3 = tk.Button(self.frame, text="3", command=lambda: self.action(3))

        button_4 = tk.Button(self.frame, text="4", command=lambda: self.action(4))
        button_5 = tk.Button(self.frame, text="5", command=lambda: self.action(5))
        button_6 = tk.Button(self.frame, text="6", command=lambda: self.action(6))

        button_7 = tk.Button(self.frame, text="7", command=lambda: self.action(7))
        button_8 = tk.Button(self.frame, text="8", command=lambda: self.action(8))
        button_9 = tk.Button(self.frame, text="9", command=lambda: self.action(9))
        button_0 = tk.Button(self.frame, text="0", command=lambda: self.action(0))

        number_buttons = [button_7, button_8, button_9, button_4, 
        button_5, button_6, button_1, button_2,button_3,button_0]       

        #Creating Operator Buttons (+,- etc..)
        add_button = tk.Button(self.frame, text="+", command=lambda: self.action("+"))
        subtract_button = tk.Button(self.frame, text="-", command=lambda: self.action("-"))

        multiply_button = tk.Button(self.frame, text="x", command=lambda: self.action("x"))
        divide_button = tk.Button(self.frame, text="/", command=lambda: self.action("/"))

        exponent_button = tk.Button(self.frame, text="x^n", command=lambda: self.action("^"))
        square_root_button = tk.Button(self.frame, text="√", command=lambda: self.action("√"))

        operator_buttons =[exponent_button, square_root_button, divide_button,
        multiply_button, subtract_button, add_button]

        #Creating Other Buttons (Clear, Decimal etc.)
        open_bracket_button = tk.Button(self.frame, text="(", command=lambda: self.action("("))
        close_bracket_button = tk.Button(self.frame, text=")", command=lambda: self.action(")"))

        decimal_button = tk.Button(self.frame, text=".", command=lambda: self.action("."))
        clear_button = tk.Button(self.frame, text="Clear", command=self.clear)
        all_clear_button = tk.Button(self.frame, text="AC", command=self.all_clear)

        other_buttons = [open_bracket_button, close_bracket_button,decimal_button, 
        clear_button, all_clear_button]

        #Placing Operator Buttons using grid()
        for i, button in enumerate(operator_buttons):
            button.config(height=2, width=8, border=2, bg="#454545", fg="White")
            button.grid(row= i, column=3, padx=3, pady=3)

        #Placing Number and Other buttons using grid()
        n_o_buttons = number_buttons + other_buttons

        for r, group in enumerate([n_o_buttons[i*3 : (i+1)*3] for i in range(5)]):
            for c, button in enumerate(group):
                button.config(height=2, width=8, border=2, bg="#454545", fg="White")
                button.grid(row= r, column= c, padx=3, pady=3)    

        #Creating & Placing Equal Button
        equal_button = tk.Button(self.frame, text="=", command=self.equal)
        equal_button.config(height=2, width=29, border=2, bg="#454545", fg="white")
        equal_button.grid(row=5, column=0, columnspan=3, padx=3, pady=3)

    def action(self, value):
        self.expression = self.input_field.get()
        self.expression += str(value)
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression) 

    def replace_operators(self):
        operators = {"x" : "*", "^" : "**", ")(" : ")*(", "√" : "sqrt("}
        for o in operators:
            self.expression = self.expression.replace(o, operators[o])            

    def equal(self):
        self.expression = self.input_field.get()
        self.replace_operators()
        self.input_field.delete(0, tk.END)
        try:
            if "sqrt" in self.expression:
                self.expression += ")"    
            self.expression = str(eval(self.expression))  
            if len(self.expression) > 45:
                self.input_field.insert(0, "Calculation Timeout")
            else:     
                self.input_field.insert(0, self.expression) 
        except ZeroDivisionError:
            self.input_field.insert(0, "Cannot be divided by 0")
        except SyntaxError or TypeError:
            self.input_field.insert(0, "Invalid Input")

    def clear(self):
        self.expression = self.input_field.get()[:-1]
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)

    def all_clear(self):
        self.expression = ""
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)          

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Calculator")
    root.config(bg="#323232")
    root.minsize(324,366)
    root.maxsize(324,366)

    simple_calculator = Calculator(root)

    root.mainloop()