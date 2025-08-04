import pandas as pd

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
        subselect = spec_list[(str(spec_list['effective_temperature'])==str(self.effective_temperature)) & (str(spec_list['surface_gravity'])==str(self.surface_gravity)) & (str(spec_list['metallicity'])==str(self.metallicity))]
        filepath = subselect['filepath']
        spectra = pd.read_txt(filepath)
