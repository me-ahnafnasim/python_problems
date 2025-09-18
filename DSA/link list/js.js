    // Helper function to create a new node
    function createNode(value) {
        return { value: value, next: null };
    }


function append(head, value) {
    
    // Create a new node with the given value
    const newNode = createNode(value);

    // If the head is null (empty list), return the new node as the head
    if (head === null) {
        console.log("I'm new", head);
        return newNode;
    }

    // Traverse to the end of the linked list
    let current = head;
    while (current.next !== null) {
        current = current.next;
        //console.log("current", current);
    }

    // Append the new node at the end
    current.next = newNode;

    // Return the head of the updated list
    return head;
}


let list = null; // Initially empty list

list = append(list, 10); // Append 10
list = append(list, 20); // Append 20
list = append(list, 30); // Append 30

console.log(list);
