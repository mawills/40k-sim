import matplotlib.pyplot as plt
from blume.table import table
from typing import List
from config import (
    BENCHMARKS,
    DEFENDER_UNIT_SIZE,
    DEFENDER_WOUND_PER_MODEL,
    WINDOW_HEIGHT_IN,
    WINDOW_WIDTH_IN,
)


class DamageTable:
    def render_table(
        data: List[List[float]], col_labels: List[str], row_labels: List[str]
    ):
        fig, ax = plt.subplots()

        cell_colors = []
        for row_label in row_labels:
            if row_label in BENCHMARKS:
                cell_colors.append(["#83e8fc"] * len(data[0]))
            else:
                cell_colors.append(["w"] * len(data[0]))

        tbl = table(
            plt.gca(),
            cellText=data,
            rowLabels=row_labels,
            colLabels=col_labels,
            cellColours=cell_colors,
            loc="center",
            cellLoc="center",
            bbox=[0, 0, 1, 1],
        )

        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)
        tbl.scale(1, 1)

        fig.set_size_inches(WINDOW_WIDTH_IN, WINDOW_HEIGHT_IN)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.box(on=None)

        ax.set_title(
            "Average (Mean) Damage Against Defending Units of %s Model(s) with %s Wound(s) Per Model"
            % (DEFENDER_UNIT_SIZE, DEFENDER_WOUND_PER_MODEL)
        )

        plt.show()
