class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return " the CDLL created!"

    def insertion(self, value, location):
        if self.head is None:
            return "doesn't exist."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
        return "the node has been inserted."

    def traversal(self):
        if self.head is None:
            return "there is not any nodes."
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def Reverse_Traversal(self):
        if self.head is None:
            return "there is not any list here."
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchValue(self, nodeValue):
        if self.head is None:
            return "there is not any list here."
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "the value doesn't exist."
                tempNode = tempNode.next

    def deletion(self, location):
        if self.head is None:
            return "there is not any list here."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("the node deleted.")

    def deleteHole(self):
        if self.head is None:
            return "there is no element to delete."
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("the CDLL has been deleted.")


CDLL = CircularDLL()
CDLL.createCDLL(5)
CDLL.insertion(1, 1)
CDLL.insertion(4, 0)
CDLL.insertion(0, 0)
CDLL.insertion(2, 2)

print([node.value for node in CDLL])

CDLL.traversal()
CDLL.Reverse_Traversal()
print(CDLL.searchValue(4))
print(CDLL.searchValue(8))
CDLL.deletion(0)

# print([node.value for node in CDLL])
# CDLL.deletion(1)
# print([node.value for node in CDLL])
# CDLL.deletion(2)
# print([node.value for node in CDLL])
CDLL.deleteHole()
print([node.value for node in CDLL])
