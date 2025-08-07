import obafgkm.main as obafgkm
from obafgkm.plot import plotter

types=[3000, 4000, 5000, 6000, 7000, 8000, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
metals = ['supersolar', 'solar', 'subsolar']

def run():
    """Function to run our prompter program to plot a specific spectra

    Args:
        None
    Returns:
        None
    """
    while True:
        print("Select effective temperature class: (options are: '3000', '4000', '5000', '6000', '7000', '8000')")
        try:
            input_teff = int(input())
            if input_teff not in types:
                raise ValueError('stuff is not in content')
        except:
            print("Invalid input. Please enter a valid spectral type.")
            continue
        else:
            break
    while True:
        print("Select surface gravity: (options include log(g) [dex] values of: '0.0', '1.0', '2.0', '3.0', '4.0', '5.0')")
        try:
            input_logg = float(input())
            if input_logg not in types:
                raise ValueError('stuff is not in content')
        except ValueError:
            print("Invalid input. Please enter a valid metallicity.")
            continue
        else:
            break
    while True:
        print("Select [M/H]: (options include 'supersolar' ([M/H]=0.5), 'solar' ([M/H]=0.0), or 'subsolar' ([M/H]=-2.0))")
        try:
            input_metallicity = str(input())
            if input_metallicity not in metals:
                raise ValueError('stuff is not in content')
        except ValueError:
            print("Invalid input. Please enter a valid metallicity.")
            continue
        else:
            break
    plot_star = obafgkm.Star(input_teff, input_logg, input_metallicity)

    stellar_info = plot_star.select_spectra() # four value tuple

    plotter(stellar_info, input("Would you like to save the plot? (y/n): ").lower())