import pandas as pd

# Creiamo una lista Python
lista = [10, 20, 30, 40, 50]

# Creiamo una Series da una lista
serie_da_lista = pd.Series(lista)

print("Series da lista:\n", serie_da_lista)

import numpy as np

# Creiamo un array NumPy
array = np.array([100, 200, 300, 400, 500])

# Creiamo una Series da un array NumPy
serie_da_array = pd.Series(array)

print("\nSeries da array NumPy:\n", serie_da_array)


# Creiamo un dizionario Python
dizionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Creiamo una Series da un dizionario (le chiavi diventano gli indici)
serie_da_dizionario = pd.Series(dizionario)

print("\nSeries da dizionario:\n", serie_da_dizionario)

######### SERIES INDEXING ########## 

import pandas as pd

# Creiamo una Series
serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Accesso a un elemento tramite indice
print("Elemento con indice 'b':", serie['b'])

# Accesso tramite posizione (indicizzazione intera)
print("Elemento in posizione 2:", serie[2])

# Slicing utilizzando etichette
sotto_serie_etichette = serie['b':'d']
print("\nSlicing con etichette ('b' a 'd'):\n", sotto_serie_etichette)

# Slicing utilizzando indici posizionali
sotto_serie_posizionale = serie[1:4]
print("\nSlicing con indici posizionali (da 1 a 3):\n", sotto_serie_posizionale)

# Eseguiamo operazioni matematiche su una Series

# Moltiplichiamo ogni elemento per 2
moltiplicata_per_2 = serie * 2
print("\nMoltiplicazione per 2:\n", moltiplicata_per_2)

# Sommiamo 10 a ogni elemento
somma_10 = serie + 10
print("\nSomma di 10 a ogni elemento:\n", somma_10)

# Calcoliamo la radice quadrata degli elementi
import numpy as np
radice_quadrata = np.sqrt(serie)
print("\nRadice quadrata degli elementi:\n", radice_quadrata)

