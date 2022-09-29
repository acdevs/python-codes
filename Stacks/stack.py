class Stack:
    def __init__(self):
        self.stack = []
        
    def isempty(self):
        if self.stack==[]:
            return True
        else:
            return False
    
    def push(self, dataitem):
        if dataitem not in self.stack:
            self.stack.append(dataitem)
            return True
        else:
            return False
        
    def pop(self):
        if len(self.stack) = 0:
            return ("UnderFlow !")
        else:
            return self.stack.pop()
        
    def display(self):
        if self.isempty():
            return ("Stack is Empty!")
        else:
            return (list(self.stack))
        
    def view(self):
        print("Stack Items\n")
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])
            
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.stack[-1]
        
