#searching for an item in an ordered list
#this technique uses a binary search

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarySearch(item, itemList):
    #get the list size
    listSize = len(itemList) - 1
    #start at the two ends of list
    lowerIdx = 0
    upperIdx = listSize

    while lowerIdx <= upperIdx:
        pass
        #TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        #TODO: if item is found,return the index
        if itemList[midPt] == item:
            return midPt

        #TODO: otherwise get the next midpoint
        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else: 
            upperIdx = midPt - 1
        

    if lowerIdx > upperIdx:
        return None 
    
print(binarySearch(23, items))
print(binarySearch(87, items))
print(binarySearch(250, items))
