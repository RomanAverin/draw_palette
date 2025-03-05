"""
Main lib class PlotterPalette

"""

from matplotlib.patches import FancyBboxPatch
from matplotlib.figure import Figure
from .config import DEFAULT_CONFIG
from .utils import get_text_color


class PlotterPalette:
    """
    A class for rendering a palette of colors specified as a dictionary.
    Input parameters:
        - colors(dict) dicrionaty of colors

        example:
        { "black": "#000000", "white": "#ffffff" }

    """

    def __init__(self, colors: list, config=None):
        self.config = {**DEFAULT_CONFIG, **(config or {})}
        self.palette = colors
        self.colors_num = len(colors)
        self.__create_figure()

    def __create_figure(self):
        """Initialize matplotlib figure."""
        self.rows_num = (
            self.colors_num + self.config["max_column_num"] - 1
        ) // self.config["max_column_num"]

        self.figure = Figure(
            figsize=(
                self.colors_num,
                4 * self.rows_num * (self.config["cell_size"] + self.config["spacing"]),
            )
        )
        self.ax = self.figure.subplots()
        self.ax.set_aspect("equal")
        self.ax.axis("off")

    def render(self):
        """
        Rendering palette

        """
        rect_width = self.config["cell_size"] - 2 * self.config["spacing"]
        rect_size = rect_width - self.config["spacing"]

        for index, color_pair in enumerate(self.palette):
            color_name = color_pair[0]
            color_hex_value = color_pair[1]

            row = index // self.config["max_column_num"]
            col = index % self.config["max_column_num"]
            y_pos = (self.rows_num - 1 - row) * (
                self.config["cell_size"] + self.config["spacing"]
            )
            x_pos = col * (self.config["cell_size"] + self.config["spacing"])

            rect = FancyBboxPatch(
                (x_pos + self.config["spacing"], y_pos + self.config["spacing"]),
                rect_size,
                rect_size,
                boxstyle=f"round,pad={self.config['spacing']},rounding_size={self.config['rounding']}",
                facecolor=color_hex_value,
                edgecolor="none",
            )
            self.ax.add_patch(rect)

            # Color name
            self.ax.text(
                x_pos + self.config["cell_size"] / 2,
                y_pos + self.config["cell_size"] / 2,
                color_name,
                ha="center",
                va="center",
                color=get_text_color(color_hex_value),
                fontsize=self.config["color_name_size"],
                wrap=True,
                fontfamily=self.config["fontfamily"],
            )

            # HEX-color
            self.ax.text(
                x_pos + self.config["cell_size"] - 0.2,
                y_pos + 0.1,
                color_hex_value.upper(),
                ha="right",
                va="bottom",
                color=get_text_color(color_hex_value),
                fontsize=self.config["color_hex_size"],
                alpha=0.8,
                fontfamily=self.config["fontfamily"],
            )

        self.ax.set_xlim(
            0,
            self.config["max_column_num"]
            * (self.config["cell_size"] + self.config["spacing"]),
        )
        self.ax.set_ylim(
            0,
            self.rows_num * (self.config["cell_size"] + self.config["spacing"]),
        )

    def save_image(self, image_name="colors_palette.png"):
        """
        Save image to the disk

            Input parameters:
                - image_name(str) image path and name, default 'colors_palette.png'
                  example: './pallet.png'
        """

        self.figure.savefig(
            image_name,
            transparent=True,
            dpi=self.config["dpi"],
            bbox_inches="tight",
            pad_inches=0.1,
        )
