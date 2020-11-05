''' Main Application ''' 

# Imports
import mainmenu, length, temperature, area, volume, weight
import funcs
import tkinter as tk
from tkinter import ttk
 

class Conversionator(tk.Tk):
    """ Main window for all the frames. """

    # == Window Attributes == 
    defaultTitle = "Conversionator"
    defaultSize = "500x400"

    # Initalizes the window
    def __init__(self):
        super().__init__()

        # Setting window characteristics
        self.title(self.defaultTitle)
        funcs.center_window(self, self.defaultSize)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Creating dict and adding into it
        self.windows = {}
        self.windows[mainmenu.MainMenu] = mainmenu.MainMenu(self)
        self.windows[length.Length] = length.Length(self)
        self.windows[temperature.Temperature] = temperature.Temperature(self)
        self.windows[volume.Volume] = volume.Volume(self)
        self.windows[area.Area] = area.Area(self)
        self.windows[weight.Weight] = weight.Weight(self)

    # Run the program        
    def run(self):
        self.show_window(mainmenu.MainMenu)


    # Initalizes the Frame, and raises it to the top of the window
    def show_window(self, window_name):
        frame = self.windows[window_name]
        frame.tkraise()
        self.geometry(window_name.winSize)


    # Removes grid from frame, making it invisible to the main window
    def hide_window(self, window_name):
        frame = self.windows[window_name]
        frame.grid_forget()


if __name__ == "__main__":
    app = Conversionator()
    app.run()
    app.mainloop()