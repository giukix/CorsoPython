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