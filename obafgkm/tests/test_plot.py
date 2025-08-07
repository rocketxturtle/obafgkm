import obafgkm.main as obafgkm
from obafgkm.plot import plotter
from obafgkm import DATADIR
import os

def plot_tester(monkeypatch):
    plot_star = obafgkm.Star(4000, 2.0, "solar")
    plot_star.select_spectra()
    monkeypatch.setattr(__name__, 'builtins.input', value=(lambda msg: 'y'))
    plotter(plot_star, input("Would you like to save the plot? (y/n): ").lower() == 'y')
    checker = os.path.exists(os.path.join(DATADIR, 'plots', f'teff_{4000}.0_logg_{2.0}_mh_0.0_spectrum.png'))
    expectcheck = True
    assert checker == expectcheck