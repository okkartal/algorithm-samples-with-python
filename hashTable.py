''''
Key-to-value mappings are unique
Hash tables are typically very fast
For small datasets,arrays are usually more efficient
Hash tables do not order entries in a predictable way
'''

#demonstrate hashTable usage

# TODO: create a hashTable all at once
items1 = dict({"key1" : 1, "key2": 2, "key3" : "three"})
print(items1)

# TODO: create a hashTable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = "three"
print(items2)

# TODO: try to access a nonexistent key
# print(items1["key6"]) -> KeyError

# TODO: replace an item
items2["key2"] = "two"
print(items2)

# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key: ",key, " value: ",value)