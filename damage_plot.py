import matplotlib.pyplot as plt
from config import (
    TOUGHNESS_CHARACTERISTICS,
    SAVE_CHARACTERISTICS,
    BENCHMARKS,
    WINDOW_HEIGHT_IN,
    WINDOW_WIDTH_IN,
    DEFENDER_UNIT_SIZE,
)


class DamagePlot:
    def render_plot(damage_results: dict):
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
            ax.axvline(x=value, color="grey", alpha=0.1, linestyle="--")

        for benchmark in BENCHMARKS:
            ax.axvline(benchmark, alpha=0.9, linestyle=":")

        ax.set_xticks(x_axis)
        ax.set_xticklabels(x_axis, rotation=90)

        ax.set_title(
            "Average (Mean) Damage Against Defending Units of %s Model(s)"
            % (DEFENDER_UNIT_SIZE)
        )
        ax.set_xlabel("Defender (Toughness, Save)")
        ax.set_ylabel("Damage")
        ax.legend()

        fig.set_size_inches(WINDOW_WIDTH_IN, WINDOW_HEIGHT_IN)

        plt.show()
