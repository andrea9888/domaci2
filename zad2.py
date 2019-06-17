def filter_1(function, iterable):
    tip=type(iterable)

    if tip is list or tip is str or tip is tuple:
        iterable1=[]
        for i in iterable:
            k=function(i)
            if k==True:
                iterable1.append(i)
        if tip is tuple:
            return tuple(iterable1)
        elif tip is str:
            return ''.join(str(i) for i in iterable1)
        else:
            return iterable1


    elif tip is set:
        iterable1=set()
        for i in iterable:
            k=function(i)
            if k==True:
                iterable1.add(i)
        return iterable1
def map_1(function,iterable):
    tip=type(iterable)

    if tip is list or tip is str or tip is tuple:
        iterable1=[]
        for i in iterable:
            k=function(i)
            iterable1.append(k)
            
        if tip is tuple:
            return tuple(iterable1)
        elif tip is str:
            return ''.join(str(i) for i in iterable1)
        else:
            return iterable1


    elif tip is set:
        iterable1=set()
        for i in iterable:
            k=function(i)
            iterable1.add(k)
        return iterable1
def reduce_1(function,iterable):
    if type(iterable) is str:
        iterable1=[]
        for i in iterable:
            iterable1.append(int(i))
            
    else:
        iterable1=list(iterable)
    rezultat=function(iterable1[0], iterable1[1])
    iterable1.pop(0)
    iterable1.pop(0)
    for i in iterable1:
        rezultat=function(rezultat,i)
    return rezultat


'''
string='aaabbbccc haaa'
lista=[1, 2]
set1=set(lista)
torka=(1,2)
check=lambda i: i=='a'
check1=lambda i: i==1
check2=lambda i: i+'1'
check3=lambda i: 9*i
print(filter_1(check,string))
print(filter_1(check1,lista))
print(filter_1(check1,set1))
print(filter_1(check1,torka))

print(map_1(check2,string))
print(map_1(check3,lista))
print(map_1(check3,torka))
print(map_1(check3,set1))

a = [1, 2, 3, 4]
set1=set(a)
string='1234'
torka=(1,2,3,4)
suma = reduce_1(lambda x, y: x + y, string)
print (suma)
'''