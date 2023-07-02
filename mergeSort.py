''''
Divide-and-conquer algorithm
Breaks a dataset into individual pieces and merges them
Uses recursion to operate on datasets
Performs well on large sets of data
In general has a performance of O(n log n) time complexity
'''
#Implement a merge sort with recursion

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftArr = dataset[:mid]
        rightArr = dataset[mid:]

        #TODO: recursively break down the arrays
        mergeSort(leftArr)
        mergeSort(rightArr)

        #TODO: now perform the merging
        i = 0 # index into the left array
        j = 0 #index into the right array
        k = 0 #index into merged array

        # TODO: while both arrays have content
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                    dataset[k] = leftArr[i]
                    i += 1
            else:
                    dataset[k] = rightArr[j]
                    j += 1
            k += 1
        #TODO: if the left array still has values, add them
        while i < len(leftArr):
             dataset[k] = leftArr[i]
             i += 1
             k += 1 
        # TODO: if the right array still has values,add them
        while j < len(rightArr):
             dataset[k] = rightArr[j]
             j += 1
             k += 1    

print(items)
mergeSort(items)
print(items)