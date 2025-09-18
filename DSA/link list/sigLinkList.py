class Node:
    def __init__(self, data):
        self.data = data       # Stores the value of the node
        self.next = None       # Pointer to the next node (initially set to None)


# Create nodes
node1 = Node(10)  # Node with data = 10
node2 = Node(20)  # Node with data = 20
node3 = Node(30)  # Node with data = 30
node4 = Node(40)  # Node with data = 40

#--------------------------------------------the output of the above code----------------------------------
Node1: [data=10, next=None]
Node2: [data=20, next=None]
Node3: [data=30, next=None]
#--------------------------------------------------------------------------------------------------------------


# Link the nodes
node1.next = node2  # Node1 points to Node2
node2.next = node3  # Node2 points to Node3
node3.next = node4  # Node3 points to Node4

#--------------------------------------------after linking the node the output------------------------------------
#Node1: [data=10, next=Node2] --> Node2: [data=20, next=Node3] --> Node3: [data=30, next=None]
#-----------------------------------------------------------------------------------------------------------------




# Define the head of the linked list
head = node1
# Traverse and print the linked list
currentNode = head
while currentNode:
    print(currentNode.data, end=" -> ")  # Print the data of the current node
    currentNode = currentNode.next        # Move to the next node
print("null")  # Print "null" at the end to indicate the end of the list