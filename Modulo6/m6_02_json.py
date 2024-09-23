import json

# Crea un dizionario
data = {'name': 'Alice', 'age': 30, 'city': 'Roma'}

# Scrive il dizionario in un file JSON
nomefile_json = 'C:/temp/dati.json'
with open(nomefile_json, 'w') as f:
    json.dump(data, f)

# Legge il file JSON e lo converte in un dizionario
with open(nomefile_json, 'r') as f:
    data = json.load(f)

# Stampa il contenuto del dizionario
print(data)


import json

# Crea una lista
lista = [1, 2, 3, 'quattro']

# Converte la lista in una stringa JSON
stringa_json = json.dumps(lista)
print(stringa_json)

"""
json.dumps(): Restituisce una stringa JSON. È utile quando vuoi manipolare la stringa JSON prima di salvarla o inviarla.
json.dump(): Scrive direttamente la rappresentazione JSON in un file. È più efficiente per salvare grandi quantità di dati
Differenza tra loads() e load():

json.loads(): Prende una stringa JSON come input e restituisce un oggetto Python.
json.load(): Legge un file JSON e restituisce il contenuto come un oggetto Python.
"""