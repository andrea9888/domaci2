igrice=[]
žanrovi=[]
f = open("C:/Users/USER/Desktop/igrice.txt")
for line in f:
    igrice.append(line)
f.close()
def pravilan_fajl(i):
    i_str=''.join(str(k) for k in i)
    posebni_podaci=i_str.split(";")
    if 2<len(posebni_podaci[0])<40:
        if len((posebni_podaci[1].split("."))[1])==2:
            if 1950<int(posebni_podaci[2])<2019:
                if 2<len(posebni_podaci[3])<40:
                    if posebni_podaci[4].count(" ")<3:
                        return True
bez_novog_reda=[]
igrice_filter=list(filter(pravilan_fajl,igrice))
for i in igrice_filter:
    if i==igrice_filter[-1]:
        bez_novog_reda.append(i)
    else:
        bez_novog_reda.append(i[:-2])
print("Igrice nakon micanja nepravilno unešenih u originalnom fajlu: \n", bez_novog_reda)
f = open("C:/Users/USER/Desktop/igrice.txt","w")
for linija in igrice_filter:
    f.write(linija)
f.close()
for i in igrice_filter:
    i_str=''.join(str(k) for k in i)
    posebni_podaci=i_str.split(";")
    žanr=posebni_podaci[4][:-2].strip()
    if žanr.count(" ")!=0:
        više_žanrova=žanr.split(" ") 
        for k in više_žanrova:
            žanrovi.append(k.lower())
    else:
        žanrovi.append(žanr.lower())

update_igrice=[]
taster=input("Da li želite da unesete nove igrice? Pritisnite 1 ako da, 0 ako ne. \n")
while taster=='1':
    nova_igrica=input("Unesite igricu, i to naziv, ocjenu, godinu, izdavaca i zanr(ukoliko unosite vise zanrova razdvojeni su space-om), razdvajajuci kategorije sa ';'\n ")
    while pravilan_fajl(nova_igrica)!=True:
        print("Unos nije validan!\n")
        taster=input("Da li želite opet da unesete igricu? Pritisnite 1 ako da, 0 ako ne. \n")
        if taster=='1':
            nova_igrica=input("Unesite igricu: ")
        elif taster=='0':
            break
       
    update_igrice.append(nova_igrica)
    taster=input("Da li želite da unesete još igrica? Pritisnite 1 ako da, 0 ako ne. \n")
    if taster=='0':
        break

f = open("C:/Users/USER/Desktop/igrice.txt","a")
for linija in update_igrice:
    f.write("\n")
    f.write(linija)
f.close()
igrice_prije_finalnog_odabira=[]
f = open("C:/Users/USER/Desktop/igrice.txt")
for line in f:
    igrice_prije_finalnog_odabira.append(line)
f.close()
lista_dict=[]
lista_torki=[]
broj=0

for i in igrice_prije_finalnog_odabira:
    i_str=(''.join(str(k) for k in i))
    igrica_prije_finalnog_odabira=i_str.split(";")
    d={"naziv":str(igrica_prije_finalnog_odabira[0]),"ocjena":float(igrica_prije_finalnog_odabira[1]),"godina":int(igrica_prije_finalnog_odabira[2]),"izdavac":str(igrica_prije_finalnog_odabira[3]),"zanrovi":str((igrica_prije_finalnog_odabira[4].replace(" \n"," ")).strip()).split(" ")}
    torka=tuple(d.values())
    lista_dict.append(d)
    lista_torki.append(torka)
print(lista_dict)
lista_zanrova= [zanrovi for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki]
lista_zanrova_final=[]
for i in lista_zanrova:
        for k in i:
            lista_zanrova_final.append(k)
    
print("Zanrovi su: ",set(lista_zanrova_final))
print("Listu igrica možete filtrirati! ")
while 1:
    taster1=input("Unesite 1 za filter po imenu, 2 za filter po ocjeni, 3 po godini, 4 po izdavaču, 5 po zanru!\n Ako ne zelite da filtrirate listu, unesite 0.\n")
    if taster1=='0':
        break
    if taster1=='1':
        filter1=input("Unesite termin kojim počinje željena igrica: ")
        if 2<len(filter1)<40:
            lista_torki1=[(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if naziv.startswith(filter1)]
            print(lista_torki1) 
        else:
            print("Unos je nevalidan!\n")      
        dalja_filtracija=input("Ako ne želite dalje da filtrirate ukucajte 0! Ukoliko nastavljate, kliknite bilo koji drugi taster \n ")
        if dalja_filtracija=='0': 
            print(lista_torki1)
            break
    if taster1=='2':
        filter2=input("Ocjene su od 1 do 10, zaokruzene na 2 decimale. Unesite minimalnu ocjenu zeljene igrice: \n ")
        if len((filter2.split("."))[1])==2:
            lista_torki1=[(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if ocjena>float(filter2)]
            print(lista_torki1)
        else:
            print("Unos je nevalidan!\n")     
        dalja_filtracija=input("Ako ne želite dalje da filtrirate ukucajte 0! Ukoliko nastavljate, kliknite bilo koji drugi taster \n ")
        if dalja_filtracija=='0': 
            print(lista_torki1)
            break
    if taster1=='3':
        filter3=input("Unesite godinu: \n")
        prije_poslije=input("Da li želite igricu prije ili poslije unijete godine? \n")
        if prije_poslije=="prije":
            if 1950<int(filter3)<2019:
                lista_torki1=[(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if godina<int(filter3)]
                print(lista_torki1)
            else:
                print("Unos je nevalidan!\n")
        elif prije_poslije=="poslije":
            if 1950<int(filter3)<2019:
                lista_torki1=[(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if int(godina)>int(filter3)]
                print(lista_torki1)
            else:
                print("Unos je nevalidan!\n") 
        dalja_filtracija=input("Ako ne želite dalje da filtrirate ukucajte 0! Ukoliko nastavljate, kliknite bilo koji drugi taster \n ")
        if dalja_filtracija=='0': 
            print(lista_torki1)
            break
    
    if taster1=='4':
        filter4=input("Unesite termin kojim počinje željeni izdavac:\n")
        if 2<len(filter4)<40:
            lista_torki1=[(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if izdavac.startswith(filter4)]
            print(lista_torki1)
        else:
            print("Unos je nevalidan!\n") 
        dalja_filtracija=input("Ako ne želite dalje da filtrirate ukucajte 0! Ukoliko nastavljate, kliknite bilo koji drugi taster \n ")
        if dalja_filtracija=='0': 
            print(lista_torki1)
            break
    if taster1=='5':
        lista_torki1=[]
        print("Možete birati izmedju: ", set(lista_zanrova_final), "\n")
        filter5=input( "Unesite željene žanrove: \n")
        if filter5.count(" ")<3:
            lista_zeljenih_zanrova= filter5.split(" ")
            for k in range(0,len(lista_zeljenih_zanrova)):
                lista_torki1.append([(naziv,ocjena,godina,izdavac,zanrovi) for (naziv,ocjena,godina,izdavac,zanrovi) in lista_torki if zanrovi.count(lista_zeljenih_zanrova[k])==1])
            print(lista_torki1)
        else:
            print("Unos je nevalidan!\n") 
        dalja_filtracija=input("Ako ne želite dalje da filtrirate ukucajte 0! Ukoliko nastavljate, kliknite bilo koji drugi taster \n ")
        if dalja_filtracija=='0': 
            print(lista_torki1)
            break

'''   
ukoliko bismo jednu listu filtrirali po vise kategorija istovremeno, 
umjesto lista_torki1 svuda bi islo lista_torki, kako bi se napravile dodatne izmjene na vec filtriranoj listi

'''