

    # Step 3: Define the prepend method to add a new node at the beginning of the list
    def prepend(self, data):
        # Step 4: Create a new node with the given data
        new_node = Node(data)  # Instantiate a new node with the provided data
        
        # Step 5: Set the new node's next pointer to the current head of the list
        new_node.next = self.head  # Point the new node's next to the current head
        
        # Step 6: Update the head of the list to point to the new node
        self.head = new_node  # Make the new node the head of the list

    
    

  