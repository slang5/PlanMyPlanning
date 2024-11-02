import UserClass as PNJ

def day(valeur : int)->str:
    val = ((valeur) // 3)%5
    jours = ["Lundi", "Mardi","Mercredi", "Jeudi","Vendredi"]
    return jours[val]

def period(valeur : int)->str:
    val = (valeur) % 3
    jours = ["Matin", "Midi","Soir"]
    return jours[val]

def DayPeriod(i : int)->str:
    return day(i) + " " + period(i)

def SumUtilite(array:tuple)->float:
    perso:PNJ.Utilisateur
    retour: float
    retour = 0.0
    for perso in array:
        retour +=perso.Cumul
    return retour
    
def Variance(array:tuple)->float:
    mean = SumUtilite(array)
    perso:PNJ.Utilisateur
    taille = float(len(array))
    var: float
    var = 0.0
    for perso in array:
        var += ((float(mean)-float(perso.Cumul))**2)
    return var / taille

def Planning(Perso:tuple, Cbjours:int)->tuple:
    Personnages=[]
    for i in Perso:
        Personnages.append(PNJ.Utilisateur(i[0],i[1],i[2],i[3]))
    
    NbPersonnages = len(Personnages)
    NbPeriodes = 3 * Cbjours
    Memoire = [["P1","P2","P1_Loc", "P2_Loc", "UtiliteConsommee", "Periode"] for _ in range(NbPeriodes)]

    for iter in range(0, NbPeriodes):
        maxUtilite = -100
        Memoire[iter][5]=iter
        #print("{} : {}".format(iter,DayPeriod(iter)))
        Perso1 : PNJ.Utilisateur
        Perso2 : PNJ.Utilisateur
        for Personnage1 in range(0,NbPersonnages):
            for Personnage2 in range(Personnage1+1,NbPersonnages):
                Perso1 = Personnages[Personnage1]
                Perso2 = Personnages[Personnage2]
                Utilite = (Perso1.Utilite(iter) + Perso2.Utilite(iter)) /(1+Variance(Personnages)) 
                #print("{} & {} => {}".format(Perso1.Name, Perso2.Name,Utilite))
                if (maxUtilite) < (Utilite):
                    Memoire[iter][0]=Perso1.Name
                    Memoire[iter][2]=Personnage1

                    Memoire[iter][1]=Perso2.Name
                    Memoire[iter][3]=Personnage2
                    maxUtilite = Utilite

        #print("\tOn selectionne : {} et {}".format(Personnages[Memoire[iter][2]].Name,Personnages[Memoire[iter][3]].Name))
        Personnages[Memoire[iter][2]].Add_Utilite(iter)
        Personnages[Memoire[iter][3]].Add_Utilite(iter)
        Memoire[iter][4]= Personnages[Memoire[iter][2]].DeltaUtilite + Personnages[Memoire[iter][3]].DeltaUtilite

        #for i in range(0,NbPersonnages):
        #    print(Personnages[i].Debug())
    return Memoire
