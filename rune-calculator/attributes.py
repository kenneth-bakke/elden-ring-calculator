from cgitb import text
from tkinter import *
from tkinter import ttk


class Attribute:
    def __init__(self, root, row_place, name="Placeholder", stat_count=0):
        self.mainframe = ttk.Frame(root, border=1, borderwidth=1, relief="sunken")

        self.stat_count = stat_count

        self.name = ttk.Label(self.mainframe, text=name, border=1, borderwidth=1, relief="sunken")
        self.attr_entry = ttk.Entry(self.mainframe, textvariable=self.stat_count)
        self.attribute_display = ttk.Label(
            self.mainframe, text=self.stat_count, border=1, borderwidth=1, relief="sunken"
        )
        self.inc = ttk.Button(self.mainframe, text="▲", command=self.increment_stat)
        self.dec = ttk.Button(self.mainframe, text="▼", command=self.decrement_stat)

        self.attr_entry.bind("<Return>", self.set_stat_count)

        self.mainframe.grid(column=0, row=row_place, sticky=(N, W, E, S))
        self.name.grid(column=1, row=row_place, rowspan=3, sticky=W)
        self.attr_entry.grid(column=2, row=row_place, rowspan=3, sticky=W)
        self.attribute_display.grid(
            column=3,
            row=row_place,
            rowspan=3,
            sticky=W,
        )
        self.inc.grid(column=4, row=1, ipady=5, ipadx=5, sticky=E)
        self.dec.grid(column=4, row=3, ipady=5, ipadx=5, sticky=E)

    def increment_stat(self):
        self.stat_count = self.stat_count + 1
        if self.stat_count > 99:
            self.stat_count = 99
        self.attribute_display["text"] = self.stat_count

    def decrement_stat(self):
        self.stat_count = self.stat_count - 1
        if self.stat_count < 0:
            self.stat_count = 0
        self.attribute_display["text"] = self.stat_count

    def get_stat_count(self):
        return self.stat_count

    def set_stat_count(self, event):
        print(event)
        stat = int(self.attr_entry.get())
        self.stat_count = int(stat)
        self.attribute_display["text"] = self.stat_count
        self.attr_entry.delete(0, END)
