import tkinter as tk


class WeaponStatBlock:
    def create_stat_block(parent_frame: tk.Frame, i: int):
        new_weapon_frame = tk.Frame(parent_frame)
        new_weapon_frame.grid(row=i, column=0)

        name_label = tk.Label(new_weapon_frame, text="Weapon Name")
        name_label.grid(row=0, column=0)

        name_entry = tk.Entry(new_weapon_frame)
        name_entry.grid(pady=10, padx=10, row=0, column=0)

        attacks_label = tk.Label(new_weapon_frame, text="A")
        attacks_label.grid(row=0, column=1)

        attacks_entry = tk.Entry(new_weapon_frame)
        attacks_entry.grid(pady=10, padx=10, row=0, column=1)

        skill_label = tk.Label(new_weapon_frame, text="WS/BS")
        skill_label.grid(row=0, column=2)

        skill_entry = tk.Entry(new_weapon_frame)
        skill_entry.grid(pady=10, padx=10, row=0, column=2)

        strength_label = tk.Label(new_weapon_frame, text="S")
        strength_label.grid(row=0, column=3)

        strength_entry = tk.Entry(new_weapon_frame)
        strength_entry.grid(pady=10, padx=10, row=0, column=3)

        armor_pen_label = tk.Label(new_weapon_frame, text="AP")
        armor_pen_label.grid(row=0, column=4)

        armor_pen_entry = tk.Entry(new_weapon_frame)
        armor_pen_entry.grid(pady=10, padx=10, row=0, column=4)

        damage_label = tk.Label(new_weapon_frame, text="D")
        damage_label.grid(row=0, column=5)

        damage_entry = tk.Entry(new_weapon_frame)
        damage_entry.grid(pady=10, padx=10, row=0, column=5)

        count_label = tk.Label(new_weapon_frame, text="Count")
        count_label.grid(row=0, column=6)

        count_entry = tk.Entry(new_weapon_frame)
        count_entry.grid(pady=10, padx=10, row=0, column=6)
