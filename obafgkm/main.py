import pandas as pd
import numpy as np
import os

class Star(object):
    """
    A simulated Star that holds all the information needed to plot an example spectra.
    
    """

    def __init__(self, effective_temperature:int, surface_gravity:float, metallicity:str):
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
        spec_list = pd.read_csv('obafgkm/star_types.csv')
        subselect = spec_list[(spec_list['effective_temp']==self.effective_temperature) & (spec_list['surface_gravity']==self.surface_gravity) & (spec_list['metallicity']==self.metallicity)]
        filename = subselect['filepath'].values[0]
        unnormalized = np.loadtxt(os.path.join('obafgkm/unnormalized_spectra', filename), skiprows=0)
        normalized = np.loadtxt(os.path.join('obafgkm/normalized_spectra', filename), skiprows=0)
        parameters = (self.effective_temperature, self.surface_gravity, self.metallicity)
        return (unnormalized, normalized, parameters, filename)