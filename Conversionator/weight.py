
# Imports
import mainmenu, length, temperature, area, volume
import funcs
import tkinter as tk
from tkinter import ttk



WEIGHT_VALUES = {
    "Kilogram":{"Kilogram":1, "Gram":1000, "Milligram":1000000, "MetricTon":0.001, "ShortTon":0.0011023122, "Pound":2.2046244202, "Ounce":35.273990723, "Carrat":5000},
    "Gram":{"Kilogram":0.001, "Gram":1, "Milligram":1000, "MetricTon":0.000001, "ShortTon":0.0000011023, "Pound":0.0022046244, "Ounce":0.0352739907, "Carrat":5},
    "Miligram":{"Kilogram":0.000001, "Gram":0.001, "Milligram":1, "MetricTon":9.999999999**-10, "ShortTon":1.10231221**-9, "Pound":0.0000022046, "Ounce":0.000035274, "Carrat":0.005},
    "MetricTon":{"Kilogram":1000, "Gram":1000000, "Milligram":1000000000, "MetricTon":1, "ShortTon":1.1023122101, "Pound":2204.6244202, "Ounce":35273.990723, "Carrat":5000000},
    "ShortTon":{"Kilogram":907.184, "Gram":907184, "Milligram":907184000, "MetricTon":0.907184, "ShortTon":1, "Pound":2000, "Ounce":32000, "Carrat":4535920},
    "Pound":{"Kilogram":0.453592, "Gram":453.592, "Milligram":453592, "MetricTon":0.000453592, "ShortTon":0.0005, "Pound":1, "Ounce":16, "Carrat":2267.96},
    "Ounce":{"Kilogram":0.0283495, "Gram":28.3495, "Milligram":28349.5, "MetricTon":0.0000283495, "ShortTon":0.0000279018, "Pound":0.0625, "Ounce":1, "Carrat":141.7475},
    "Carrat":{"Kilogram":0.0002, "Gram":0.2, "Milligram":200, "MetricTon":2**-7, "ShortTon":2.20462442**-7, "Pound":0.0004409249, "Ounce":0.0070547981, "Carrat":1}
}


class Weight(tk.Frame):
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

        # Input & output
        self.valueEntry = tk.Entry(self)
        self.resultLabel = tk.Label(self) 

        self.inputMenu = ttk.Combobox(self)
        self.outputMenu = ttk.Combobox(self)

        self.setup_widgets()


    def setup_widgets(self):
        funcs._frame_title(self, "Weight")
        funcs._frame_labels(self)
        funcs._frame_buttons(self, self.controller, WEIGHT_VALUES)
        funcs._frame_inputs_n_outputs(self, self.valueEntry, self.resultLabel)
        funcs._frame_menus(self, WEIGHT_VALUES, self.inputMenu, self.outputMenu)
