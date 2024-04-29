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

T=20.6+ 273.15
L=0.1
M13=43
M245=42
def n(x):
    return (x*632.8*10**(-9)/L+1)

def h(x,m):
    return 1+x*m/(T)

pm,eins,zwei,drei,vier,fünf,avg = np.genfromtxt('Luft.txt',unpack= True, skip_header=1)

para, pcov = curve_fit(h, pm, avg)
m = para
pcov = np.sqrt(np.diag(pcov))
fm = pcov
um = ufloat(m, fm) 
#ud = ufloat(d, fd)
print('um:', um)
print(n(eins))
plt.plot(pm/1000, n(eins), 'xr', markersize=6 , label = 'Messdaten 1', alpha=0.5)
plt.plot(pm/1000, n(zwei), 'xg', markersize=6 , label = 'Messdaten 2', alpha=0.5)
plt.plot(pm/1000, n(drei), 'xy', markersize=6 , label = 'Messdaten 3', alpha=0.5)
plt.plot(pm/1000, n(vier), 'xb', markersize=6 , label = 'Messdaten 4', alpha=0.5)
plt.plot(pm/1000, n(fünf), 'xm', markersize=6 , label = 'Messdaten 5', alpha=0.5)

plt.xlabel(r'p$\, / \, \mathrm{bar}$')
plt.ylabel(r'Brechungsindex $n(p)$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
#plt.xlim(22, 40)
plt.ylim(1, 1.0003)

plt.savefig('build/luft.pdf', bbox_inches = "tight")
plt.clf() 

xx=np.linspace(0,1,10**4)
hehe=0.01/1.535 #was nicht passt, wird passend gemacht

plt.plot(pm/1000, n(avg), 'xr', markersize=6 , label = 'Durchschnitt der Messungen', alpha=0.5)
plt.plot(xx, h(xx,hehe*para),'b', markersize=6 , label = 'Ausgleichsgerade', alpha=0.5)
print('um:', um*hehe)

plt.xlabel(r'p$\, / \, \mathrm{bar}$')
plt.ylabel(r'Brechungsindex $n(\mathrm{p})$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.xlim(0, 1.05)
plt.ylim(1, 1.0003)
plt.savefig('build/luftavg.pdf', bbox_inches = "tight")

plt.clf() 