
# Imports
import mainmenu, length, temperature, volume, weight
import funcs
import tkinter as tk
from tkinter import ttk



AREA_VALUES = {
    "SqrMeter":{"SqrMeter":1,"SqrKilometer":0.000001,"SqrCentimeter":10000,"SqrMile":3.861018768**-7,"SqrYard":1.1959900463,"SqrFoot":10.763910417,"SqrInch":1550.0031,"Acre":0.0002471054},
    "SqrKilometer":{"SqrMeter":1000000,"SqrKilometer":1,"SqrCentimeter":10000000000,"SqrMile":0.3861018768,"SqrYard":1195990.0463,"SqrFoot":10763910.417,"SqrInch":1550003100,"Acre":247.10538147},
    "SqrCentimeter":{"SqrMeter":0.0001,"SqrKilometer":1**-10,"SqrCentimeter":1,"SqrMile":3.861018768**-11,"SqrYard":0.000119599,"SqrFoot":0.001076391,"SqrInch":0.15500031,"Acre":2.471053814**-8},
    "SqrMile":{"SqrMeter":2589990,"SqrKilometer":2.58999,"SqrCentimeter":25899900000,"SqrMile":1,"SqrYard":3097602.26,"SqrFoot":27878420.34,"SqrInch":4014492529,"Acre":640.00046695},
    "SqrYard":{"SqrMeter":0.83612736,"SqrKilometer":8.3612736**-7,"SqrCentimeter":8361.2736,"SqrMile":3.228303429**-7,"SqrYard":1,"SqrFoot":9,"SqrInch":1296,"Acre":0.0002066116},
    "SqrFoot":{"SqrMeter":0.09290304,"SqrKilometer":9.290304**-8,"SqrCentimeter":929.0304,"SqrMile":3.58700381**-8,"SqrYard":0.1111111111,"SqrFoot":1,"SqrInch":144,"Acre":0.0000229568},
    "SqrInch":{"SqrMeter":0.00064516,"SqrKilometer":6.4516**-10,"SqrCentimeter":6.4516,"SqrMile":2.490974868**-10,"SqrYard":0.0007716049,"SqrFoot":0.0069444444,"SqrInch":1,"Acre":1.594225079**-7},
    "Acre":{"SqrMeter":4046.8564224,"SqrKilometer":0.0040468564,"SqrCentimeter":40468564.224,"SqrMile":0.0015624989,"SqrYard":4840,"SqrFoot":43560,"SqrInch":6272640,"Acre":1}
}

# Controls the Area Frame.
class Area(tk.Frame):
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
        funcs._frame_title(self, "Area")
        funcs._frame_labels(self)
        funcs._frame_buttons(self, self.controller, AREA_VALUES)
        funcs._frame_inputs_n_outputs(self, self.valueEntry, self.resultLabel)
        funcs._frame_menus(self, AREA_VALUES, self.inputMenu, self.outputMenu)