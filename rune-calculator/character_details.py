from tkinter import *
from tkinter import ttk
from config import ELDEN_RING


# TODO: ADD RUNES NEEDED
class CharacterDetails:
    def __init__(self, root, level=None, class_type=None, runes_held=0, name=None):

        self.mainframe = ttk.Frame(root, border=1, borderwidth=1, relief="sunken")

        # Character Variables
        self.character_name = name
        self.character_level = level
        self.character_class = class_type
        self.runes_held = runes_held

        # State Variables
        self.edit_name = False if self.character_name else True
        self.edit_level = False if self.character_level else True
        self.character_classes_list = ELDEN_RING["CLASSES"].keys()

        # Widgets
        # Name
        self.character_name_label = ttk.Label(
            self.mainframe, text="Character Name", border=1, borderwidth=1, relief="sunken"
        )
        self.character_name_entry = ttk.Entry(self.mainframe, textvariable=self.character_name)
        self.character_name_display = ttk.Label(self.mainframe, text=self.character_name)
        # Level
        self.character_level_label = ttk.Label(
            self.mainframe, text="Current Level", border=1, borderwidth=1, relief="sunken"
        )
        self.character_level_entry = ttk.Entry(self.mainframe, textvariable=self.character_level)
        self.character_level_display = ttk.Label(self.mainframe, text=self.character_level)

        # Runes TODO

        # Class TODO

        # self.runes_held_label = ttk.Label(self.character_details, text="Runes Held")
        # self.runes_held_entry = ttk.Entry(self.character_details, text="Runes Held", textvariable=self.runes_held)
        # self.runes_needed_label = ttk.Label(self.character_details, text="Runes Needed")
        # self.runes_needed_display = ttk.Label(self.character_details, text="4000")
        # self.character_class = ttk.Label(self.character_details, text="Class")

        # Event Handlers
        self.character_name_entry.bind("<Return>", self.set_character_name)
        self.character_name_display.bind("<Button-1>", self.toggle_edit_name)
        self.character_level_entry.bind("<Return>", self.set_character_level)
        self.character_level_display.bind("<Button-1>", self.toggle_edit_level)

        # Grid
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.character_name_label.grid(column=1, row=1, columnspan=2, sticky=W)
        self.character_level_label.grid(column=1, row=3, columnspan=2, sticky=W)
        self.initialize_character_details()

        # self.character_name_entry.grid(column=2, row=2, sticky=W)
        # self.runes_held_label.grid(column=1, row=3, sticky=W)
        # self.runes_held_entry.grid(column=2, row=3, sticky=W)
        # self.runes_needed_label.grid(column=3, row=3, sticky=W)
        # self.runes_needed_display.grid(column=4, row=3, sticky=W)
        # self.character_class.grid(column=1, row=4, sticky=W)

        # self.character_classes_combobox = ttk.Combobox(
        #     self.character_details, height=8, justify="left", text="Classes", textvariable=self.character_class_var
        # )
        # self.character_classes_combobox["values"] = [char_class for char_class in self.character_classes_list]
        # self.character_classes_combobox.current(0)
        # self.character_classes_combobox.grid(column=2, row=4, sticky=W)

    def initialize_character_details(self):
        self.initialize_name_display()
        self.initialize_level_display()
        # self.initialize_class_display()

    def initialize_name_display(self):
        self.character_name_entry.grid(column=1, row=2, sticky=W)
        self.character_name_display.grid(column=2, row=2, sticky=W)
        if self.edit_name:
            self.character_name_display.grid_remove()
        else:
            self.character_name_entry.grid_remove()

    def initialize_level_display(self):
        self.character_level_entry.grid(column=1, row=4, sticky=W)
        self.character_level_display.grid(column=1, row=4, sticky=W)
        if self.edit_level:
            self.character_level_display.grid_remove()
        else:
            self.character_level_entry.grid_remove()

    # def initialize_class_display(self):
    #     self.character_class_combobox.grid(column=1, row=3, sticky=W)
    #     self.character_class_display.grid(column=1, row=3, sticky=W)
    #     if self.edit_level:
    #         self.character_class_display.grid_remove()
    #     else:
    #         self.character_class_combobox.grid_remove()

    def set_character_name(self, event=None):
        name = self.character_name_entry.get()
        self.character_name = name
        self.character_name_display["text"] = name
        self.character_name_entry.delete(0, END)
        self.toggle_edit_name()

    def toggle_edit_name(self, event=None):
        self.edit_name = not self.edit_name
        if self.edit_name:
            self.character_name_display.grid_remove()
            self.character_name_entry.grid(column=1, row=2, sticky=W)
        else:
            self.character_name_entry.grid_remove()
            self.character_name_display.grid(column=1, row=2, sticky=W)

    def set_character_level(self, event=None):
        level = int(self.character_level_entry.get())
        self.character_level = level
        self.character_level_display["text"] = self.character_level
        self.character_level_entry.delete(0, END)
        self.toggle_edit_level()

    def toggle_edit_level(self, event=None):
        self.edit_level = not self.edit_level
        if self.edit_level:
            self.character_level_display.grid_remove()
            self.character_level_entry.grid(column=1, row=4, sticky=W)
        else:
            self.character_level_entry.grid_remove()
            self.character_level_display.grid(column=1, row=4, sticky=W)


root = Tk()
CharacterDetails(root, 9, "Bandit", 3000, "Bingosa")
root.mainloop()
