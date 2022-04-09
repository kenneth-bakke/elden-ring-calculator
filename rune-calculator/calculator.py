import os
from tkinter import *
from tkinter import ttk
from config import ELDEN_RING
from attributes import Attribute
from character_details import CharacterDetails


class RuneCalculator:
    def __init__(self, root):

        root.title("Rune Calculator")

        self.mainframe = ttk.Frame(root, padding="3 12")

        # MAIN FRAMES GRID
        self.character_details = ttk.Frame(self.mainframe, borderwidth=2, relief="sunken")
        self.attributes = ttk.Frame(self.mainframe, borderwidth=2, relief="sunken")
        self.items = ttk.Frame(self.mainframe, borderwidth=2, relief="sunken")

        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.character_details.grid(column=0, row=0, columnspan=4, rowspan=1, sticky=(N, W, E, S))
        self.attributes.grid(column=0, row=1, sticky=(N, W, E, S))
        self.items.grid(column=1, row=1, sticky=(N, W, E, S))

        # CHARACTER DETAILS SECTION
        CharacterDetails(self.character_details, "Placeholder")

        # ATTRIBUTES SECTION
        for i, attribute in enumerate(ELDEN_RING["ATTRIBUTES"]):
            Attribute(self.attributes, i, attribute)

        # ITEMS SECTION
        self.items_label = ttk.Label(self.items, text="Choose Item Type")
        self.items_label.grid(column=3, row=2, columnspan=4, sticky=W)
        # WEAPONS SECTION
        self.weapon_categories_var = StringVar(self.items, name="Weapon Categories")
        self.weapon_categories_list = ELDEN_RING["WEAPON_CATEGORIES"].keys()
        self.weapon_categories_combobox = ttk.Combobox(
            self.items, height=10, justify="left", text="Weapon Categories", textvariable=self.weapon_categories_var
        )
        self.weapon_categories_combobox["values"] = [category for category in self.weapon_categories_list]
        self.weapon_categories_combobox.current(0)
        self.weapon_categories_combobox.grid(column=3, row=3, sticky=W)
