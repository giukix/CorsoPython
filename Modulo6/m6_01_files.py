# Apertura di un file in modalità lettura
with open('C:/temp/small_titanic.csv', 'r') as file:
    # Lettura dell'intero contenuto del file
    contenuto_completo = file.read()
    print("*** Contenuto complesto ***")
    print(contenuto_completo)

with open('C:/temp/small_titanic.csv', 'r') as file:
    print("*** riga per riga ***")
    # Lettura riga per riga
    for riga in file:
        print(riga)

with open('C:/temp/small_titanic.csv', 'r') as file:
    # Lettura di tutte le righe in una lista
    print("*** Tutte le righe ***")
    righe = file.readlines()
    print(righe)



output_file = "C:/temp/output.txt"
print("*** Inizio scrittura " + output_file + " ***")
# Apertura di un file in modalità scrittura (sovrascrive il contenuto esistente)
with open(output_file, 'w') as file:
    file.write("Questa è la prima riga.\n")
    file.write("Questa è la seconda riga.")

# Apertura di un file in modalità append (aggiunge al contenuto esistente)
with open(output_file, 'a') as file:
    file.write("\nQuesta è una nuova riga.")    

print("*** Fine scrittura " + output_file + " ***")



############# OS #############

import os

# Definiamo il percorso completo
percorso_completo = os.path.join("C:/temp", "python")

# Creiamo le directory annidate (se non esistono già)
os.makedirs(percorso_completo)

print("La directory", percorso_completo, "è stata creata.")


####### SUBPROCESS #########

import subprocess

cmd = ['DIR', '/R']
result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
print(result.stdout)

##############

import subprocess

# Esegui una serie di comandi concatenati con pipe
result = subprocess.run(['DIR', '/R'], stdout=subprocess.PIPE, text=True)
#result = subprocess.run(['grep', 'md'], input=result.stdout, capture_output=True, text=True)
print(result.stdout)

###### SHUTIL #######

import shutil

shutil.copy("sorgente.txt", "destinazione.txt")

shutil.copytree("sorgente_directory", "destinazione_directory")

shutil.move("sorgente.txt", "destinazione.txt")

import os
os.remove("file_da_cancellare.txt")

os.rmdir("directory_vuota")

shutil.rmtree("directory_non_vuota")

os.rename("vecchio_nome.txt", "nuovo_nome.txt")

import os.path
if os.path.exists("mio_file.txt"):
    print("Il file esiste!")

###########

import shutil
import os

# Copiare tutti i file .txt da una directory all'altra
for file in os.listdir("sorgente"):
    if file.endswith(".txt"):
        shutil.copy(os.path.join("sorgente", file), "destinazione")

# Creare una nuova directory e spostarvi dentro tutti i file .py
os.makedirs("nuova_directory")
for file in os.listdir("."):
    if file.endswith(".py"):
        shutil.move(file, "nuova_directory")    