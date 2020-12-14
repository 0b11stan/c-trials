import tkinter as tk
import json
from factsengine import FactsEngine
from rulesengine import RulesEngine
from inferenceengine import InferenceEngine
from record import Record
from tkinter.ttk import *
from tkinter import filedialog


class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.fe = FactsEngine()
        self.re = RulesEngine()
        self.ie = InferenceEngine(self.fe, self.re)
        self.grid()

        common_font = ('DejaVu', '12')
        mono_font = ('Monospace', '10')

        self.build_labels(0, 0)

        sides_range = [x for x in range(0, 6)]
        self.cboxes = [Combobox(self, values=sides_range,
                                font=common_font) for _ in range(0, 4)]

        for index, cbox in enumerate(self.cboxes):
            cbox.bind('<<ComboboxSelected>>', self.process)
            cbox.grid(column=index, row=1)

        self.label_result = Label(self, text="...", font=common_font)
        self.label_result.grid(column=0, row=2)
        self.fact_displayer = tk.Text(self, font=mono_font)
        self.fact_displayer.insert(tk.END, "{}")
        self.fact_displayer.grid(column=1, row=2, columnspan=3)

        self.save_button = Button(self, text="SAVE", command=self.save_db)
        self.save_button.grid(column=0, row=3, columnspan=2, sticky=tk.E+tk.W)
        self.load_button = Button(self, text="LOAD", command=self.load_db)
        self.load_button.grid(column=2, row=3, columnspan=2, sticky=tk.E+tk.W)

    def save_db(self):
        path = filedialog.asksaveasfilename()
        self.fe.save(path)

    def load_db(self):
        path = filedialog.askopenfilename()
        self.fe.load(path)
        self.update_fact_display()

    def build_labels(self, col, row):
        font = ('DejaVu', '10')
        labels = ["Sides", "Right Angles",
                  "Parallel Sides", "Same Length Sides"]
        for index, label in enumerate(labels):
            self.label_result = Label(
                self, text="Number of {}".format(label), font=font)
            self.label_result.grid(column=col+index, row=row)

    def process(self, event):
        for cbox in self.cboxes:
            if not cbox.get():
                cbox.set(0)
        record = Record(
            int(self.cboxes[0].get()),
            int(self.cboxes[1].get()),
            int(self.cboxes[2].get()),
            int(self.cboxes[3].get())
        )
        is_from_fact_db = self.ie.process(record)
        color = 'blue' if is_from_fact_db else 'green'
        self.label_result.config(text=str(record), foreground=color)
        self.update_fact_display()

    def update_fact_display(self):
        self.fact_displayer.delete(1.0, tk.END)
        content = json.dumps(self.fe.export(), indent=2)
        self.fact_displayer.insert(tk.END, content)
