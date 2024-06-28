import random

class ModeleTetris:
    def __init__(self, ligne = 14, colonne = 20):
        self.__ligne = ligne
        self.__colonne = colonne
        self.__base = 4
        self.__haut = self.__ligne + self.__base
        self.__larg = self.__colonne + self.__base
        self.__terrain = []
        ligne = []
        for i in range(self.__base):
            for k in range(self.__larg):
                ligne.append(-2)
            self.__terrain.append(ligne)
            ligne = [] 
        for i in range(self.__ligne):
            for k in range(self.__larg):
                ligne.append(-1)
            self.__terrain.append(ligne)
            ligne = []
        self.__forme = Forme()

    @property
    def get_largeur(self):
        return self.__larg
    
    @property
    def get_hauteur(self):
        return self.__haut
    
    @property
    def get_valeur(self, i, j):
        return self.__terrain[i][j]
    
    @property
    def est_occupe(self, i, j) -> bool:
        return self.__terrain[i][j] != -1 or self.__terrain[i][j] != -2
    
    def fini(self):
        if self.__terrain[self.__base] != [-2 for i in range(self.__larg)]:
            return True
    
    def ajoute_forme(self):
        pass #A FAIRE

    





class Forme:
    def __init__(self, modele = ModeleTetris(), couleur = 0):
        self.__modele = modele
        self.__couleur = couleur
        self.__forme = [(-1,1),(-1,0),(0,0),(1,0)]
        self.__x0 = int(random.randint(2, self.__modele.get_largeur() -2))
        self.__y0 = 0
    
    @property
    def get_couleur(self):
        return self.__couleur
    
    @property
    def get_coords(self):
        return (self.__x0, self.__y0)
    
    def collision(self, dx, dy):
        for i in range(4):
            x = self.__x0 + self.__forme[i][0] + dx
            y = self.__y0 + self.__forme[i][1] + dy
            if x < 0 or x >= self.__modele.get_largeur() or y >= self.__modele.get_hauteur():
                return True
            if y >= 0 and self.__modele.est_occupe(y,x):
                return True
        return False
    
    def tombe(self):
        if not self.collision(0,1):
            self.__y0 += 1
            return False
        else:
            return True
    



        

    
#    def printTerrain(self):
#        for i in range(self.__ligne + self.__base):
#            print(self.__terrain[i])

#jeu1 = ModeleTetris()
#jeu1.printTerrain()