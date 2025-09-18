queue = []

def add():
    element = input("Enter your element: ")
    queue.append(element)
    print(queue, "is added successfully.")

def delete():
    if queue:
        queue.pop(0)  # Deleting the first element
        print("Updated queue:", queue)
    else:
        print("The queue is empty.")

while True:
    print("1. Add an element")
    print("2. Delete an element")
    print("3. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Enter a valid choice (1, 2, or 3).")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
