class Node():
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        currentNode = Node(data)
        currentNode.next = self.head
        self.head = currentNode

    def append(self, data):
        currentNode = Node (data)
        currentNode.next = None

        p = self.head
        if (p == None ):
            self.head = currentNode
        else:
            while(p.next != None):
                p = p.next

            p.next = currentNode

    def printList(self):
        p = self.head
        while(p != None):
            print(p.data, end=" ")
            p = p.next

curr = LinkedList()
curr.append(1)
curr.append(2)
curr.append(3)
curr.append(4)
curr.append(5)
curr.append(6)
curr.push(7)
curr.printList()