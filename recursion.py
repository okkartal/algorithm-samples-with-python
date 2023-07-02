''''
Need to have a breaking condition
This prevents infinite loops and eventual crashes
Each time the function is called,the old arguments are saved
This is called the "call stack"
'''

def countdown(x):
    if x == 0:
        print("Done!")
        return 
    else:
        print(x, "...")
        countdown(x-1) 

countdown(5)