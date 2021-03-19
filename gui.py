# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:18:54 2020

@author: ulysse
"""

"""
fonctionne avec une matrice :
mat = [
[[i,i,i],[i,'X',i],[i,i,i]],
[[i,i,i],[i,'X',i],[i,i,i]],
[[i,i,i],[i,'X',i],[i,i,i]],
[[i,i,i],[i,'X',i],[i,i,i]],
[[i,i,i],[i,'X',i],[i,i,i]],
[[i,i,i],[i,'X',i],[i,i,i]],
]
Chaque sous matrice représente une face

Les faces sont ordonnées dans l'ordre suivant :
devant,droite, arrière, gauche, dessus, dessous

Les couleurs i sont représentées par les lettres :
'R','W','O','Y','G','B'
la case du centre vide est marquée par "X"

Initialisation :
obj=GUI(mat)

Mise a jour :
obj.afficher(mat)

Quitter :
obj.quit()
    
"""



import tkinter as tk
import time
import random
from RediClass import RotateArray
import copy
from PIL import ImageGrab,Image


class GUI():
    def __init__(self,cube):
        #dimentionnage cube
        self.tailleCote=30
        self.tailleFace=self.tailleCote*3
        
        #fenetre
        self.root=tk.Tk()
        self.root.title("Redi Cube")
        self.root.geometry("300x400")
        
        #zone de dessin
        self.canvas=tk.Canvas(self.root,width=300,height=400,bg="grey")
        
        #trad : struc de donnée -> Tkinter
        self.dico_coul={"R":"red",
                        'W':"white",
                        'O':"orange",
                        'Y':"yellow",
                        'G':"green",
                        'B':"blue",
                        'X':"grey"}
        
        self.afficher(cube)
        
        

        
    def afficher(self,inputCube):
        cube=copy.deepcopy(inputCube)
        #rotation pour que les faces soient dans le bon sens :
        cube[0]=RotateArray(cube[0],3)
        cube[1]=RotateArray(cube[1],3)
        cube[2]=RotateArray(cube[2],1)
        cube[3]=RotateArray(cube[3],3)
        cube[4]=RotateArray(cube[4],3)
        cube[5]=RotateArray(cube[5],3)
        #cube=[RotateArray(face,3) for face in cube]
        
        #mise en 2d du cube
        margeX=15
        margeY=20
        self.posFaces=[              (self.tailleFace+margeX,0+margeY,cube[4]),
         (0+margeX,self.tailleFace+margeY,cube[3]),(self.tailleFace+margeX,self.tailleFace+margeY,cube[0]),(2*self.tailleFace+margeX,self.tailleFace+margeY,cube[1]),
                        (self.tailleFace+margeX,2*self.tailleFace+margeY,cube[5]),
                        (self.tailleFace+margeX,3*self.tailleFace+margeY,cube[2])]
        #affichage
        for posX,posY,couleurs in self.posFaces:
            for y in range(3):
                for x in range(3):
                    #création carrés de la face
                    self.canvas.create_rectangle(posX+x*self.tailleCote,posY+y*self.tailleCote,posX+(x+1)*self.tailleCote,posY+(y+1)*self.tailleCote, fill=self.dico_coul[couleurs[y][x]])
        
        self.canvas.pack()
        self.root.update()
    
    def quit(self):
        self.root.destroy()
        
    def save_as_bmp(self,fileName):
        time.sleep(0.3)
        x = self.canvas.winfo_rootx()*1.25 #compenser zoom écran
        y = self.canvas.winfo_rooty()*1.25
        w = self.canvas.winfo_width()*1.25
        h = self.canvas.winfo_height()*1.25
        image=ImageGrab.grab((x+2, y+2, x+w-2, y+h-2))
        image.save(fileName+".bmp")

#test :
        
def test_aff_simple():
    matrice = []
    for i in ('R','W','O','Y','G','B'):
        matrice.append([[i,i,i],[i,'X',i],[i,i,i]])
            
    af=GUI(matrice)
    
    matrice=[]
    for i in ('B','W','O','Y','G','R'):
        matrice.append([[i,i,i],[i,'X',i],[i,i,i]]) 
    
    time.sleep(2)
    af.afficher(matrice)
    time.sleep(3)
    af.quit()
    
    
    

def randMatrice(): #couleurs aléatoire pour tester la bonne execution
    couleurs=('R','W','O','Y','G','B')
    mat=[]
    for face in range(6):
        f=[[None,None,None],[None,None,None],[None,None,None]]
        for i in range(3):
            for j in range(3):
                f[i][j]=random.choice(couleurs)
        f[1][1]="X"
        mat.append(f)
    return mat

def test_Rand():
    af=GUI(randMatrice())
    for i in range(10):
        time.sleep(1)
        af.afficher(randMatrice())
    af.quit()

def test_save():
    af=GUI(randMatrice())
    af.save_as_bmp("testsave")
    af.quit()
        
def afficherListePositions(positions,temps):
    #initialisation
    window=GUI(positions[0])
    for pos in positions[1:]:
        time.sleep(temps)
        window.afficher(pos)
    time.sleep(temps)
    window.quit()
    
def sauvegarderListePositions(positions):
    window=GUI(positions[0])
    window.save_as_bmp("cube"+str("0"))
    for pos in range(1,len(positions)):
        window.afficher(positions[pos])
        window.save_as_bmp("cube"+str(pos))
    window.quit()

def afficherSimple(mat,temps=3,touche=False):
    window=GUI(mat)
    if touche:
        input("Appuyer sur ENTRER pour continuer")
    else :
        time.sleep(temps)
    window.quit()
    
if __name__=="__main__":
    test_save()

