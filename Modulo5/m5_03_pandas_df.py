import pandas as pd

# Creiamo un dizionario con i dati
dati = {
    'Nome': ['Anna', 'Luca', 'Marco'],
    'Età': [23, 29, 31],
    'Città': ['Roma', 'Milano', 'Napoli']
}

# Creiamo un DataFrame dal dizionario
df_dizionario = pd.DataFrame(dati)

# Visualizziamo il DataFrame
print(df_dizionario)

# Creiamo una lista di liste
dati_liste = [
    ['Anna', 23, 'Roma'],
    ['Luca', 29, 'Milano'],
    ['Marco', 31, 'Napoli']
]

# Creiamo un DataFrame dalle liste e specifichiamo i nomi delle colonne
df_liste = pd.DataFrame(dati_liste, columns=['Nome', 'Età', 'Città'])

# Visualizziamo il DataFrame
print(df_liste)

####### METODI DI ACCESSO ##############

import pandas as pd

# Creiamo un DataFrame di esempio
data = {
    'Nome': ['Anna', 'Luca', 'Marco'],
    'Età': [23, 29, 31],
    'Città': ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Accesso a una riga tramite etichetta
print("Accesso alla riga 'b':\n", df.loc['b'])

# Accesso a un singolo valore tramite etichetta riga e colonna
print("\nAccesso a 'Età' nella riga 'c':", df.loc['c', 'Età'])

# Accesso a più righe e colonne usando slicing con etichette
print("\nAccesso a righe da 'a' a 'b' e colonne 'Nome' e 'Età':\n", df.loc['a':'b', ['Nome', 'Età']])

# Accesso a una riga tramite posizione intera
print("\nAccesso alla riga in posizione 1:\n", df.iloc[1])

# Accesso a un singolo valore tramite posizione riga e colonna
print("\nAccesso al valore nella riga 2 e colonna 1:", df.iloc[2, 1])

# Accesso a più righe e colonne usando slicing con posizioni
print("\nAccesso a righe 0 e 1 e colonne 0 e 1:\n", df.iloc[0:2, 0:2])

# Accesso a un singolo valore tramite etichetta riga e colonna
print("\nAccesso rapido a 'Città' nella riga 'b':", df.at['b', 'Città'])

# Accesso a un singolo valore tramite posizione riga e colonna
print("\nAccesso rapido al valore in posizione [2, 2]:", df.iat[2, 2])

######### OPERAZIONI DI BASE ###############

import pandas as pd

# Creiamo un DataFrame di esempio
data = {
    'Nome': ['Anna', 'Luca', 'Marco'],
    'Età': [23, 29, 31],
    'Città': ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data)

# Aggiungiamo una nuova colonna 'Professione'
df['Professione'] = ['Ingegnere', 'Dottore', 'Artista']

# Visualizziamo il DataFrame aggiornato
print("DataFrame dopo aver aggiunto la colonna 'Professione':\n", df)

# Rinominiamo la colonna 'Età' in 'Età (anni)'
df.rename(columns={'Età': 'Età (anni)'}, inplace=True)

# Visualizziamo il DataFrame aggiornato
print("\nDataFrame dopo aver rinominato la colonna 'Età':\n", df)


# Filtriamo le righe in cui 'Età (anni)' è maggiore di 25
filtro = df[df['Età (anni)'] > 25]

# Visualizziamo il DataFrame filtrato
print("\nDataFrame filtrato (Età > 25):\n", filtro)

# Ordiniamo il DataFrame in base alla colonna 'Età (anni)'
df_sorted = df.sort_values(by='Età (anni)', ascending=True)

# Visualizziamo il DataFrame ordinato
print("\nDataFrame ordinato per 'Età (anni)':\n", df_sorted)
