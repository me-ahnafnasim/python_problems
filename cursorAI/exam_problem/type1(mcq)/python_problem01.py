"""
Write the Python function onlyodd(xlist), xlist being a list of 10 integers in the range (1,20), 
that returns a list containing only the odd numbers contained in the list xlist.
"""

def onlyodd(xlist):
    oddnum =[]
    for number in xlist:
        if number % 2 != 0:
            oddnum.append(number)
    return oddnum

print(onlyodd([7,10,5,12,18,9,3,1,11,15]))



