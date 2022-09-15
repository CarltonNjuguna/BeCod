from multiprocessing.sharedctypes import Value
import string


list_of_numbers = [17, 38, 10, 25, 72]

def sortnumber(lst) :
    print(sorted(lst))

def addtwelve(lst) :
    lst.append(12)
    print(lst)

def reverselst(lst) :
    lst.reverse()
    print(lst)

def countlst(lst) :
    z = 0
    for i in lst :
        z +=1
    print(z)
    #lst.count

def delst(lst) :
    lst.remove(38)
    print(lst)
