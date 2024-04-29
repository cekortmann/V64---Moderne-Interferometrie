import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray

# Plot 1:
phi, min1, min2, min3, Min, max1, max2, max3, Max, K= np.genfromtxt('Kontrast.txt', unpack=True, skip_header=1)
            # Normierung 

# für den initial guess bei curvefit()
n = len(phi)                             # Anzahl der Daten
#mean = sum(nu*U)/n                      # Mittelwert
#sigma = np.sqrt(sum(U*(nu - mean)**2))  # Standardabweichung

# Ausgleichsrechung nach Gaußverteilung
def g(x,a,d):
    return np.sqrt(a*np.sin(np.deg2rad(2*x-d))**2)     # b = 2*sigma**2

def t(x):
    return np.sqrt(np.sin(2*x)**2)

para, pcov = curve_fit(g, phi, K)
a,d = para
pcov = np.sqrt(np.diag(pcov))
fa, fd = pcov
ua = ufloat(a, fa) 
ud = ufloat(d, fd)

print('ua:', ua)
print('ud:', ud)

xx = np.linspace(0, 180, 10**6)

plt.plot(phi, K, 'xr', markersize=6 , label = 'Messdaten', alpha=0.5)
#plt.plot(xx, t(xx), '-g', linewidth = 1, label = 'Theoriekurve', alpha=0.5)
plt.plot(xx, g(xx, *para), '-b', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.xlabel(r'$\phi \, / \, \mathrm{°}$')
plt.ylabel(r'$K$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
#plt.xlim(22, 40)
#plt.ylim(-0.05, 1.05)

plt.savefig('build/kontrast.pdf', bbox_inches = "tight")
plt.clf() 
