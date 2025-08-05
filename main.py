import pandas as pd
import numpy as np
import os

class Star(object):
    """
    A simulated Star that holds all the information needed to plot an example spectra.
    
    """

    def __init__(self, effective_temperature, surface_gravity, metallicity):
        """
        Function that initializes our star and the three selected parameters needed to determined
        which spectra is generated
        """

        self.effective_temperature = effective_temperature
        self.surface_gravity = surface_gravity
        self.metallicity = metallicity

    def select_spectra(self):
        """
        This function selects a given spectra to plot given the instatiated values for the
        star in question
        """
        spec_list = pd.read_csv('star_types.csv')
        subselect = spec_list[(spec_list['effective_temp']==self.effective_temperature) & (spec_list['surface_gravity']==self.surface_gravity) & (spec_list['metallicity']==self.metallicity)]
        filepath = subselect['filepath'].values[0]
        spectra = np.loadtxt(os.path.join('spectra', filepath), skiprows=0)
        return (spectra, filepath)
