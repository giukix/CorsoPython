

############## CSV ################

import pandas as pd

url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
df_titanic = pd.read_csv(url)

# Visualizza le prime righe
print(df_titanic.head())

########### ISIN BETWEEN #####

data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Età': [25, 30, 22, 35, 28],
        'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Torino']}
df = pd.DataFrame(data)
print(df)

# Seleziona le righe dove la città è Roma o Milano
citta_selezionate = ['Roma', 'Milano']
df_filtrato = df[df['Città'].isin(citta_selezionate)]
print(df_filtrato)

# Seleziona le righe dove la città non è Roma né Milano
citta_escluse = ['Roma', 'Milano']
df_filtrato = df[~df['Città'].isin(citta_escluse)]
print(df_filtrato)

# Seleziona le righe dove l'età è compresa tra 25 e 30 anni
df_filtrato = df[(df['Età'] >= 25) & (df['Età'] <= 30)]
print(df_filtrato)

df_filtrato = df[df['Età'].between(25, 30)]
print(df_filtrato)

# Seleziona le righe dove la città è Roma o Milano e l'età è maggiore di 25
df_filtrato = df[(df['Città'].isin(['Roma', 'Milano'])) & (df['Età'] > 25)]

# Utilizzare query() per una sintassi più simile al linguaggio naturale
df_filtrato = df.query('Città == "Roma" and Età > 30')
print(df_filtrato)

# Seleziona le righe dove la colonna 'Città' non è nulla
df_filtrato = df[df['Città'].notnull()]

################## GROUPBY ETC ##############################

import pandas as pd

data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alice', 'Bob'],
        'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Torino', 'Roma', 'Milano'],
        'Età': [25, 30, 22, 35, 28, 27, 31],
        'Spese': [100, 150, 80, 200, 120, 90, 160]}
df = pd.DataFrame(data)
print(df)

# Raggruppa per città e calcola la media dell'età
grouped = df.groupby('Città')

media_eta = grouped['Età'].mean()
print(media_eta)


# Raggruppa per città e calcola la media dell'età e la somma delle spese
agg_funcs = {'Età': 'mean', 'Spese': 'sum'}
grouped = df.groupby('Città').agg(agg_funcs)
print(grouped)


# Definisci una funzione personalizzata per calcolare il range di età
def range_eta(x):
    return x.max() - x.min()

# Raggruppa per città e applica la funzione personalizzata
grouped = df.groupby('Città').agg({'Età': range_eta})
print(grouped)

# Crea una tabella pivot con città per righe e la media dell'età per colonne
pivot_table = pd.pivot_table(df, values='Età', index='Città', aggfunc='mean')
print(pivot_table)

# Crea una tabella pivot con città e nome per righe e la somma delle spese per colonne
pivot_table = pd.pivot_table(df, values='Spese', index=['Città', 'Nome'], aggfunc='sum')
print(pivot_table)

# Raggruppa per città e nome
grouped = df.groupby(['Città', 'Nome'])

# Definisci una funzione che restituisce una nuova colonna
def aggiungi_prefisso(x):
    return x + '_city'

# Applica la funzione a ciascuna colonna del gruppo
grouped = df.groupby('Città')['Città'].apply(aggiungi_prefisso)


########### ISNULL e altro ###############

import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [9, 10, 11, np.nan]}
df = pd.DataFrame(data)
print(df)


# Crea una DataFrame booleana indicando dove ci sono i valori mancanti
missing_data = df.isnull()
print("missing_data")
print(missing_data)

# Rimuove le righe con almeno un valore mancante
df_cleaned = df.dropna()
print("df_cleaned")
print(df_cleaned)

# Sostituisce i valori mancanti con 0
df_filled = df.fillna(0)
print(df_filled)

# Riempie i valori mancanti con il valore precedente (metodo forward fill)
df_filled = df.fillna(method='ffill')
print(df_filled)

# Riempie i valori mancanti con il valore successivo (metodo backward fill)
df_filled = df.fillna(method='bfill')
print(df_filled)

# Sostituisce i valori mancanti nella colonna 'A' con la media
df['A'] = df['A'].fillna(df['A'].mean())
print(df)
