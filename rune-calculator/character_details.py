from operator import indexOf
from tkinter import *
from tkinter import ttk
from config import ELDEN_RING


# TODO: ADD RUNES NEEDED
class CharacterDetails:
    def __init__(self, root, name="", level=1, class_type="Classes", runes_held=0):

        self.mainframe = ttk.Frame(root, border=1, borderwidth=1, relief="sunken")

        # Character Variables
        self.name = name
        self.level = level
        self.runes_held = runes_held
        self.class_type = class_type

        # State Variables
        self.edit_name = False if self.name else True
        self.edit_level = False if self.level else True
        self.edit_runes = False if self.runes_held else True
        self.choose_class = True if self.class_type == "Classes" else False
        self.class_type_list = sorted(ELDEN_RING["CLASSES"].keys())

        # WIDGETS
        # Name
        self.name_label = ttk.Label(self.mainframe, text="Character Name")
        self.name_entry = ttk.Entry(self.mainframe, textvariable=self.name)
        self.name_display = ttk.Label(self.mainframe, text=self.name)

        # Level
        self.level_label = ttk.Label(self.mainframe, text="Current Level")
        self.level_entry = ttk.Entry(self.mainframe, textvariable=self.level)
        self.level_display = ttk.Label(self.mainframe, text=self.level)

        # Runes
        self.runes_held_label = ttk.Label(self.mainframe, text="Runes Held")
        self.runes_held_entry = ttk.Entry(self.mainframe, textvariable=self.runes_held)
        self.runes_held_display = ttk.Label(self.mainframe, text=self.runes_held)

        # Runes Needed TODO
        # self.runes_needed_label = ttk.Label(self.character_details, text="Runes Needed")
        # self.runes_needed_display = ttk.Label(self.character_details, text="4000")

        # Class
        self.class_type_label = ttk.Label(self.mainframe, text="Class")
        self.class_type_combobox = ttk.Combobox(
            self.mainframe,
            height=10,
            justify="left",
            text="Classes",
            textvariable=self.class_type if self.class_type else "Classes",
        )
        self.class_type_display = ttk.Label(self.mainframe, text="Class")

        # Event Handlers
        self.name_entry.bind("<Return>", self.set_name)
        self.name_display.bind("<Button-1>", self.toggle_edit_name)
        self.level_entry.bind("<Return>", self.set_level)
        self.level_display.bind("<Button-1>", self.toggle_edit_level)
        self.runes_held_entry.bind("<Return>", self.set_runes_held)
        self.runes_held_display.bind("<Button-1>", self.toggle_edit_runes_held)
        self.class_type_combobox.bind("<<ComboboxSelected>>", self.set_class_type)
        self.class_type_combobox.bind("<Button-1>", self.toggle_choose_class)

        # GRID
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.name_label.grid(column=1, row=1, columnspan=2, sticky=W)
        self.level_label.grid(column=1, row=3, columnspan=2, sticky=W)
        self.runes_held_label.grid(column=1, row=5, columnspan=2, sticky=W)
        self.class_type_label.grid(column=3, row=1, columnspan=2, sticky=E)
        self.initialize_character_details()

    def initialize_character_details(self):
        self.initialize_name_display()
        self.initialize_level_display()
        self.initialize_rune_display()
        self.initialize_class_display()

    # Initializers
    def initialize_name_display(self):
        self.name_entry.grid(column=1, row=2, sticky=W)
        self.name_display.grid(column=1, row=2, sticky=W)
        if self.edit_name:
            self.name_display.grid_remove()
        else:
            self.name_entry.grid_remove()

    def initialize_level_display(self):
        self.level_entry.grid(column=1, row=4, sticky=(W, E))
        self.level_display.grid(column=1, row=4, sticky=(W, E))
        if self.edit_level:
            self.level_display.grid_remove()
        else:
            self.level_entry.grid_remove()

    def initialize_rune_display(self):
        self.runes_held_entry.grid(column=1, row=6, sticky=(W, E))
        self.runes_held_display.grid(column=1, row=6, sticky=(W, E))
        if self.edit_runes:
            self.runes_held_display.grid_remove()
        else:
            self.runes_held_entry.grid_remove()

    def initialize_class_display(self):
        self.class_type_combobox.grid(column=3, row=2, sticky=(W, E))
        self.class_type_display.grid(column=3, row=2, sticky=(W, E))
        self.class_type_combobox["state"] = "readonly"
        self.class_type_list.insert(0, "Classes")
        self.class_type_combobox["values"] = [char_class for char_class in self.class_type_list]
        self.class_type_combobox.current(0)
        if self.choose_class:
            self.class_type_display.grid_remove()
        else:
            self.class_type_combobox.grid_remove()

    # EVENT HANDLERS
    # Setters
    def set_name(self, event=None):
        name = self.name_entry.get()
        self.name = name
        self.name_display["text"] = name
        self.name_entry.delete(0, END)
        self.toggle_edit_name()

    def set_level(self, event=None):
        level = int(self.level_entry.get())
        if level < 1:
            level = 1
        if level > 500:
            level = 500
        self.level = level
        self.level_display["text"] = self.level
        self.level_entry.delete(0, END)
        self.toggle_edit_level()

    def set_runes_held(self, event=None):
        runes = int(self.runes_held_entry.get())
        if runes < 0:
            runes = 0
        if runes > 999999999:
            runes = 999999999
        self.runes_held = runes
        self.runes_held_display["text"] = self.runes_held
        self.runes_held_entry.delete(0, END)
        self.toggle_edit_runes_held()

    def set_class_type(self, event=None):
        class_type = self.class_type_combobox.get()
        self.class_type = class_type
        if class_type == "Classes":
            self.choose_class = True
        else:
            self.choose_class = True
        self.class_type_combobox.current(indexOf(class_type))
        self.toggle_choose_class()

    # Toggles
    def toggle_edit_name(self, event=None):
        self.edit_name = not self.edit_name
        if self.edit_name:
            self.name_display.grid_remove()
            self.name_entry.grid(column=1, row=2, sticky=W)
        else:
            self.name_entry.grid_remove()
            self.name_display.grid(column=1, row=2, sticky=W)

    def toggle_edit_level(self, event=None):
        self.edit_level = not self.edit_level
        if self.edit_level:
            self.level_display.grid_remove()
            self.level_entry.grid(column=1, row=4, sticky=W)
        else:
            self.level_entry.grid_remove()
            self.level_display.grid(column=1, row=4, sticky=W)

    def toggle_edit_runes_held(self, event=None):
        self.edit_runes = not self.edit_runes
        if self.edit_runes:
            self.runes_held_display.grid_remove()
            self.runes_held_entry.grid(column=1, row=6, sticky=W)
        else:
            self.runes_held_entry.grid_remove()
            self.runes_held_display.grid(column=1, row=6, sticky=W)

    def toggle_choose_class(self, event=None):
        self.choose_class = not self.choose_class
        if self.choose_class:
            self.class_type_combobox.grid(column=3, row=2, sticky=(W, E))
            self.class_type_display.grid_remove()
        else:
            self.class_type_display.grid(column=3, row=2, sticky=(W, E))
            self.class_type_combobox.grid_remove()


# root = Tk()
# CharacterDetails(root, 9, "Bandit", 3000, "Bingosa")
# root.mainloop()
