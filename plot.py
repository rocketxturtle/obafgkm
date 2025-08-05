from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import os
import pathlib

os.chdir(pathlib.Path.cwd())
def set_rcparams():
    tab = Table.read('rcparams.txt', format='csv')
    for i in range(len(tab)):
        try:
            plt.rcParams[tab['key'][i]] = float(tab['val'][i])
        except ValueError:
            plt.rcParams[tab['key'][i]] = str(tab['val'][i])
    return

def plotter(spectra_tuple, save=False):
    """
    Plotting function to display a spectra graphically
    
    """
    set_rcparams()
    spectra, filepath = spectra_tuple
    wav, flux = (spectra[:,0], spectra[:,1])
    fig, ax  = plt.subplots(1, 1, figsize=(20, 6), layout='constrained')
    ax.plot(wav, flux, color='blue', label='Spectrum', lw=0.5)
    fig.suptitle('Spectrum Plot')
    fig.supxlabel('Wavelength ($\AA$)')
    fig.supylabel('Flux')
    ax.set_yscale('log')
    ax.grid(True)
    ax.legend()
    if save:
        if not os.path.exists('plots'):
            os.makedirs('plots')
        plt.savefig(os.path.join('plots', filepath.split('.txt')[0] + '_spectrum.png'), dpi=300)
    plt.show()