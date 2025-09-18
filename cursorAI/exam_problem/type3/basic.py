"""def insert(queue, element):
    queue.append(element)
    return queue

def extract(queue):
    x = queue.pop(0)
    return x
    # return queue.pop(0)

def is_empty(queue):
    return len(queue) == 0

def top(queue):
    if not is_empty(queue):
        return queue[0]

def length(queue):
    return len(queue)

#insert element to queue
queue1 = []
insert(queue1, 'Ali')
insert(queue1, 'Veli')
insert(queue1, 'Ayşe')
print(queue1)

#extract top element from queue
print(extract(queue1))
print(queue1)

#check if queue is empty
print(is_empty(queue1))

#check length of queue
print(length(queue1))

#check top element of queue without extracting it   
print(top(queue1))
print(queue1)

#clear queue
queue1.clear()
print(queue1)

#check if queue is empty again
print(is_empty(queue1)) """                        




"""
def insert(queue, element):
    queue.append(element)
    return queue

def len_check(queue):
    return(len(queue))

def delet_one(queue):
    if len_check(queue) == 0:
        print("your queue is empty")
        return None
    else:
        x = queue.pop(0)
        return x


queue1 =[]
insert(queue1, "a")
insert(queue1, "b")
insert(queue1, "c")
print(queue1)

print(len_check(queue1))

print(delet_one(queue1))

insert(queue1, "d")
insert(queue1, "e")
print(queue1)"""



"""dll3 = {
       'head':{'prev': None, 'next': 'tail'},
       'tail':{'prev': 'head', 'next': None},
       'A' :{'prev': 'head', 'next': 'tail'}
       }

print(dll3['head']['next'])
print(dll3['tail']['prev'])"""

"""
dll3['A'] = {'prev': 'head', 'next': 'tail'}
dll3['head']['next'] = 'A'
dll3['tail']['prev'] = 'A'

print('after inserting A', dll3)


dll3['B'] = {'prev':'A', 'next': 'tail'}
dll3['tail']['prev'] = 'B'
dll3['A']['next'] = 'B'

print('after inserting B', dll3)

print(dll3)"""


# Doubly linked list-based queue
def insert_queue(queue, value):
    new_node = {'value': value}
    prev_tail = queue['tail']['prev']
    
    # Link the new node
    new_node['prev'] = prev_tail
    new_node['next'] = 'tail'
    
    # Update the previous node and tail links
    queue[prev_tail]['next'] = str(value)
    queue['tail']['prev'] = str(value)
    
    # Add new node to queue dictionary
    queue[str(value)] = new_node

def extract_queue(queue):
    first = queue['head']['next']
    if first == 'tail':
        return None  # Queue is empty
    
    next_node = queue[first]['next']
    
    # Update links
    queue['head']['next'] = next_node
    queue[next_node]['prev'] = 'head'
    
    # Remove and return the value
    value = queue[first]['value']
    del queue[first]
    return value

def traverse(queue):
    current = queue['head']['next']
    result = []
    while current != 'tail':
        result.append(queue[current]['value'])
        current = queue[current]['next']
    print("Queue contents:", result)

# Initialize the queue
dll_queue2 = {
    'head': {'prev': None, 'next': 'tail'},
    'tail': {'prev': 'head', 'next': None}
}

# Insert values [100, 200, 300, 400]
xlist = [100, 200, 300, 400]
for x in xlist:
    insert_queue(dll_queue2, x)

# Traverse and show the queue after initial insertions
traverse(dll_queue2)

# Extract two values
print("Extracted:", extract_queue(dll_queue2))
print("Extracted:", extract_queue(dll_queue2))

# Insert the value 500
insert_queue(dll_queue2, 500)

# Traverse and show the queue after operations
traverse(dll_queue2)

  