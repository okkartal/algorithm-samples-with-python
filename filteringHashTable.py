#use a hashTable to filter out duplicate items

#define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

#TODO: create a hashTable to perform a filter
filter = dict()

#TODO: loop over each item and add to the hashTable 
for key in items:
    filter[key] = 0

#TODO: create a set from the resulting keys in the hashTable
result = set(filter.keys())
print(result)

#Value counting with hash table
#TODO: create a hashTable  object to hold the items and counts
counter = dict()

#TODO: iterate over each item and increment the count for each one
for item in items:
    if(item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

#print the results
print(counter)