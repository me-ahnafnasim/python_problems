from collections import deque
#in deque append and pop also working
stack = deque()

#pusing elements in the queue
stack.append(1)  # Push
stack.append(2)
stack.append(3)
stack.append(4)


#removing elements from the queue
print(stack)
print(stack.pop())  # Pop -> 2
print(stack.pop())  # Pop -> 1
print(stack)




try:
    if stack:
        print(stack.pop()) #delet 40
    else:
      print("the queu is empty")
except valueError:
    print("its invalid")

#show the top element by usint try and except
try:
    if stack:
       top=stack[-1]
       print(top)
except valueError:
    print("the queue is empty")

print(stack)
