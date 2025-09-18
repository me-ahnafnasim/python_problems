def insert_in_pos(data):
  new_node ={"data": data, "next": None}
  

  linked_list = {
    "head": {"data": 10, "next": {"data": 20, "next": {"data": 30, "next": {"data": 40, "next": {"data": 50, "next": {"data": 60, "next": {"data": 70, "next": None}}}}}}},
    "tail": {"data": 70, "next": None}
}
  
  new_node["next"] = linked_list["head"]
  print(new_node)
  #now modify the whole link_list
  linked_list["head"] = new_node

  print("modifed link_list is: ", linked_list)


print(insert_in_pos(5))





def insert_speci_pos(link_list, data, position):
  new_node = {"data": data, "next": None}

  if position ==0:
    new_node["next"] = link_list["head"]
    link_list["next"] = new_node
    if link_list["tail"] is None:
      link_list["tail"] = new_node
      return
    
    current = link_list["head"]
    index = 0

    while current is not None and index<position-1:
      current = current["next"]
      index = index+1
    
    if current is None:
      print("invalid position")
    else:
      new_node["next"] = current["next"]
      current["next"] = new_node
      
      if new_node["next"] is None:
        link_list["tail"] = new_node

  

  