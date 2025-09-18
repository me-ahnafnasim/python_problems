queue=[]

def enque(queue, item):
    queue.append(item)

def is_empty(queue):
    return len(queue)==0

def deque(queue):
    if not is_empty(queue):
       queue.pop(0)
    else:
        return "the queue is empty"

def size(queue):
    return len(queue)


enque(queue, 10)
enque(queue, 20)
enque(queue, 30)
enque(queue, 40)
enque(queue, 50)

print("the queue is:", queue)

print("size of the queue is:",size(queue))
print("is the queue empty?", is_empty(queue))
print("after out the first element",deque(queue))
print("the new queue is:", queue)