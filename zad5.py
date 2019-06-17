htmlString1 ='''
<article id='parakeet'>

    <h1 class= "parrot">My parakeet</h1>

    <p>I have a parakeet named Pietje. He can fly and play well. In the daytime he is allowed out of his cage. He eats and drinks in his cage. He has many toys:</p>

    <h2>Pietje's toys</h2>

        <p>

            A mirror, a bell, another bell, another mirror and much much more

        </p>

    <p>This concludes the article about Pietje the parakeet.</p>
</article>'''
def getTagContent(htmlString,tag):
    konacna_lista_sadrzaja=[]
    def ima_li_taga(htmlString,tag):
        tag_1='<'+tag
        brojac=0 #broji da li se svi brojevi u nazivu taga poklapaju
        for (count,elem) in enumerate(htmlString):
            if elem==tag_1[0]:
                if htmlString[count+1]==tag_1[1]:
                    brojac=1 
                    for count2 in range(1,len(tag)):
                        if htmlString[count+1+count2]==tag[count2]:
                            brojac=brojac+1
                    if brojac==len(tag):
                        return True
                    
    while 1:
        if (ima_li_taga(htmlString,tag))==True:
            tag_1='<'+tag
            tag_2=tag+'>'
            lista1=htmlString.partition(tag_1)
            lista2=lista1[2].partition(tag_2)
            konacna_lista_sadrzaja.append(lista2[0])
            htmlString=lista2[2]
        else:
            break

    konacna_lista_sadrzaja_bez_oznaka=[]
    for elem in konacna_lista_sadrzaja:
        pocetak=elem.find(">")
        kraj=elem.find('</')
        konacna_lista_sadrzaja_bez_oznaka.append(elem[pocetak+1:kraj].replace('\n', '').lstrip().rstrip())
    print(konacna_lista_sadrzaja_bez_oznaka) 

getTagContent(htmlString1,'h1')  
getTagContent(htmlString1,'h2')        
getTagContent(htmlString1,'p')

