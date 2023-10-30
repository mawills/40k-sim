import tkinter as tk
from tkinter import ttk
from typing import List
from config import TOUGHNESS_CHARACTERISTICS, SAVE_CHARACTERISTICS


class DamageGraph:
    def render_graph(
        parent_frame: tk.Frame,
        weapon_names: List[str],
        weapon_damage: List[List[float]],
    ):
        column_headings = ["Toughness, Save"] + weapon_names
        table = ttk.Treeview(
            parent_frame,
            columns=column_headings,
            show="headings",
            height=len(TOUGHNESS_CHARACTERISTICS) * len(SAVE_CHARACTERISTICS),
        )

        table.heading(0, text="Toughness, Save")
        table.column(0, width=100, anchor="center")

        for i, weapon_name in enumerate(weapon_names):
            table.heading(i + 1, text=weapon_name)
            table.column(i + 1, width=100, anchor="center")

        i = 0
        for toughness in TOUGHNESS_CHARACTERISTICS:
            for save in reversed(SAVE_CHARACTERISTICS):
                row = ["%s,%s+" % (toughness, save)] + weapon_damage[i]
                table.insert("", "end", values=row)
                i += 1

        table.grid(row=1, column=0)
