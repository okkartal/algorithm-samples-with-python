''''
Collection that supports push and pop operations
The last item pushed is the first one popped
Practical Applications : Expression processing , Backtracking : browser back stack 
'''
#try out the Python stack functions

# TODO: create a new empty stack
stack = []

# TODO: push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# TODO: print the stack contents
print(stack)

#TODO: pop an item off the stack
x = stack.pop()
print(x) #4
print(stack) #1,2,3