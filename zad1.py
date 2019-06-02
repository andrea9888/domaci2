lista=list(range(1,11))
lista1=[]
lista2=[]
k=0
import random
while k!=5:
    lista2.append(random.choice(lista))
    k=k+1
for i in lista:
    if lista2.count(i)==0:
        lista1.append(i)
print (list(zip(lista1, lista2)))