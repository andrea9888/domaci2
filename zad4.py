N=int(input("Unesi broj vrata:\n"))
vrata=['0']*N
k=1
def promjena_stanja(i):
    global N,k
    for ucenik in list(range(1,N+1)):
        if k%ucenik==0:
            if i=='0': 
                i='1'
            else: 
                i='0'
    k=k+1
    return i
   
print(list(map(promjena_stanja,vrata)).count('1'))