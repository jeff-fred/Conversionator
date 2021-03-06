
# Imports
import mainmenu, length, area, volume, weight
import funcs
import tkinter as tk
from tkinter import ttk


TEMPERATURE_VALUES = {
    "Celsius":{"Celsius":1, "Kelvin":0, "Fahrenheit":9/5},
    "Kelvin":{"Celsius":0, "Kelvin":1, "Fahrenheit":0},
    "Fahrenheit":{"Celsius":0, "Kelvin":0, "Fahrenheit":1}
}



class Temperature(tk.Frame):
    """ Frame that contains options for all conversions """

    # == Frame Attributes == 
    winSize = "500x400"
    backgroundColor = funcs.colorSchemes["bg"]
    foregroundColor = funcs.colorSchemes["fg"]

    # Inialize the Frame
    def __init__(self, controller):
        super().__init__()
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller


        # Frame Characteristics
        self.configure(bg=self.backgroundColor)

        # ======= Grid Size ======== 
        self.numRows = 4
        self.numColumns = 3
        
        funcs.generate_frame_grid(self)
        # ==========================

        self.valueEntry = tk.Entry(self)
        self.resultLabel = tk.Label(self) 

        self.inputMenu = ttk.Combobox(self)
        self.outputMenu = ttk.Combobox(self)

        self.setup_widgets()
 

    def setup_widgets(self):
        funcs._frame_title(self, "Temperature")
        funcs._frame_labels(self)
        funcs._frame_buttons_temperature(self, self.controller, TEMPERATURE_VALUES)
        funcs._frame_inputs_n_outputs(self, self.valueEntry, self.resultLabel)
        funcs._frame_menus(self, TEMPERATURE_VALUES, self.inputMenu, self.outputMenu)

