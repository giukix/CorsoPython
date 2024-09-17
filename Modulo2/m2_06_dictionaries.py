#Dictionaries are data structures used to map arbitrary keys to values.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

primary = {
    "red": [255, 0, 0], 
    "green": [0, 255, 0], 
    "blue": [0, 0, 255], 
}

print(primary["red"])
#print(primary["yellow"]) #KeyError

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)



pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary")) # gestisce la chiave assente con un valore di default

# AGGIUNGERE UN ELEMENTO
pairs["new_item"] = "XX"
print(pairs)