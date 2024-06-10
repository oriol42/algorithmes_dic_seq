val=int(input("veuillez entrez la valeur recherche\n"))
tab=[2,3,1,4,5,9,7,45,23]
longueur = len(tab)
i = 0
test = 0
while i < longueur:
    if val == tab[i]:
        print("la valeur se trouve dans le tableau a la position p =",i )
        test = 1
    i= i+1 
if i >= longueur & test == 0 :
    print("la valeur recherche n'est pas dans le tableau")