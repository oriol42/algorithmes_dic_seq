val=int(input("veuillez entrez la valeur recherche\n"))
tab=[0,3,5,7,9,11,13,15,17]
fin = len(tab) -1
debut = 0
test = 0

while debut <= fin:
    milieu = (fin + debut)// 2
    if val == tab[milieu]:
        print("la valeur se trouve dans le tableau a la position p =",milieu )
        debut = fin +1 
        test = 1
    else:
        if val > tab[milieu]:
            debut = milieu + 1
        else:
            fin = milieu -1    
if test == 0:
    print("la valeur n'est pas dans le tableau")