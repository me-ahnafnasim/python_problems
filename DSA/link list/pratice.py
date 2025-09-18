#so, write code for a single link list so that we can add elements to the end of the list
# 1st: we need to define two class for data and pointer and second one for initializing
# current node or head equal zero

#write the function which append node
#declear/write insteance of Node which store the data
#wite the condition that check the list is empty or not. If the list is empty write
# self.head = new_node and return
# curr_node = self.head
# and run a while loop for track the element and append the new node at the end of the list
#  like,,, curr_node=curr_node.next and curr_node=new_node
#  ###
        
        


    







class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return # Function exits here if the list was empty
                   # NOTE: Here, return under if condition

        last = self.head
        while last.next:
            last = last.next  # Move to the next node

        last.next = new_node  # line appends the new node to the end of the list.


    def prepend(self, data):
        new_node= Node(data) #create a variable or instance of a node class for storing the value
        
        #set the new node's next pointer to the current head of the list
        new_node.next = self.head

        #update the head of the list to point to the new node 
        self.head=new_node

    def preprend(self, data):
        new_node = Node(data) # create a instance of the node calass
        #set the new node's pointeer to the current head of the list
        new_node = self.head
        self.head=new_node



    def display(self):
        if not self.head:
            print("empty")
            return

        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")  # Correct position

# Example Usage
if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()

    # Append elements
    llist.append(2)
    llist.append(3)
    llist.append(4)
    print("output after apending element: ")
    llist.display()


    llist.prepend(1)
    llist.prepend(0)
    print("output after prepending the elemens: ")
    llist.display()



