# First part for inventory manager. (Just a test)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newNode): 
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:  # Traverse until the last node
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteEnd(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:  # If there is only one node
            self.head = None
            return
        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = None  # Remove the last node

    def deleteHead(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next  # Move the head to the next node

    def deleteAt(self, position):
        sizeOfList = self.linkedListSize()  # Get the size of the list at the beginning

        if position == 0:
            self.deleteHead()
            return

        if position < 0 or position >= sizeOfList:  # Proper position check
            print(f"Position {position} is out of range.")
            return

        currentNode = self.head
        currentPosition = 0
        previousNode = None

        while currentNode is not None:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                return
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def printList(self):
        iterator = self.head
        if iterator is None:
            print("List is empty.")
        while iterator is not None:
            print(iterator.data)
            iterator = iterator.next

    def linkedListSize(self):
        iterator = self.head
        counter = 0
        while iterator is not None:
            iterator = iterator.next
            counter += 1
        return counter
    
    
     # Insert a new node at the end of the list
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head 
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    # Insert a new node at the beginning of the list
    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode

    # Insert a new node at a specific position
    def insertAt(self, newNode, position):
        if position < 0 or position > self.linkedListSize():
            print("Invalid position")
            return
        
        if position == 0:
            self.insertHead(newNode)
            return

        currentNode = self.head
        currentPosition = 0
        previousNode = None

        while currentNode and currentPosition < position:
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

        # Insert the new node between previousNode and currentNode
        newNode.next = currentNode
        previousNode.next = newNode


# Testing the LinkedList class
firstNode = Node("Apple")
secondNode = Node("Banana")
thirdNode = Node("Kiwi")
fourthNode = Node("Orange")

myLinkedList = LinkedList()
myLinkedList.append(firstNode)
myLinkedList.append(secondNode)
myLinkedList.append(thirdNode)
myLinkedList.append(fourthNode)

# we used printList, deleteend, deletehead insertAt, insetHead, insert,
print("Original list:")
myLinkedList.printList()

myLinkedList.deleteEnd()
print("\nAfter deleting the last element:")
myLinkedList.printList()

myLinkedList.deleteHead()
print("\nAfter deleting the head element:")
myLinkedList.printList()

myLinkedList.deleteAt(1)
print("\nAfter deleting the element at pos 1:")
myLinkedList.printList()

print("\ninserting a node at pos 1:")
myLinkedList.insertAt(fourthNode,1)
myLinkedList.printList()

print("\ninserting a node at head:")
myLinkedList.insertHead(firstNode)
myLinkedList.printList()

fithNode = Node("Wow!")
print("\ninserting a node at end of list:")
myLinkedList.insert(fithNode)
myLinkedList.printList()

print("\n")
size = myLinkedList.linkedListSize()
print("Total linked list size is: ", size)