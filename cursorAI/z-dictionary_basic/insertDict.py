#insert intwo dictionary
myDict = {
    "name": "nasim", 
    "age":24, 
    "institute":"unime"
    }
#Add single key-value pair in the dict
myDict["country"] = "Bangladesh"

#Add multiple key-value pairs from a dict
myDict.update({"DOV":"15/12/2000", 'id':5162})


#Insert from a list of key-value pairs
myDict.update([("DOV","15/12/2000"), ('id',5162), ("location", "Messina")])
print(myDict)


dict1 ={"a":2}
dict1 |={"b":2, "a":1}

print(dict1)