 import sys
class Stack ():
    def __init__(self):
        self.items=[]
    def push (self,item):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s1= Stack()
decNum= int(raw_input("Enter the decimal num : "))
while decNum!=0:
    newNum= decNum%2
    decNum = decNum//2
    s1.push(newNum)
while s1.size() != 0:
    a=s1.pop()
    sys.stdout.write(str(a))
sys.stdout.flush()