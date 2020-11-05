
# Imports
import mainmenu, temperature, area, volume, weight
import funcs
import tkinter as tk
from tkinter import ttk



# Conversions
LENGTH_VALUES = {
    "Meter":{"Meter":1, "Kilometer":0.001, "Centimeter":100, "Mile":0.0006213689, "Yard":1.0936132983, "Feet": 3.280839895, "Inches": 39.37007874},
    "Kilometer":{"Meter":1000, "Kilometer":1, "Centimeter":100000, "Mile":0.6213688756, "Yard":1093.6132983, "Feet":3280.839895, "Inches":39370.07874},
    "Centimeter":{"Meter":0.01, "Kilometer":0.00001, "Centimeter":1, "Mile":0.0000062137, "Yard":0.010936133, "Feet":0.032808399, "Inches":0.3937007874},
    "Mile":{"Meter":1609.35, "Kilometer":1.60935, "Centimeter":160935, "Mile":1, "Yard":1760.0065617, "Feet":5280.019685, "Inches":63360.23622},
    "Yard":{"Meter":0.9144, "Kilometer":0.0009144, "Centimeter":91.44, "Mile":0.0005681797, "Yard":1, "Feet":3, "Inches":36},
    "Feet":{"Meter":0.3048, "Kilometer":0.0003048, "Centimeter":30.48, "Mile":0.0001893932, "Yard":0.3333333333, "Feet":1, "Inches":12},
    "Inches":{"Meter":0.0254, "Kilometer":0.0000254, "Centimeter":2.54, "Mile":0.0000157828, "Yard":0.0277777778, "Feet":0.0833333333, "Inches":1}
    }


class Length(tk.Frame):
    """ Frame that contains all LENGTH conversions """

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

        # Input & output
        self.valueEntry = tk.Entry(self)
        self.resultLabel = tk.Label(self) 

        self.inputMenu = ttk.Combobox(self)
        self.outputMenu = ttk.Combobox(self)

        self.setup_widgets()


    def setup_widgets(self):
        funcs._frame_title(self, "Length")
        funcs._frame_labels(self)
        funcs._frame_buttons(self, self.controller, LENGTH_VALUES)
        funcs._frame_inputs_n_outputs(self, self.valueEntry, self.resultLabel)
        funcs._frame_menus(self, LENGTH_VALUES, self.inputMenu, self.outputMenu)
