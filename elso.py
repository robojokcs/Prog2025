import random 

szamok = []


#100 elemu lista 1-100 között

#szám generálás
for i in range(100):
    
    rszam = random.randint(1,100)
    
    szamok.append(rszam)
'''
print(szamok)
'''

jatek_szam=0
nem_talaltDB=0


kitalalando_szam = szamok[random.randint(0,len(szamok))]

tipp=input("Kérek egy tippet 1-100 között: ")
while (not tipp.isdecimal()):
    print("Egész számot adj meg")
    tipp=input("Kérek egy tippet 1-100 között: ")
tipp=int(tipp)
    
    
    
    
if(tipp<kitalalando_szam):
    print("A tipp kisebb mint a kitalálandó szám")
    nem_talaltDB+=1 
if(tipp>kitalalando_szam):  
    print("A tipp nagyobb mint a kitalálandó szám")
    nem_talaltDB+=1
    
while (tipp!=kitalalando_szam):
    tipp=input("Kérek egy tippet 1-100 között: ")
    
    
    while (not tipp.isdecimal()):
        print("Egész számot adj meg")
        tipp=input("Kérek egy tippet 1-100 között: ")
    
    
    tipp=int(tipp)
    
    
    
    if(tipp<kitalalando_szam):
        print("A tipp kisebb mint a kitalálandó szám")
        
    if(tipp>kitalalando_szam):
        print("A tipp nagyobb mint a kitalálandó szám")
        

print("Gratulálok eltaláltad a számot")