#!/usr/bin/env python

import sys

from rqt_gui.main import Main
from rqt_plot_xy.plot import Plot

plugin = 'rqt_plot_xy.plot.Plot'
main = Main(filename=plugin)
sys.exit(main.main(standalone=plugin, plugin_argument_provider=Plot.add_arguments))
