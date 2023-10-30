import tkinter as tk
from run_simulation import run_simulation
from weapon_profile import Weapon
from weapon_stat_block import WeaponStatBlock


def submit():
    # test data
    weapon1 = Weapon("weapon1", 4, 3, 4, 0, 1, 5)
    weapon2 = Weapon("weapon2", 4, 3, 4, 0, 1, 5)
    weapon3 = Weapon("weapon3", 4, 3, 8, 1, 1, 5)
    weapons = [weapon1, weapon2, weapon3]

    run_simulation(frame, weapons)


def add_weapon_block(frame: tk.Frame):
    global weapon_block_index
    weapon_block_index += 1
    WeaponStatBlock.create_stat_block(frame, weapon_block_index)


def remove_weapon_block(frame: tk.Frame):
    all_rows = frame.grid_slaves()
    last_row = max(row.grid_info()["row"] for row in all_rows)
    if last_row > 1:
        global weapon_block_index
        weapon_block_index -= 1
        for row in all_rows:
            if row.grid_info()["row"] == last_row:
                row.grid_remove()


root = tk.Tk()
root.title("Warhammer 10E Damage Profile Comparison")

frame = tk.Frame(root)
frame.pack()

weapon_block_index = 1

weapon_info_frame = tk.LabelFrame(frame, text="Weapon Stats")
weapon_info_frame.grid(pady=10, padx=10, row=0, column=0)

weapon_info_controls = tk.LabelFrame(frame)
weapon_info_controls.grid(pady=10, padx=10, row=1, column=0)

WeaponStatBlock.create_stat_block(weapon_info_frame, weapon_block_index)

add_weapon_block_button = tk.Button(
    weapon_info_controls,
    text="Add Weapon",
    command=lambda frame=weapon_info_frame: add_weapon_block(frame),
)
add_weapon_block_button.grid(pady=10, padx=10, row=3, column=0)

remove_weapon_block_button = tk.Button(
    weapon_info_controls,
    text="Remove Weapon",
    command=lambda frame=weapon_info_frame: remove_weapon_block(frame),
)
remove_weapon_block_button.grid(pady=10, padx=10, row=3, column=1)

graph_frame = tk.LabelFrame(frame, text="Simulation Results")
graph_frame.grid(pady=10, row=1, column=0)

submit_button = tk.Button(root, text="Run Simulation", command=submit)
submit_button.pack(pady=10)

root.mainloop()
