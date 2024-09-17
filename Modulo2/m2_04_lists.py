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