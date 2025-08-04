import pandas as pd

class Star(object):
    """
    A simulated Star that holds all the information needed to plot an example spectra.
    
    """

    def __init__(self, spectral_class, metallicity):
        """
        Function that initializes our star and the three selected parameters needed to determined
        which spectra is generated
        """

        self.spectral_class = spectral_class\
        self.metallicity = metallicity

    def select_spectra(self):
        """
        This function selects a given spectra to plot given the instatiated values for the
        star in question
        """
        spec_list = pd.read_csv('(#name of csv with all the sim spectra info#)')
        subselect = spec_list[(str(spec_list['spectral class'])==str(self.spectral_class)) 
                            & (str(spec_list['metallicity'])==str(self.metallicity))]
        filepath = subselect['(#name of column holding file names)#']
        spectra = pd.read_csv(filepath)