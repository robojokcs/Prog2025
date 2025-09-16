import random 

szamok = []


#100 elemu lista 1-999 között

#szám generálás
for i in range(100):
    
    rszam = random.randint(1,999)
    
    szamok.append(rszam)
  
print(szamok)


jatek_szam=0
nem_talaltDB=0


kitalalando_szam = random.randint(szamok)   