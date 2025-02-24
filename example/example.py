import sys

sys.path.append("..")

from plotpalette import utils, PlotterPalette

colors = utils.import_palette("./colors.lua")

plotter = PlotterPalette(colors)
plotter.render()
plotter.save_image()
