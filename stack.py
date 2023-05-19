class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def prepend(self, value):
        newNode = Node(value)
        curNode = self.head
        curNode.prev = newNode
        newNode.next = curNode
        self.head = newNode

    def straighttraversal(self):
        curNode = self.head
        if curNode is None :
            print("Doublu Linked list is Empty")

        else:
            print("Contents of Doubly Linked list are")
            while curNode is not None:
                print(curNode.data, end="\t")
                curNode = curNode.next

    def Reversetraversal(self):
        curNode = self.tail
        if curNode is None:
            print("empty")

        else:
            print("doubly Linked list items are")
            while curNode is not None:
                print(curNode.data, end="\t")
                curNode = curNode.prev

a = Linkedlist(90)
a.prepend(80)
a.prepend(70)
a.straighttraversal()
print()
print("reverse order")
a.Reversetraversal()