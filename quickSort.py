'''
Divide-and-conquer algorithm,like the merge sort
Also uses recursion to perform sorting
Generally performs better than merge sort, O(n log n)
Operates in place on the data
Worst case is O(n2) when data is mostly sorted already
'''

#Implement a quicksort

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def quickSort(dataset, first, last):
    if first < last:
        #calculate te split point
        pivotIdx = partition(dataset, first, last)

        #now sort the two partitions
        quickSort(dataset, first, pivotIdx -1)
        quickSort(dataset, pivotIdx +1, last)

def partition(dataValues, first, last):
    #chose the first item as the pivot value
    pivotValue = dataValues[first]

    #establish the upper and lower indexes
    lower = first + 1
    upper = last 

    #start searching for the crossing point 
    done = False
    while not done:
        #TODO : advance the lower index
        while lower <= upper and dataValues[lower] <= pivotValue:
            lower += 1 

        #TODO: advance the upper index
        while dataValues[upper] >= pivotValue and upper >= lower:
            upper -= 1
       
        #TODO: if the two indexes cross, we have found the split point
        if upper < lower:
            done = True 
        else:
            temp = dataValues[lower]
            dataValues[lower] = dataValues[upper]
            dataValues[upper] = temp

    #when the split point os found, exchange the pivot value 
    temp = dataValues[first]
    dataValues[first] = dataValues[upper]
    dataValues[upper] = temp

    #return the split point index
    return upper

#test the merge sort with data 
print(items)
quickSort(items, 0, len(items) - 1)
print(items)