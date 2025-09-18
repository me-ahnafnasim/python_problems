def dllb(listx, low, high):
    dll = listx
    current = dll['head']['next']

    while current != 'tail':
        value = int(current)
        if value < low or value > high:
            # Remove current node
            prev_node = dll[current]['prev']
            next_node = dll[current]['next']
            dll[prev_node]['next'] = next_node
            dll[next_node]['prev'] = prev_node
            del dll[current]
            current = next_node
        else:
            current = dll[current]['next']
    
    return dll

listx = {
    'head': {'prev': None, 'next': '12'},
    '12':   {'prev': 'head', 'next': '20'},
    '20':   {'prev': '12', 'next': '15'},
    '15':   {'prev': '20', 'next': '2'},
    '2':    {'prev': '15', 'next': 'tail'},
    'tail': {'prev': '2', 'next': None}
}
low = 10
high = 19

call = dllb(listx,low, high)
print(call)