stack = []

def push(stack, item):
    stack.append(item)

def is_empty(stack):
    return len(stack)==0

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        return "Stack underflow"
    
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        return "stack is empty"

def size(stack):
    return len(stack)



push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)

print("top element", peek(stack))
print("size of the queu", size(stack))

print("delet the top element", pop(stack))

print("is the stack is empty?", is_empty(stack))

print("poped", pop(stack))







# Stack is represented using a list
stack = []

# Push an element onto the stack
def push(stack, item):
    stack.append(item)

# Check if the stack is empty
def is_empty(stack):
    return len(stack) == 0


# Pop an element from the stack
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        return "Stack Underflow"

# Peek at the top element of the stack
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        return "Stack is empty"



# Get the size of the stack
def size(stack):
    return len(stack)



push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Top element:", peek(stack))   # Output: 30
print("Stack size:", size(stack))    # Output: 3

print("Popped:", pop(stack))         # Output: 30
print("Popped:", pop(stack))         # Output: 20

print("Is stack empty?", is_empty(stack))  # Output: False

print("Popped:", pop(stack))         # Output: 10
print("Popped:", pop(stack))         # Output: Stack Underflow

