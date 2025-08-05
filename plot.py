import numpy as np
import matplotlib.pyplot as plt

spec = np.loadtxt('codeastro_files/teff_4000.0_logg_0.0_mh_0.0.txt', skiprows=0)
wav, flux = (spec[:,0], spec[:,1])

plt.figure(figsize=(20, 6))
plt.plot(wav, flux, color='blue', label='Spectrum', lw=0.5)
plt.title('Spectrum Plot')
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux')
plt.yscale('log')
plt.grid(True)
plt.legend()
# plt.savefig('spectrum_plot.png')
plt.show()