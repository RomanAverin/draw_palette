import sys

sys.path.append("..")

from draw_palette import utils, DrawPalette  # pylint: disable=import-error

colors = utils.import_palette("./colors.lua")
colors.sort(key=lambda x: x[0])

palette = DrawPalette(colors)
palette.render()
palette.save_image(image_name="palette.png")
