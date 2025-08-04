import numpy as np
from main import Star
types=['O', 'B', 'A', 'F', 'G', 'K', 'M', 'Y' 'supersolar', 'solar', 'subsolar']

while True:
    print("Select spectral class: (options include: 'O', 'B', 'A', 'F', 'G', 'K', 'M', 'Y')")
    try:
        input_spec_type = input()
        if input_spec_type not in types:
            raise ValueError('stuff is not in content')
    except:
        print("Invalid input. Please enter a valid spectral type.")
        continue
    else:
        break
while True:
    print("Select [M/H]: (options include 'supersolar', 'solar', or 'subsolar')")
    try:
        input_metallicity = input()
        if input_metallicity not in types:
            raise ValueError('stuff is not in content')
    except ValueError:
        print("Invalid input. Please enter a valid metallicity.")
        continue
    else:
        break
plot_star = Star(input_spec_type, input_metallicity)

plot_star.select_spectra()

plot_star.plot_spectra()