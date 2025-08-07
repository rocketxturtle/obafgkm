import obafgkm.main as obafgkm
from obafgkm.plot import plotter
from obafgkm import DATADIR
import matplotlib.pyplot as plt
import os

def test_plot_tester(monkeypatch):
    plot_star = obafgkm.Star(4000, 2.0, "solar")
    stellar_info = plot_star.select_spectra()
    monkeypatch.setattr('builtins.input', lambda msg: 'y')
    plotter(stellar_info, input("Would you like to save the plot? (y/n): ").lower())
    plt.close('all')
    checker = os.path.exists(os.path.join(DATADIR, 'plots', f'teff_{4000}.0_logg_{2.0}_mh_0.0_spectrum.png'))
    expectcheck = True
    assert checker == expectcheck