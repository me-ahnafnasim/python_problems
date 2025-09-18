""""
def ini_link_list(link_list, data):
    return {"head": None, "tail": None}

def add_node_back(link_list, data):
    new_node ={"data": data, "next": None}
    if link_list["head"] is None: #if the list is empty
        link_list["head"] = new_node
        link_list["tail"] = new_node
    else:
       #if the list is not empty
       link_list["tail"]["next"] = new_node
       link_list["tail"] = new_node




def search_and_delete(link_list, value):
    current = link_list["head"]
    previous = None
#2->3->4
#Traverse the link list to find the node for deleting
    while current is not None:
        if current["data"] == value: #node found
#previous is None means the targated node is found in the front of the link list
            if previous is None: #previous is None means it indicates the first node
                #deleting the first node
                link_list["head"] = current["next"] 
                  #what if, if the link is empty?
                if link_list["head"] is None:
                    link_list["tail"] = None
                else:
                    #deleting a middle or a last element
                    previous["next"] = current["next"] #this line is for bypass the targeted line
                    #deleting the last node
                    if current["next"] is None: #  checks whether the current node is the last node in the linked list. 
                        link_list["tail"] = previous
                return True
        previous = current
        current = current["next"] 



def print_link_list(link_list):
    current = link_list["head"]

    while current is not None:
        print(current["data"], end="->")
        current = current["next"]
    print("None")



"""



"""
score = 32

if score >=80:
    print("you got A+")

elif score >=70:
    print("you got A")

elif score >=60:
    print("you got c")

elif score >=33:
    print("you got F")

else:
    print("you are fail")"""





"""def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False"""

    
"""def is_even(num):
    if num%2 == 0:
        return True
   
    return False

print("is the given number even?",is_even(31))"""
def insert(link_data, 5):
    new_node ={"data": 5, "next": None }
 
new_node["next"] = link_list["head"]



new_node ={"data": 5, "next":{"data": 10, "next": {"data": 20, "next": {"data": 30, "next": {"data": 40, "next": {"data": 50, "next": {"data": 60, "next": {"data": 70, "next": None}}}}}}},
    "tail": {"data": 70, "next": None} }


linked_list = {
    "head": {"data": 10, "next": {"data": 20, "next": {"data": 30, "next": {"data": 40, "next": {"data": 50, "next": {"data": 60, "next": {"data": 70, "next": None}}}}}}},
    "tail": {"data": 70, "next": None}
}

current_head = linked_list["head"]  # Gets the entire head node
head_data = current_head["data"]    # Gets the value (10)
next_node = current_head["next"]

print("current head: ",current_head)
print("head data: ", head_data)
print("next node: ", next_node)
