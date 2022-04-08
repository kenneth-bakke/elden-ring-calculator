from tkinter import *
from tkinter import ttk
from config import ELDEN_RING
import requests

local_api = "http://127.0.0.1:3000/items/"


class Items:
    def __init__(self, root):
        self.mainframe = ttk.Frame(root, border=1, borderwidth=1, relief="sunken")

        # Variables
        self.item_category = None
        self.selected_item = None
        self.categories_list = sorted(ELDEN_RING["ITEM_CATEGORIES"].keys())
        self.items_list = []

        # State Variables
        self.choose_item_category = False if self.item_category else True

        # Items dropdown -> On select make a call to the API for the category
        self.items_label = ttk.Label(self.mainframe, text="Item Type")
        self.item_categories_combobox = ttk.Combobox(
            self.mainframe,
            height=len(self.categories_list) + 1,
            justify="left",
            text="Item Types",
            textvariable=self.item_category if self.item_category else "Items",
        )
        self.item_categories_display = ttk.Label(self.mainframe, text="Item Categories")
        # Search bar -> Just like a React app, live update based on name

        # List -> Live update based on search term

        # EVENT BINDINGS
        self.item_categories_combobox.bind("<<ComboboxSelected>>", self.get_items)
        self.item_categories_display.bind("<Button-1>", self.toggle_choose_item_categories)

        # GRID
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.items_label.grid(column=1, row=1, columnspan=2, sticky=W)

        self.initialize_items()

    def initialize_items(self):
        self.initialize_item_categories_display()

    # INITIALIZERS
    def initialize_item_categories_display(self, event=None):
        self.item_categories_combobox.grid(column=1, row=2, columnspan=2, sticky=(W, E))
        self.item_categories_combobox["state"] = "readonly"
        self.categories_list.insert(0, "Item Categories")
        self.item_categories_combobox["values"] = [category for category in self.categories_list]
        self.item_categories_combobox.current(0)

        if self.choose_item_category:
            self.item_categories_display.grid_remove()
        else:
            self.item_categories_combobox.grid_remove()

    # REST METHODS
    def get_items(self, event=None):
        category = self.item_categories_combobox.get()
        self.item_category = category
        category_url = f"{local_api}{category.lower()}"
        print(category_url)
        if category != "Item Categories":
            category_items = requests.get(category_url)
            print(category_items)
        self.item_categories_display["text"] = self.item_category
        self.toggle_choose_item_categories()

    # TOGGLES
    def toggle_choose_item_categories(self, event=None):
        self.choose_item_category = not self.choose_item_category
        if self.choose_item_category:
            self.item_categories_display.grid_remove()
            self.item_categories_combobox.grid(column=1, row=2, columnspan=2, sticky=(W, E))
        else:
            self.item_categories_combobox.grid_remove()
            self.item_categories_display.grid(column=1, row=2, columnspan=2, sticky=(W, E))


root = Tk()
Items(root)
root.mainloop()
