import os

__version__ = "0.1.3"

# set Python env variable to keep track of example data dir
DATADIR = os.path.dirname(__file__)
unnormed_data = os.path.join(DATADIR, "unnormalized_spectra/")
normed_data = os.path.join(DATADIR, "normalized_spectra/")
STARCSV = os.path.join(DATADIR, "star_types.csv")
rcparams = os.path.join(DATADIR, "rcparams.txt")


print("You have successfully imported obafgkm!")
print("The spectra in this package were synthesized from MARCS model atmospheres using Korg. Due to this are currently only available within [3000, 8000] K. Future releases will aim to expand this range.")
