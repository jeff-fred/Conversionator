
# Imports
import mainmenu
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

''' Application general attributes and functions ''' 

# ==== Attributes ==== 
colorSchemes = {"bg":"gray36", "fg":"snow"}

#Places window at center of the screen
def center_window(root, size):
    win_size = size.split("x")

    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    win_x = int((screen_width/2) - (int(win_size[0])/2))
    win_y = int((screen_height/2) - (int(win_size[1])/2))

    root.geometry("{0}+{1}+{2}".format(size, win_x, win_y))

# Generate grid on to frame for all conversion frames
def generate_frame_grid(frame):
    rows = 0
    while rows < frame.numRows+1:
        frame.rowconfigure(rows, weight=1)
        rows += 1

    columns = 0
    while columns < frame.numColumns:
        frame.columnconfigure(columns, weight=1)
        columns += 1

# Create a title on every frame with the same characteristics
def _frame_title(frame, title):
    tk.Label(
        frame, 
        text=title, 
        bg=frame.backgroundColor,
        fg=frame.foregroundColor,
        anchor="center",
        padx=5,
        relief="ridge",
        font=("Courier", 20,"bold")
    ).grid(row=0, columnspan=frame.numColumns)

# Create and grid immutable labels
def _frame_labels(frame):
    tk.Label(
        frame,
        text="Value: ",
        bg=frame.backgroundColor,
        fg=frame.foregroundColor,
        padx=10,
        font=("Courier", 14)
    ).grid(row=2, column=0, sticky="n")
    
    tk.Label(
        frame,
        text="Result: ",
        bg=frame.backgroundColor,
        fg=frame.foregroundColor,
        padx=10,
        font=("Courier", 14)
    ).grid(row=3, column=0, sticky="n")

# Grid and modify in and out widgets
def _frame_inputs_n_outputs(frame, inputWidget, outputWidget):
    inputWidget.config(
        bg=frame.backgroundColor,
        fg=frame.foregroundColor,
        width=10
    )
    inputWidget.grid(row=2, columnspan=3, sticky="n")

    outputWidget.config(
        text=" ---- ",
        fg=frame.foregroundColor,
        bg=frame.backgroundColor,
        anchor="center",
        font=("Courier", 10,"italic")
    )
    outputWidget.grid(row=3, columnspan=3, sticky="n")

# Grid and modify frame buttons
def _frame_buttons(frame, controller, values):
    tk.Button(
        frame,
        text="Return",
        bg=frame.backgroundColor,
        fg=frame.foregroundColor,
        font=("Courier", 10, "italic"),
        command=lambda: [clear(frame.valueEntry, frame.resultLabel, frame.inputMenu, frame.outputMenu), controller.show_window(mainmenu.MainMenu)]
        ).grid(row=frame.numRows, column=0, padx=15, pady=15, sticky="ws")
    
    tk.Button(
        frame,
        text="Calculate",
        fg=frame.foregroundColor,
        bg=frame.backgroundColor,
        font=("Courier", 12,"bold"),
        command=lambda: calculate(values, frame.inputMenu, frame.outputMenu, frame.valueEntry, frame.resultLabel)
    ).grid(row=4, columnspan=3, sticky="n")

    tk.Button(
        frame,
        text="Clear",
        fg=frame.foregroundColor,
        bg=frame.backgroundColor,
        font=("Courier", 10, "italic"),
        command=lambda: clear(frame.valueEntry, frame.resultLabel, frame.inputMenu, frame.outputMenu)
    ).grid(row=4, column=2, sticky="se", padx=15, pady=15)

# Grid and edit the menus
def _frame_menus(frame, values, inMenu, outMenu):
    inMenu.state(["readonly"])
    outMenu.state(["readonly"])

    inMenu['values'] = ([i for i in values])
    outMenu['values'] = ([i for i in values])

    inMenu.config(width=10)
    outMenu.config(width=10)
    inMenu.grid(row=2, column=2, sticky="n")
    outMenu.grid(row=3, column=2, sticky="n")

# Calculates the conversion
def calculate(values, inMenu, outMenu, entryWidget, resultWidget):
    try:
        entryValue = int(entryWidget.get())
        conversion = values[inMenu.get()][outMenu.get()]
        calculation = round((entryValue*conversion), 10)
        resultWidget.config(text=str(calculation))
    except ValueError:
        clear(entryWidget, resultWidget, inMenu, outMenu)
        messagebox.showerror("Error", "Please enter a number.")

# Clears the In and Out widgets and clears both drop menus
def clear(entryWidget, resultWidget, inMenu, outMenu):
    entryWidget.delete(0, "end")
    resultWidget.config(text="----")
    inMenu.set("")
    outMenu.set("")