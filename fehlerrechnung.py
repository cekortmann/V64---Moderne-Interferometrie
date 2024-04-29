import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  


A = unp.uarray([34,34,35,35,34,34,36,34,35,33],[0,0,0,0,0,0,0,0,0,0])

T = 10**-3
def n(max):
   return 1/(1-632.8*10**(-9)*A/(np.deg2rad(20)*np.deg2rad(10)*T))
    
def mean(x):
    a=0
    i=0
    while i<10:
        a+=x[i] 
        i+=1
    return a/10   

print('n der Brechungsindizes',n(A))
print('Durchschnitt der n', mean(n(A)))