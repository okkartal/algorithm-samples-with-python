#Linked list example

#the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None 

    def get_data(self):
        return self.val 
    
    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

#The LinkedList class 
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head 
        self.count = 0

    def get_count(self):
        return self.count 
    
    def insert(self, data):
        #TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        #TODO: find the first item with a given value 
        item = self.head 
        while(item != None):
            if item.get_data() == val:
                return item 
            else:
                item = item.get_next()

        return None 
    
    def deleteAt(self, idx):
        #TODO: delete an item at given index 
        if idx > self.count - 1:
            return
        
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    
    def dump_list(self):
        tempNode = self.head 
        while (tempNode != None):
            print("Node: ", tempNode.get_data())
            tempNode = tempNode.get_next()

''''
Collection of data elements,called nodes
Contain reference to the next node in the list
Hold whatever data the application needs
Elements can be easily inserted and removed
Underlying memory does not need to be reorganized
Can not do constant-time random item access
Item lookup is linear in time complexity (O(n))
'''
#create a linked list and insert some items 
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

#exercise the list
print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(13))
print("Finding item: ", itemList.find(78))

#delete an item
itemList.deleteAt(3)
print("Item count: ", itemList.get_count())
print("Finding items: ", itemList.find(38))
itemList.dump_list()