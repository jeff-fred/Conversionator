
# Imports
import length, temperature, area, volume, weight
import funcs
import tkinter as tk


class MainMenu(tk.Frame):
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

        # ====== Grid Size ======= 
        self.numRows = 4
        self.numColumns = 2
        funcs.generate_frame_grid(self)
        # =========================

        self.setup_widgets(self.controller)

    
    # Main Menu Widgets
    def setup_widgets(self, controller):
        tk.Label(self,
                 text = "Select a conversion.",
                 bg = self.backgroundColor,
                 fg = self.foregroundColor, 
                 anchor="center",
                 padx=3,
                 pady=3,
                 relief="groove",
                 font=("Courier", "12", "bold")
                 ).grid(row=0, columnspan=self.numColumns)

        tk.Button(
            self,
            text="Length",
            width=15,
            bg=self.backgroundColor,
            fg=self.foregroundColor,
            font=("Courier", "12", "bold"),
            command=lambda: controller.show_window(length.Length)
        ).grid(row=1, column=0)

        tk.Button(
            self,
            text="Temperature",
            width=15,
            bg=self.backgroundColor,
            fg=self.foregroundColor,
            font=("Courier", "12", "bold"),
            command=lambda: controller.show_window(temperature.Temperature)
        ).grid(row=1, column=1)

        tk.Button(
            self,
            text="Area",
            width=15,
            bg=self.backgroundColor,
            fg=self.foregroundColor,
            font=("Courier", 12, "bold"),
            command=lambda: controller.show_window(area.Area)
        ).grid(row=2, column=0)

        tk.Button(
            self,
            text="Volume",
            width=15,
            bg=self.backgroundColor,
            fg=self.foregroundColor,
            font=("Courier", "12", "bold"),
            command=lambda: controller.show_window(volume.Volume)
        ).grid(row=2, column=1)

        tk.Button(
            self,
            text="Weight",
            width=15,
            bg=self.backgroundColor,
            fg=self.foregroundColor,
            font=("Courier", "12", "bold"),
            command=lambda: controller.show_window(weight.Weight)
        ).grid(row=3, columnspan=2)