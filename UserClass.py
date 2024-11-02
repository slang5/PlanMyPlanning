import math as m
class Utilisateur():
    
    def __init__(self, Name : str,Coef1 : int, Coef2  : int, Coef3 : int) -> None:
        self.Name = Name
        self.Coef = [(Coef1) ,(Coef2) ,(Coef3)]
        self.TotalPerme = [0 for _ in range(3)]
        self.Cumul = 0.0
        self.DeltaUtilite = 0.0
        self.Permanances = 0.0
        pass

    def Close(self) -> None:
        for i in range(0,3):
            if self.Coef[i] < 1:
                self.Coef[i] = 1
            elif self.Coef[i]  > 100:
                self.Coef[i] =  100
            else:
                self.Coef[i] = self.Coef[i] 

    def Utilite(self, Periode : int) -> float:
        retour = 1
        mod = Periode % 3
        x = self.TotalPerme[mod] + 1
        a = self.Coef[mod]
        T = Periode + 1
        partie1 = m.exp(x**2/T - (x/101)**(1/(101-a))) - a ** (-1/T) + ((T+x*a)/T)**(-1/a)
        partie1 = m.log(partie1) + 1/(1/(4+a)) + m.log(1+a/101)
        retour = m.log(partie1)+ m.exp(1-(x/T)**(4/3)) + (m.log(m.cos((x-T)*0.5/(m.cos(T*x)))+10)**2)*T/(x+75+20)
        
        self.DeltaUtilite = retour
        return self.DeltaUtilite

    def Add_Utilite(self, Periode : int) -> None:
        self.Cumul += round(self.Utilite(Periode))
        self.TotalPerme[Periode%3] +=1
        self.PermanencesFaite()
        pass

    def Debug(self) -> str:
        text = "{}: Coef1={} Coef2={} Coef3={} Matin={} Midi={} Soir={} | Utilite={} | Total={}".format(self.Name, self.Coef[0], self.Coef[1], self.Coef[2],self.TotalPerme[0],self.TotalPerme[1],self.TotalPerme[2], self.Cumul,self.Permanances)
        return text
    
    def PermanencesFaite(self) -> None:
        tmp = 0
        for i in range(0,3):
            tmp += self.TotalPerme[i]
        self.Permanances = tmp
        pass
