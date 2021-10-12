#Linked List implementation using python
class Node:
    def __init__(self,data):
        self.data=data
        self.nextval=None
class SingleLinkedList:
    def __init__(self):
        self.headval=None
    def printval(self):
        temp=self.headval
        while(temp):
         print(temp.data)
         temp=temp.nextval

    def countLinkedlist(self):
        #this countLinkedList function will count alll
        count=0 #set up the counter variables
        data_setup=self.headval #assigning data headval
        while(data_setup): #as long this this is true ,it will be run till the end
            count+=1 #set up counter
            print('Current LinkedList Node\t: ',data_setup.data,'\t Node Position ',count) #every time its going to print data
            data_setup=data_setup.nextval #moving to next
        print(count) #Print total number linked list

    def append(self,data):
       cur=self.headval
       new_node=Node(data)
       while(cur!=None):
           cur=cur.next
        cur.nextval=new_node

l=SingleLinkedList()
l.headval=Node(5)
e2=Node(6)
e3=Node(10)
e4=Node(12)
l.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
l.printval()
l.sumOfNode()
l.countLinkedlist()
