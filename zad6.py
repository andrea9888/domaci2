class Akcija:
    def __init__(self, zahtjev):
        self.quote=zahtjev[0]
        self.quantity=zahtjev[1]
        self.price=zahtjev[2]
        self.status=zahtjev[3]
    def broker(self):
        if self.status=='B':
            return {"Buy": float(self.price)*float(self.quantity), "Sell":0}
        else:
            return {"Buy": 0, "Sell":float(self.price)*float(self.quantity)}
    
zahtjev_str=input("Unesite zahtjev ")
broj_zahtjeva=zahtjev_str.count(",")+1
if broj_zahtjeva==1: 
    zahtjev=zahtjev_str.split(" ")
    print(Akcija(zahtjev).broker())
else:
    final_dict={"Buy":0, "Sell":0}
    zahtjevi=zahtjev_str.split(",")
    for i in zahtjevi:
        zahtjev1=i.split(" ")
        my_dict=Akcija(zahtjev1).broker()
        final_dict["Buy"]=final_dict["Buy"]+my_dict["Buy"]    
        final_dict["Sell"]=final_dict["Sell"]+my_dict["Sell"]    
    print(final_dict)
    