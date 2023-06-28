class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        if currentNode is None:
            print("\n\n**** Your List is Empty ****\n\n")
        else:
            print("\n**** Your List is ****")
            while True:
                if currentNode is None:
                    break
                print(currentNode.value,end = "")
                currentNode = currentNode.next
                print(end=" >> ") if currentNode is not None else None

linkList = LinkedList()
while True:
    choice = int(input("\nPress 1 to insert element into the list\nPress 2 to print the list\nPress 0 to Exit\n"))
    if choice == 1:
        element = input("Eneter your element : ")
        node = Node(element)
        linkList.insert(node)
    elif choice == 2:
        linkList.printList()
    elif choice == 0:
        break
    pass


    