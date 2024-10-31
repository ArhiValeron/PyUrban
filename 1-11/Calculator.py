import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

window = tk.Tk()
window.title("Калькулятор")

entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_7 = tk.Button(window, text="7", width=5, command=lambda: button_click("7"))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = tk.Button(window, text="8", width=5, command=lambda: button_click("8"))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = tk.Button(window, text="9", width=5, command=lambda: button_click("9"))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_multiply = tk.Button(window, text="*", width=5, command=lambda: button_click("*"))
button_multiply.grid(row=1, column=3, padx=5, pady=5)

button_4 = tk.Button(window, text="4", width=5, command=lambda: button_click("4"))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(window, text="5", width=5, command=lambda: button_click("5"))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(window, text="6", width=5, command=lambda: button_click("6"))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_divide = tk.Button(window, text="/", width=5, command=lambda: button_click("/"))
button_divide.grid(row=2, column=3, padx=5, pady=5)

button_1 = tk.Button(window, text="1", width=5, command=lambda: button_click("1"))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = tk.Button(window, text="2", width=5, command=lambda: button_click("2"))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = tk.Button(window, text="3", width=5, command=lambda: button_click("3"))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_add = tk.Button(window, text="+", width=5, command=lambda: button_click("+"))
button_add.grid(row=3, column=3, padx=5, pady=5)

button_0 = tk.Button(window, text="0", width=5, command=lambda: button_click("0"))
button_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

button_dot = tk.Button(window, text=".", width=5, command=lambda: button_click("."))
button_dot.grid(row=4, column=2, padx=5, pady=5)

button_equal = tk.Button(window, text="=", width=5, command=equal)
button_equal.grid(row=4, column=3, padx=5, pady=5)

button_clear = tk.Button(window, text="C", width=5, command=clear)
button_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()