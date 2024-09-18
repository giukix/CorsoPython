words = ["Hello", "world", "!"]

print(words)

print(words[1])

empty_list = []

#operations
words[2] = "!!!"
print(words[2])

print("hello" in words)

#Functions
words.append("new word")
print(words)
print(len(words))

words.insert(1, "inserted item")
print(words)

print(words.index("!!!"))
#print(words.index("Non c'e'"))

# LIST SLICES
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[:7])
print(squares[7:])

#alternate
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

print(squares[1:-1]) # negative

print(squares[:-1]) # REVERSE A LIST

# altra istruzione di loop
for word in words:
    print("word item => " + word)

# for vs while    


########### SET ###########
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) # stampa non in ordine di creazione
nums.add(-7) ## invece di append (come nelle liste)
nums.remove(3)
print(nums)