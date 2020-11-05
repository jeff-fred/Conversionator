
# Imports
import mainmenu, length, temperature, area, weight
import funcs
import tkinter as tk
from tkinter import ttk



VOLUME_VALUES = {
    "Liter":{"Liter":1, "Milliliter":1000,"US_Gallon":0.2641721769, "US_Quart":1.0566887074, "US_Pint":2.1133774149,"US_Cup":4.2267548297},
    "Milliliter":{"Liter":0.001, "Milliliter":1,"US_Gallon":0.0002641722, "US_Quart":0.0010566887, "US_Pint":0.0021133774,"US_Cup":0.0042267548},
    "US_Gallon":{"Liter":3.78541, "Milliliter":3785.41,"US_Gallon":1, "US_Quart":4, "US_Pint":8,"US_Cup":16},
    "US_Quart":{"Liter":0.9463525, "Milliliter":946.3525,"US_Gallon":0.25, "US_Quart":1, "US_Pint":2,"US_Cup":4},
    "US_Pint":{"Liter":0.47317625, "Milliliter":473.17625,"US_Gallon":0.125, "US_Quart":0.5, "US_Pint":1,"US_Cup":2},
    "US_Cup":{"Liter":0.236588125, "Milliliter":236.588125,"US_Gallon":0.0625, "US_Quart":0.25, "US_Pint":0.5,"US_Cup":1}
}


class Volume(tk.Frame):
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
        funcs._frame_title(self, "Volume")
        funcs._frame_labels(self)
        funcs._frame_buttons(self, self.controller, VOLUME_VALUES)
        funcs._frame_inputs_n_outputs(self, self.valueEntry, self.resultLabel)
        funcs._frame_menus(self, VOLUME_VALUES, self.inputMenu, self.outputMenu)
