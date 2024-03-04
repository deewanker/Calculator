import tkinter as tk
from PIL import Image, ImageTk
import math
import random

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
    elif symbol == 'sin':
        try:
            result = math.sin(math.radians(float(current)))
            display_var.set(str(result))
        except:
            display_var.set('Error')
    elif symbol == 'cos':
        try:
            result = math.cos(math.radians(float(current)))
            display_var.set(str(result))
        except:
            display_var.set('Error')
    elif symbol == 'tan':
        try:
            result = math.tan(math.radians(float(current)))
            display_var.set(str(result))
        except:
            display_var.set('Error')
    elif symbol == 'sqrt':
        try:
            result = math.sqrt(float(current))
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
button1 = tk.Button(m, text="7", width=5, command=lambda: click('7'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button1.grid(row=1, column=0, sticky='news')

button2 = tk.Button(m, text="8", width=5, command=lambda: click('8'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button2.grid(row=1, column=1, sticky='news')

button3 = tk.Button(m, text="9", width=5, command=lambda: click('9'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button3.grid(row=1, column=2, sticky='news')

button4 = tk.Button(m, text="+", width=5, command=lambda: click('+'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button4.grid(row=1, column=3, sticky='news')

# Next row
button5 = tk.Button(m, text="4", width=5, command=lambda: click('4'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button5.grid(row=2, column=0, sticky='news')

button6 = tk.Button(m, text="5", width=5, command=lambda: click('5'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button6.grid(row=2, column=1, sticky='news')

button7 = tk.Button(m, text="6", width=5, command=lambda: click('6'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button7.grid(row=2, column=2, sticky='news')

button8 = tk.Button(m, text="-", width=5, command=lambda: click('-'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button8.grid(row=2, column=3, sticky='news')

# Next row
button9 = tk.Button(m, text="1", width=5, command=lambda: click('1'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button9.grid(row=3, column=0, sticky='news')

button10 = tk.Button(m, text="2", width=5, command=lambda: click('2'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button10.grid(row=3, column=1, sticky='news')

button11 = tk.Button(m, text="3", width=5, command=lambda: click('3'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button11.grid(row=3, column=2, sticky='news')

button12 = tk.Button(m, text="*", width=5, command=lambda: click('*'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button12.grid(row=3, column=3, sticky='news')

# Next row
button13 = tk.Button(m, text="C", width=5, command=lambda: click('C'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button13.grid(row=4, column=0, sticky='news')

button14 = tk.Button(m, text="0", width=5, command=lambda: click('0'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button14.grid(row=4, column=1, sticky='news')

button15 = tk.Button(m, text="=", width=5, command=lambda: click('='), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button15.grid(row=4, column=2, sticky='news')

button16 = tk.Button(m, text="/", width=5, command=lambda: click('/'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button16.grid(row=4, column=3, sticky='news')

# Scientific calculator buttons
button17 = tk.Button(m, text="sin", width=5, command=lambda: click('sin'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button17.grid(row=5, column=0, sticky='news')

button18 = tk.Button(m, text="cos", width=5, command=lambda: click('cos'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button18.grid(row=5, column=1, sticky='news')

button19 = tk.Button(m, text="tan", width=5, command=lambda: click('tan'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button19.grid(row=5, column=2, sticky='news')

button20 = tk.Button(m, text="sqrt", width=5, command=lambda: click('sqrt'), bg=f'#{random.randint(0, 0xFFFFFF):06x}')
button20.grid(row=5, column=3, sticky='news')


# Load and display an image
image = Image.open("C:/Users/vipin/Downloads/accountant-concept-illustration/5252601.jpg")
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = tk.Label(m, image=photo)
label.grid(row=7, column=0, columnspan=4, sticky='news', padx=10, pady=10)


# Run the main event loop
m.mainloop()
