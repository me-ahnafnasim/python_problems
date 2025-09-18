#delear a empty list
#1st function which add element
#2nd show the peek elements
#3rd pop a elements
#   ######

store=[]

def addEle():
    store.append(input("enter your elements: "))

def show():
    if store:
        print(store[-1])
    else:
        print("the list is empty")

def delet():
    if store:
       store.pop()
    else:
       print("empty")

while True: 
    try:
     choice=int (input("Enter your choice(1. add 2.show 3. pop):"))
    except valueError:
       print("Invalid input. Please chose a valid number")
       continue

    if choice==1:
       addEle()

    elif choice==2:
       show()

    elif choice==3:
       delet()
    
    elif choice==4:
       break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("Current Stack:", store)



