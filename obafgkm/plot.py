from astropy.table import Table
import matplotlib.pyplot as plt
import os
import pathlib
from obafgkm import DATADIR, rcparams


os.chdir(pathlib.Path.cwd())
def set_rcparams():
    """Function to apply rcparams.txt file to all output plots

    Args:
        None
    Returns:
        None
    """
    tab = Table.read(rcparams, format='csv')
    for i in range(len(tab)):
        try:
            plt.rcParams[tab['key'][i]] = float(tab['val'][i])
        except ValueError:
            plt.rcParams[tab['key'][i]] = str(tab['val'][i])
    return

def plotter(spectra_tuple:tuple, save=False):
    """Core function to plot KORG spectra of a determined Star() object with specific Teff, log(g), and [M/H]

    Args:
        spectra_tuple (tuple): a tuple object that holds (Teff, log(g), [M/H]) values as determined when user_prompts.run() is ran
        save (bool): a boolean object to denote whether the plotted spectra should be saved (in the /plots folder) or not

    Returns:
        None
    """
    set_rcparams()
    unnormalized_spectra, normalized_spectra, parameters, filepath = spectra_tuple
    wav_unnormed, flux_unnormed = (unnormalized_spectra[:,0], unnormalized_spectra[:,1])
    wav_normed, flux_normed = (normalized_spectra[:,0], normalized_spectra[:,1])

    (teff, logg, m_h) = [parameters[i] for i in range(3)]

    fig, [ax1, ax2]  = plt.subplots(2, 1, figsize=(20, 14), layout='constrained')
    
    ax1.plot(wav_unnormed, flux_unnormed, color='blue', lw=0.5)
    ax2.plot(wav_normed, flux_normed, color='r', lw=0.5)

    fig.suptitle(r"Spectrum of T$_{\rm{eff}}$=" + str(teff) + r", $\log$(g)=" + str(logg) + ", [M/H]=" + str(m_h), weight='bold')
    fig.supxlabel(r'Wavelength ($\rm{\AA}$)')
    
    ax1.set_ylabel('Flux [erg/s/cm$^{5}$]')
    ax2.set_ylabel('Normalized Flux')
    ax1.set_yscale('log')
    [ax.grid(True) for ax in [ax1, ax2]]
    [ax.axvline(3968.47, c='orange', lw=0.5, label='Ca H') for ax in [ax1, ax2]]
    [ax.axvline(3933.66, c='orange', lw=0.5, label='Ca K') for ax in [ax1, ax2]]
    [ax.axvline(4861.34, c='k', lw=0.5, linestyle='-.', label=r'H $\beta$') for ax in [ax1, ax2]]
    [ax.axvline(5889.95, c='purple', lw=0.5, linestyle='--', label=r'Na D$_{2}$') for ax in [ax1, ax2]]
    [ax.axvline(5895.92, c='purple', lw=0.5, linestyle='--', label=r'Na D$_{1}$',) for ax in [ax1, ax2]]
    [ax.axvline(6562.81, c='k', lw=0.5, linestyle=':', label=r'H $\alpha$') for ax in [ax1, ax2]]
    [ax.legend(ncols=3, fontsize=12) for ax in [ax1, ax2]]
    if save:
        if not os.path.exists(os.path.join(DATADIR, 'plots')):
            os.makedirs(os.path.join(DATADIR, 'plots'))
        if(os.path.exists(os.path.join(DATADIR, 'plots', filepath.split('.txt')[0] + '_spectrum.png'))):
            print(f"This spectrum has already been saved! Look in plots/{filepath.split('.txt')[0]}_spectrum.png")
        else:
            plt.savefig(os.path.join(DATADIR, 'plots', filepath.split('.txt')[0] + '_spectrum.png'), dpi=300)
