import tkinter as tk

# buttons are clicked
def click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set('Error')
    else:
        display_var.set(current + symbol)

# Defining variables and putting title
m = tk.Tk()
m.title("Python Calculator")

# Making Textbox to get input
display_var = tk.StringVar()
display_var.set('')

display = tk.Entry(m, textvariable=display_var, font=('Lucida', 18), border=5)
display.grid(row=0, column=0, columnspan=4, sticky='news', padx=40, pady=10)

# Making buttons for calculator
button1 = tk.Button(m, text="7", width=5, command=lambda: click('7'))
button1.grid(row=1, column=0, sticky='news')

button2 = tk.Button(m, text="8", width=5, command=lambda: click('8'))
button2.grid(row=1, column=1, sticky='news')

button3 = tk.Button(m, text="9", width=5, command=lambda: click('9'))
button3.grid(row=1, column=2, sticky='news')

button4 = tk.Button(m, text="+", width=5, command=lambda: click('+'))
button4.grid(row=1, column=3, sticky='news')

# Next row
button5 = tk.Button(m, text="4", width=5, command=lambda: click('4'))
button5.grid(row=2, column=0, sticky='news')

button6 = tk.Button(m, text="5", width=5, command=lambda: click('5'))
button6.grid(row=2, column=1, sticky='news')

button7 = tk.Button(m, text="6", width=5, command=lambda: click('6'))
button7.grid(row=2, column=2, sticky='news')

button8 = tk.Button(m, text="-", width=5, command=lambda: click('-'))
button8.grid(row=2, column=3, sticky='news')

# Next row
button9 = tk.Button(m, text="1", width=5, command=lambda: click('1'))
button9.grid(row=3, column=0, sticky='news')

button10 = tk.Button(m, text="2", width=5, command=lambda: click('2'))
button10.grid(row=3, column=1, sticky='news')

button11 = tk.Button(m, text="3", width=5, command=lambda: click('3'))
button11.grid(row=3, column=2, sticky='news')

button12 = tk.Button(m, text="*", width=5, command=lambda: click('*'))
button12.grid(row=3, column=3, sticky='news')

# Next row
button13 = tk.Button(m, text="C", width=5, command=lambda: click('C'))
button13.grid(row=4, column=0, sticky='news')

button14 = tk.Button(m, text="0", width=5, command=lambda: click('0'))
button14.grid(row=4, column=1, sticky='news')

button15 = tk.Button(m, text="=", width=5, command=lambda: click('='))
button15.grid(row=4, column=2, sticky='news')

button16 = tk.Button(m, text="/", width=5, command=lambda: click('/'))
button16.grid(row=4, column=3, sticky='news')

# Run the main event loop
m.mainloop()
