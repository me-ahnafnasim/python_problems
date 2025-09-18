
dll = {
    'head': {'prev': None, 'next': 12},
    12: {'prev': 'head', 'next': 20},
    20: {'prev': 12, 'next': 15},
    15: {'prev': 20, 'next': 2},
    2: {'prev': 15, 'next': 'tail'},
    'tail': {'prev': 2, 'next': None}
}

def sum_dll(dll):
    current = dll["head"]["next"]  
    total =0
    while current != "tail":
        if current % 2 == 0: #note just (if current % 2 != 0:) will give you odd node sum
            total += current  
        current = dll[current]['next']  
    return total  

print(sum_dll(dll))  # Output will be 34 (12 + 20 + 2)=34