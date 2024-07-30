from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")  # Set the window size

# Change the background color of the root window 
root.configure(bg='#2e2e2e') 

# Global variable to store the equation
equation_text = ""
equation_label = StringVar()

# Function to handle button presses for numbers and operators
def button_press(num):
    global equation_text
    # Add the pressed button's value to the equation text
    equation_text = equation_text + str(num)
    # Update the label
    equation_label.set(equation_text)

# Function to evaluate the equation and display the result
def equals():
    global equation_text
    try:
        # Evaluate the equation using eval and convert to string
        total = str(eval(equation_text))
        # Update the label with the result
        equation_label.set(total)
        # Set the equation text to the result for further calculations
        equation_text = total
    except SyntaxError:
        # Handle syntax errors and reset the equation text
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        # Handle division by zero errors and reset the equation text
        equation_label.set("Arithmetic Error")
        equation_text = ""

# Function to clear the equation text and reset the display
def clear():
    global equation_text
    # Clear the label
    equation_label.set("")
    # Reset the equation text
    equation_text = ""

# Set up the display label to see sum
label = Label(root, textvariable=equation_label, font=('Verdana', 20, 'bold'), bg="white", fg="black", width=24, height=2)
label.grid(row=0, column=1, columnspan=4)

# Configure the grid rows and columns for centering the label and buttons
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(5, weight=1)

# Configure the grid rows and columns for the buttons
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=0)
root.grid_columnconfigure(4, weight=0)

# Define colors for buttons
button_colors = {
    'number': {'bg': '#4e4e4e', 'fg': '#ffffff'},  # Medium grey for number buttons
    'operator': {'bg': '#666666', 'fg': '#ffffff'},  # Slightly lighter grey for operator buttons
    'equals': {'bg': '#888888', 'fg': '#ffffff'},  # Even lighter grey for equals button
    'clear': {'bg': '#555555', 'fg': '#ffffff'}  # Dark grey for clear button
}

# Add buttons to the grid 
button1 = tk.Button(root, text="7", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(7))
button1.grid(row=1, column=1)

button2 = tk.Button(root, text="8", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(8))
button2.grid(row=1, column=2)

button3 = tk.Button(root, text="9", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(9))
button3.grid(row=1, column=3)

button4 = tk.Button(root, text="-", width=15, height=3, bg=button_colors['operator']['bg'], fg=button_colors['operator']['fg'], command=lambda: button_press('-'))
button4.grid(row=1, column=4)

button5 = tk.Button(root, text="4", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(4))
button5.grid(row=2, column=1)

button6 = tk.Button(root, text="5", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(5))
button6.grid(row=2, column=2)

button7 = tk.Button(root, text="6", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(6))
button7.grid(row=2, column=3)

button8 = tk.Button(root, text="/", width=15, height=3, bg=button_colors['operator']['bg'], fg=button_colors['operator']['fg'], command=lambda: button_press('/'))
button8.grid(row=2, column=4)

button9 = tk.Button(root, text="1", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(1))
button9.grid(row=3, column=1)

button10 = tk.Button(root, text="2", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(2))
button10.grid(row=3, column=2)

button11 = tk.Button(root, text="3", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(3))
button11.grid(row=3, column=3)

button12 = tk.Button(root, text="X", width=15, height=3, bg=button_colors['operator']['bg'], fg=button_colors['operator']['fg'], command=lambda: button_press('*'))
button12.grid(row=3, column=4)

button13 = tk.Button(root, text="0", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press(0))
button13.grid(row=4, column=1)

button14 = tk.Button(root, text=".", width=15, height=3, bg=button_colors['number']['bg'], fg=button_colors['number']['fg'], command=lambda: button_press('.'))
button14.grid(row=4, column=2)

button15 = tk.Button(root, text="+", width=15, height=3, bg=button_colors['operator']['bg'], fg=button_colors['operator']['fg'], command=lambda: button_press('+'))
button15.grid(row=4, column=3)

# Equals button directly calls the equals function
button16 = tk.Button(root, text="=", width=15, height=3, bg=button_colors['equals']['bg'], fg=button_colors['equals']['fg'], command=equals)
button16.grid(row=4, column=4)

# Clear button to reset the equation
btn_clear = tk.Button(root, text="C", width=15, height=3, bg=button_colors['clear']['bg'], fg=button_colors['clear']['fg'], command=clear)
btn_clear.grid(row=5, column=1, columnspan=4)

# Start the Tkinter event loop
root.mainloop()
