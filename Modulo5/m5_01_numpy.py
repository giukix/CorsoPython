import numpy as np

# 1. array(): crea un array a partire da una lista
lista = [1, 2, 3, 4, 5]
array_da_lista = np.array(lista)
print("Array da lista:", array_da_lista)

# 2. zeros(): crea un array di zeri di dimensione specificata
array_di_zeri = np.zeros((3, 4))  # 3 righe e 4 colonne
print("\nArray di zeri (3x4):\n", array_di_zeri)

# 3. ones(): crea un array di uno di dimensione specificata
array_di_uno = np.ones((2, 5))  # 2 righe e 5 colonne
print("\nArray di uno (2x5):\n", array_di_uno)

# 4. arange(): crea un array con valori da 0 a 9 con step 1
array_con_arange = np.arange(0, 10, 1)  # Da 0 a 9 (escluso il 10)
print("\nArray con arange da 0 a 9:", array_con_arange)

# 5. linspace(): crea un array con 5 valori equidistanti tra 0 e 1
array_con_linspace = np.linspace(0, 1, 5)
print("\nArray con linspace da 0 a 1 (5 valori equidistanti):", array_con_linspace)

######### OPERAZIONI VETTORIALI #############

import numpy as np

# Creiamo due array vettoriali
vettore1 = np.array([1, 2, 3])
vettore2 = np.array([4, 5, 6])

# Creiamo due array matriciali (matrici 2x2)
matrice1 = np.array([[1, 2], [3, 4]])
matrice2 = np.array([[5, 6], [7, 8]])

# 1. Somma vettoriale e matriciale
somma_vettori = vettore1 + vettore2
somma_matrici = matrice1 + matrice2

print("Somma vettoriale:", somma_vettori)
print("Somma matriciale:\n", somma_matrici)

# 2. Sottrazione vettoriale e matriciale
sottrazione_vettori = vettore1 - vettore2
sottrazione_matrici = matrice1 - matrice2

print("\nSottrazione vettoriale:", sottrazione_vettori)
print("Sottrazione matriciale:\n", sottrazione_matrici)

# 3. Prodotto vettoriale e matriciale (elemento per elemento)
prodotto_vettori = vettore1 * vettore2
prodotto_matrici = matrice1 * matrice2

print("\nProdotto vettoriale (elemento per elemento):", prodotto_vettori)
print("Prodotto matriciale (elemento per elemento):\n", prodotto_matrici)

# 4. Prodotto matriciale vero e proprio (prodotto di matrici)
prodotto_matriciale_vero = np.dot(matrice1, matrice2)

print("\nProdotto matriciale (vero e proprio):\n", prodotto_matriciale_vero)

########### FUNZIONI SOMMA E ALTRE ######## 

import numpy as np

# Creiamo un array NumPy
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 1. sum(): somma di tutti gli elementi dell'array
somma = np.sum(array)
print("Somma:", somma)

# 2. mean(): calcola la media degli elementi
media = np.mean(array)
print("Media:", media)

# 3. max(): trova il valore massimo
massimo = np.max(array)
print("Massimo:", massimo)

# 4. min(): trova il valore minimo
minimo = np.min(array)
print("Minimo:", minimo)

# 5. std(): calcola la deviazione standard
deviazione_standard = np.std(array)
print("Deviazione standard:", deviazione_standard)

### ALTRE FUNZIONI #######

import numpy as np

# Creiamo un array monodimensionale di 12 elementi
array_originale = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Array originale:", array_originale)

# 1. reshape(): cambia la forma dell'array senza alterarne i dati
array_reshaped = array_originale.reshape(3, 4)  # Reshape in una matrice 3x4
print("\nArray reshaped (3x4):\n", array_reshaped)

# 2. ravel(): appiattisce l'array in una dimensione
array_appiattito = array_reshaped.ravel()  # Appiattisce la matrice in un array monodimensionale
print("\nArray appiattito con ravel():", array_appiattito)


import numpy as np

# Creiamo due array 1D
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 1. concatenate(): concatenare due array lungo l'asse specificato
array_concatenato = np.concatenate((array1, array2))
print("Array concatenato:", array_concatenato)

# Creiamo due array 2D
array2D_1 = np.array([[1, 2], [3, 4]])
array2D_2 = np.array([[5, 6], [7, 8]])

# Concatenare lungo l'asse 0 (righe)
array_concatenato_asse0 = np.concatenate((array2D_1, array2D_2), axis=0)
print("\nConcatenazione lungo l'asse 0 (righe):\n", array_concatenato_asse0)

# Concatenare lungo l'asse 1 (colonne)
array_concatenato_asse1 = np.concatenate((array2D_1, array2D_2), axis=1)
print("\nConcatenazione lungo l'asse 1 (colonne):\n", array_concatenato_asse1)

# 2. split(): suddividere un array in sotto-array
array_da_suddividere = np.array([1, 2, 3, 4, 5, 6])

# Dividiamo l'array in 3 sotto-array
array_suddiviso = np.split(array_da_suddividere, 3)
print("\nArray suddiviso in 3 parti:", array_suddiviso)

# Suddividiamo una matrice lungo l'asse 0
array2D_da_suddividere = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
array2D_suddiviso_asse0 = np.split(array2D_da_suddividere, 2, axis=0)
print("\nMatrice suddivisa lungo l'asse 0 (righe):\n", array2D_suddiviso_asse0)

# Suddividiamo una matrice lungo l'asse 1
array2D_suddiviso_asse1 = np.split(array2D_da_suddividere, 2, axis=1)
print("\nMatrice suddivisa lungo l'asse 1 (colonne):\n", array2D_suddiviso_asse1)

