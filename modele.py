class ModeleTetris:
    def __init__(self, ligne = 14, colonne = 20):
        self.__ligne = ligne
        self.__colonne = colonne
        self.__base = 4
        self.__haut = self.__ligne + self.__base
        self.__larg = self.__colonne + self.__base
        self.__terrain = []
        ligne = [] #Ajout de la zone grise
        for i in range(self.__base):
            for k in range(self.__larg):
                ligne.append(-2)
            self.__terrain.append(ligne)
            ligne = [] 
        for i in range(self.__ligne): #Ajout de la zone de jeu
            for k in range(self.__larg):
                ligne.append(-1)
            self.__terrain.append(ligne)
            ligne = []
    
#    def printTerrain(self):
#        for i in range(self.__ligne + self.__base):
#            print(self.__terrain[i])

#jeu1 = ModeleTetris()
#jeu1.printTerrain()