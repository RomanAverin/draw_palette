import sys

sys.path.append("..")

from plotpalette import utils, PlotterPalette  # pylint: disable=import-error

colors = utils.import_palette("./colors.lua")
colors.sort(key=lambda x: x[0])

plotter = PlotterPalette(colors)
plotter.render()
plotter.save_image()
