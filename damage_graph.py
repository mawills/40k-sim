import matplotlib
import matplotlib.pyplot as plt
from config import (
    TOUGHNESS_CHARACTERISTICS,
    SAVE_CHARACTERISTICS,
    GRAPH_HEIGHT_IN,
    GRAPH_WIDTH_IN,
)


class DamageGraph:
    def render_graph(damage_results: dict):
        matplotlib.rcParams["figure.figsize"] = (GRAPH_HEIGHT_IN, GRAPH_WIDTH_IN)

        fig, ax = plt.subplots()

        x_axis = []
        for toughness in TOUGHNESS_CHARACTERISTICS:
            for save in reversed(SAVE_CHARACTERISTICS):
                x_axis.append("T%s,%s+" % (toughness, save))

        for weapon in damage_results.keys():
            ax.plot(
                x_axis,
                damage_results[weapon],
                label=weapon,
            )

        for value in x_axis:
            ax.axvline(x=value, color="grey", alpha=0.1, linestyle="-")

        ax.set_xticks(x_axis)
        ax.set_xticklabels(x_axis, rotation=90)

        ax.set_xlabel("Defender (Toughness, Save)")
        ax.set_ylabel("Average Damage")
        ax.legend()

        plt.show()
