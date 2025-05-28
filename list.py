class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linkelist:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def _inset_at_Begining(self,newdata):
            newNode = Node(newdata)
            newNode.next= self.head
            self.head =newNode

l1=linkelist()
l1.head = Node("toyota")
l2= Node("bmw")
l3=Node("audi")
l4=Node("lambogini")
l1.head.next=l2
l2.next=l3
l3.next=l4
l1.listprint()

l1.listprint()
print("")
l1._inset_at_Begining("benz")
l1.listprint()
l1._inset_at_Begining("car")
print("")
l1.listprint()