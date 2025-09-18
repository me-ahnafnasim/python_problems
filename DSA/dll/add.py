def Node(self, data):
    self.data = None


def addNode(self, data):
    # Create a new node
    newNode = Node(data)

    # If list is empty
    if self.head == None:
        # Both head and tail will point to newNode
        self.head = self.tail = newNode
        # head's previous will point to None
        self.head.previous = None
        # tail's next will point to None, as it is the last node of the list
        self.tail.next = None
    else:
        # newNode will be added after tail such that tail's next will point to newNode
        self.tail.next = newNode
        # newNode's previous will point to tail
        newNode.previous = self.tail
        # newNode will become new tail
        self.tail = newNode
        # As it is last node, tail's next will point to None
        self.tail.next = None



#short version

def addNode(self, data):
    newNode = Node(data)
    if self.head is None:
        self.head = self.tail = newNode
    else:
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = newNode
    self.tail.next = None