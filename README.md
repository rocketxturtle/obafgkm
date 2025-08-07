# obafgkm 🌟

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16764379.svg)](https://doi.org/10.5281/zenodo.16764379)
[![PyPI version](https://badge.fury.io/py/obafgkm.svg?icon=si%3Apython)](https://badge.fury.io/py/obafgkm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An interactive Python tool for plotting representative stellar spectra across different spectral types and metallicities! Perfect for astronomy education, research, and stellar classification studies.

## 📖 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Parameters](#-parameters)
- [Examples](#-examples)
- [Data Sources](#-data-sources)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## ✨ Features

- **Interactive Stellar Spectra Plotting**: Generate and visualize synthetic stellar spectra with customizable parameters
- **Wide Parameter Range**: 
  - Effective temperatures: 3000K - 8000K
  - Surface gravities: log(g) = 0.0 - 5.0 dex
  - Metallicities: subsolar ([M/H]=-2.0), solar ([M/H]=0.0), and supersolar ([M/H]=0.5)
- **Dual Spectra Display**: View both normalized and unnormalized flux spectra
- **Spectral Line Markers**: Automatic labeling of important spectral features (Ca H/K, H-alpha, H-beta, Na D lines)
- **Export Capabilities**: Save high-resolution plots for publications and presentations
- **Pre-computed Spectra**: Fast loading from pre-synthesized MARCS/Korg models

## 🚀 Installation

### From PyPI (Stable Release)
```
pip install obafgkm
```

### From GitHub (Development Version)
```
# Latest development version
pip install git+https://github.com/rocketxturtle/obafgkm

# Or clone and install locally
git clone https://github.com/rocketxturtle/obafgkm.git
cd obafgkm
pip install -e .
```

### Dependencies
The package requires the following Python libraries:
- `numpy` - Numerical computations
- `pandas` - Data manipulation
- `astropy` - Astronomical utilities
- `matplotlib` - Plotting functionality

These will be automatically installed with the package.

## 🎯 Quick Start 

```
# In the terminal
python
import obafgkm.prompt as p
p.run()
```

This will launch an interactive session where you can select stellar parameters and generate spectra.

## 📊 Usage

### Interactive Mode
The simplest way to use `obafgkm` is through the terminal:

```
python
import obafgkm.prompt as p
p.run()
```

After which ou'll be prompted to select:
1. **Effective temperature** (3000, 4000, 5000, 6000, 7000, or 8000 K)
2. **Surface gravity** (log(g): 0.0, 1.0, 2.0, 3.0, 4.0, or 5.0 dex)
3. **Metallicity** ('subsolar', 'solar', or 'supersolar')

### Programmatic Usage
For more control, you can use the package by manually setting the `Star` object parameters:

```
import obafgkm.main as obafgkm
from obafgkm.plot import plotter

# Create a star object with specific parameters
star = obafgkm.Star(
    effective_temperature=5000,  # K
    surface_gravity=4.0,         # log(g) in dex
    metallicity='solar'          # or 'subsolar', 'supersolar'
)

# Generate spectra data
spectra_data = star.select_spectra()

# Plot the spectra (with optional save)
plotter(spectra_data, save=True)  # Set save=False to just display
```

### Custom Plotting
Access the raw spectral data for more detailed analysis:

```
import obafgkm.main as obafgkm
import matplotlib.pyplot as plt

star = obafgkm.Star(5000, 4.0, 'solar')
unnorm, norm, params, filename = star.select_spectra()

# unnorm and norm are numpy arrays with wavelength and flux columns
wavelength = norm[:, 0]  # Wavelength in Angstroms
flux = norm[:, 1]        # Normalized flux

# Create your own custom plot
plt.figure(figsize=(12, 6))
plt.plot(wavelength, flux)
plt.xlabel('Wavelength (Å)')
plt.ylabel('Normalized Flux')
plt.title(f'Teff={params[0]}K, log(g)={params[1]}, [M/H]={params[2]}')
plt.show()
```

## 🔢 Parameters

### Effective Temperature (Teff)
- Available values: 3000, 4000, 5000, 6000, 7000, 8000 K
- Covers spectral types from M to A stars

### Surface Gravity (log g)
- Available values: 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 dex
- From supergiants (low log g) to main sequence/subdwarfs (high log g)

### Metallicity ([M/H])
- **subsolar**: [M/H] = -2.0 (metal-poor)
- **solar**: [M/H] = 0.0 (solar abundance)
- **supersolar**: [M/H] = 0.5 (metal-rich)

## 🌟 Examples

### Example 1: Solar-like Star
```
import obafgkm.main as obafgkm
from obafgkm.plot import plotter

# Create a Sun-like star (G-type)

sun_like = obafgkm.Star(
    effective_temperature=6000,
    surface_gravity=4.0,
    metallicity='solar'
)
plotter(sun_like.select_spectra(), save=True)
```

### Example 2: Red Giant
```
import obafgkm.main as obafgkm
from obafgkm.plot import plotter

# K-type giant star

red_giant = obafgkm.Star(
    effective_temperature=4000,
    surface_gravity=1.0,
    metallicity='solar'
)
plotter(red_giant.select_spectra())
```

### Example 3: Metal poor Dwarf
```
import obafgkm.main as obafgkm
from obafgkm.plot import plotter

# Metal-poor dwarf star

subdwarf = obafgkm.Star(
    effective_temperature=5000,
    surface_gravity=5.0,
    metallicity='subsolar'
)
plotter(subdwarf.select_spectra())
```

## 📁 Project Structure

```
obafgkm/
├── __init__.py              # Package initialization and version info
├── main.py                  # Core Star class and spectra selection
├── plot.py                  # Plotting utilities and visualization
├── prompt.py                # Interactive user interface
├── rcparams.txt            # Matplotlib configuration settings
├── star_types.csv          # Database of available stellar spectra
├── normalized_spectra/     # Pre-computed normalized flux spectra
├── unnormalized_spectra/   # Pre-computed unnormalized flux spectra
└── plots/                  # Saved plot outputs (created on first save)
```

## 📈 Data Sources

The spectral data in this package were synthesized from:
- **Model Atmospheres**: MARCS model atmospheres
- **Spectral Synthesis**: Korg spectral synthesis code
- **Wavelength Range**: Full optical coverage
- **Resolution**: High-resolution synthetic spectra

Note: Current temperature range is limited to 3000-8000 K. Future releases aim to expand this range to include O and B type stars (>8000 K) and cooler M dwarfs (<3000 K).

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Extending temperature range beyond 3000-8000 K
- Adding more metallicity options
- Implementing additional spectral analysis tools
- Improving documentation and examples
- Adding unit tests

## 📚 Citation

If you use `obafgkm` in your research, please cite (bibtex):

```
@misc{obafgkm,
  author = {{Gozman, Katya}, {Sinha, Amaya}, {Schochet, Meir}, {Ramon, Lisha}},
  title = {obafgkm: Interactive Stellar Spectra Plotting Tool},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.16762220},
  url = {https://github.com/rocketxturtle/obafgkm}
}
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/rocketxturtle/obafgkm/blob/main/LICENSE) file for details.


## 🙏 Acknowledgments

- Created at [Code/Astro](https://semaphorep.github.io/codeastro/) workshop
- Spectral synthesis using [MARCS](https://marcs.astro.uu.se/) model atmospheres
- Synthetic spectra generated with [Korg](https://github.com/ajwheeler/korg.jl)
- Special thanks to the astronomy community for feedback and testing

## 🐛 Bug Reports & Questions

Found a bug or have a question? Please open an issue on our [GitHub Issues](https://github.com/rocketxturtle/obafgkm/issues) page.

## 🔮 Future Enhancements

- [ ] Extend temperature range to include O/B stars (>8000 K)
- [ ] Add ultra-cool dwarfs (<3000 K)
- [ ] Implement spectral classification algorithms
- [ ] Add interactive Jupyter widget interface
- [ ] Include additional spectral line identification tools
- [ ] Support for custom wavelength ranges
- [ ] Integration with observational data formats

---

**Happy stellar spectroscopy! 🔭✨**

*Remember: The universe is under no obligation to make sense to you, but these spectra might help!*
