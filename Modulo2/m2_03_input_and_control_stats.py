######## INPUT
x = input("Inserire un stringa => ")

print ("La stringa inserita e': "+x)

# Walrus operator (:=)
print (y := input("inserire il valore di y: "))

print("Il valore di y e' " + y)


num = int(input("inserire un numero: "))
print("il doppio del valore inserito e' " + str(num*2))

########## CONTROL STATS
if num < 10:
    print("Il numero inserito e' minore di 10")
else:
    print("Il numero inserito e' superiore a 10")
# si puo' usere elif in caso di piu' else

i = 0;
while i < 5:
    print("i="+str(i)) 
    i += 1

i = 0;
while i < 5:
    print("breaked i="+str(i)) 
    if i == 2:
        break    
    i += 1

# c'e' anche il continue

# il for lo vediamo dopo le liste

numbers = list(range(10)) # range(10) == range(0,10)
print (numbers)

numbers = list(range(0, 10, 2)) # step 
print (numbers)

for i in range(5):
    print(i)