import sys

sys.path.append("..")

from draw_palette import utils, DrawPalette  # pylint: disable=import-error

colors = utils.import_palette("./example.lua")
colors.sort(key=lambda x: x[0])

CONFIG = {
    "spacing": 0.05,  # spacing between cells
    "dpi": 300,  # dpi of output image
    "rounding": 0.05,  # rounding of cell
    "max_column_num": 6,  # max colomns
    "cell_size": 3.0,  # size of color cell
    "fontfamily": "monospace",  # font family for any text
    "color_name_size": 14,  # font size of label color name
    "color_hex_size": 8,  # font size of label color HEX value
}

palette = DrawPalette(colors, config=CONFIG)
palette.render()
palette.save_image(image_name="palette.png")
