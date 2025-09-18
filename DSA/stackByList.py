
store = []

#for push we need to use append method
def addEle():
    store.append(input("Enter element: "))

# Show the top element of the stack
def topEle():
    if store:  # Check if stack is not empty
        print("Top element:", store[-1])
    else:
        print("Stack is empty")

def delet():
    if store:  # Check if stack is not empty before popping
        store.pop()
    else:
        print("Stack is empty, cannot delete")

while True:
    try:
        choice = int(input("Input your choice (1: Push, 2: Top, 3: Pop, 4: Exit): "))  
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Ask for input again
    
    if choice == 1:
        addEle()
    
    elif choice == 2:
        topEle()
    
    elif choice==3
        delet()
    
    elif choice == 4:
        break  # Exit loop

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("Current Stack:", store)  # Show stack after each operation
