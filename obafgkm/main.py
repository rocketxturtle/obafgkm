import pandas as pd
import numpy as np
import os
import pathlib
from obafgkm import unnormed_data, normed_data, STARCSV

os.chdir(pathlib.Path.cwd())
class Star(object):
    """The core class for obafgkm, which holds the parameters needed to choose the spectra for plotting 
     
     Attributes:
        effective_temperature (int): KORG effective temperature for selected star (in Kelvin)
        surface_gravity (float): KORG surface gravity for selected star (in dex, re: 10**surface_gravity)
        metallicity (str): KORG metallicity for selected star ('solar','subsolar', & 'supersolar' with values of -2.0, 0.0, and 0.5 for [M/H]

    """

    def __init__(self, effective_temperature:int, surface_gravity:float, metallicity:str):
        """__init__ method for our Star objects
       
        Args:
            effective_temperature (int): KORG effective temperature for selected star (in Kelvin)
            surface_gravity (float): KORG surface gravity for selected star (in dex, re: 10**surface_gravity)
            metallicity (str): KORG metallicity for selected star ('solar','subsolar', & 'supersolar' with values of -2.0, 0.0, and 0.5 for [M/H]
        """
        self.effective_temperature = effective_temperature
        self.surface_gravity = surface_gravity
        self.metallicity = metallicity

    def select_spectra(self):
        """this method selects the spectra file for plotting
       
        Args:
            None
        """
        spec_list = pd.read_csv(STARCSV)
        subselect = spec_list[(spec_list['effective_temp']==self.effective_temperature) & (spec_list['surface_gravity']==self.surface_gravity) & (spec_list['metallicity']==self.metallicity)]
        filename = subselect['filepath'].values[0]
        unnormalized = np.loadtxt(os.path.join(unnormed_data, filename), skiprows=0)
        normalized = np.loadtxt(os.path.join(normed_data, filename), skiprows=0)
        parameters = (self.effective_temperature, self.surface_gravity, self.metallicity)
        return (unnormalized, normalized, parameters, filename)
