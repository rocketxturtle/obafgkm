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
    unnormalized_spectra, normalized_spectra, parameters, filepath = spectra_tuple
    wav_unnormed, flux_unnormed = (unnormalized_spectra[:,0], unnormalized_spectra[:,1])
    wav_normed, flux_normed = (normalized_spectra[:,0], normalized_spectra[:,1])

    (teff, logg, m_h) = [parameters[i] for i in range(3)]

    fig, [ax1, ax2]  = plt.subplots(2, 1, figsize=(20, 14), layout='constrained')
    
    ax1.plot(wav_unnormed, flux_unnormed, color='blue', lw=0.5)
    ax2.plot(wav_normed, flux_normed, color='r', lw=0.5)

    fig.suptitle("Spectrum of T$_{eff}$=" + str(teff) + " , $\log$(g)=" + str(logg) + ", [M/H]=" + str(m_h), weight='bold')
    fig.supxlabel('Wavelength ($\AA$)')
    
    ax1.set_ylabel('Flux [erg/s/cm$^{5}$]')
    ax2.set_ylabel('Normalized Flux')
    ax1.set_yscale('log')
    [ax.grid(True) for ax in [ax1, ax2]]
    if save:
        if not os.path.exists('plots'):
            os.makedirs('plots')
        if(os.path.exists(os.path.join('plots', filepath.split('.txt')[0] + '_spectrum.png'))):
            print(f"This spectrum has already been saved! Look in plots/{filepath.split('.txt')[0]}_spectrum.png")
        else:
            plt.savefig(os.path.join('plots', filepath.split('.txt')[0] + '_spectrum.png'), dpi=300)
    plt.show()