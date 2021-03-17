# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:13:51 2021

@author: ulyss
"""

# format {"position actuelle":(profondeur,positionPreced)}

import RediClass
from gui import afficherListePositions,afficherSimple
from ast import literal_eval
from collections import namedtuple,Counter
import time
import copy
import json
import random

#Etat=namedtuple("Etat",["prof","posPrec"])
solvedCube=[[[i, i, i], [i, 'X', i], [i, i, i]] for i in ('W', 'O', 'Y', 'R', 'G', 'B')]
  
def recuCreate(redi,profondeur,profMax):
    global dicPos
    if profondeur<=profMax:
        #moving only the top 4 corner, white face allready solved
        for side in (1,2):
            for y in ("up","down"):
                for z in (-1,1):
                    newRedi=RediClass.Redi(copy.deepcopy(redi.cube))
                    newRedi.rotate(side,y,z)
                    #if position not in dic and closer to solved, add it
                    insert=False
                    if not dicPos.get(str(newRedi.cube)):
                        insert =True
                    elif dicPos[str(newRedi.cube)]["prof"]>profondeur: #smaller prof=closer from start
                        insert=True
                    if insert :
                        dicPos[str(newRedi.cube)]={"prof":profondeur,"posPrec":redi.cube}
                    recuCreate(newRedi, profondeur+1,profMax)
                    
                    
def findPath(inputRedi):
    redi=copy.deepcopy(inputRedi)
    #retourne toutes les étapes pour arriver à la position résolue à partire d'une position donnée
    etapes=[]
    actuel = {"prof":1000,"posPrec":redi.cube}
    while actuel["prof"]>1:
        try :
            new=copy.deepcopy(dicPos[str(actuel["posPrec"])])
        except :
            print("Non présent dans le dic")
            break
        if new==actuel:
            print("Actuel = nouveau")
            break
        etapes.append(actuel)
        actuel=new
    etapes.append({"prof":0,"posPrec":solvedCube})
    return etapes

def createDic(profondeur) : 
    global dicPos
    dicPos={}
    dicPos[str(solvedCube)]={"prof":0,"posPrec":solvedCube}
    initialRedi=RediClass.Redi()
    recuCreate(initialRedi, 1,profondeur)  
    return(dicPos)

#ajouter des éléments dans un dicto existant
def addToDic(profondeurMaxActuelle,newProf):
    dicIter=copy.deepcopy(dicPos)
    counter=0 #counter to know where we are in the execution
    start_time = time.time() #to know time of exec
    for key in dicIter:
        if dicPos[key]["prof"]==profondeurMaxActuelle:
            redi=RediClass.Redi(dicPos[key]["posPrec"])
            recuCreate(redi, profondeurMaxActuelle, newProf)
            counter+=1
            #if counter%10==0:
            print("nb : ",counter,"time : ",(time.time() - start_time),"s")

def timeFunc(prof):
    start_time = time.time()
    res=createDic(prof)
    tempsEx=(time.time() - start_time)
    taille=len(res)
    print("profondeur : ",prof)
    print(f"{tempsEx} seconds" )
    print("taille : ",taille)
    return (tempsEx,taille)

def testFindPath():
    #creation dic
    createDic(4)
    dicStats()
    print("dic created")
    
    #mélange
    redi=RediClass.Redi()
    redi.rotate(2, "down", -1)
    redi.rotate(1, "up", -1)
    redi.rotate(1, "down", 1)
    redi.rotate(1, "up", 1)
    redi.rotate(1, "up", 1)
    afficherSimple(copy.deepcopy(redi.cube), 3)
    #pos.append(redi.cube)
    #afficherListePositions(pos,5)

    #résolution
    chemin=findPath(redi)
    pos=[etat["posPrec"] for etat in chemin]
    afficherListePositions(pos,2)
    print(chemin)
    return chemin

def testFindPathNRandom(n):
    #melange
    redi=RediClass.Redi()
    for i in range (n):
        y=random.choice(["up","down"])
        side=random.choice([1,2])
        z=random.choice([1,-1])
        redi.rotate(side,y,z)
    afficherSimple(copy.deepcopy(redi.cube), 3)
    
    #resolution
    chemin=findPath(redi)
    pos=[etat["posPrec"] for etat in chemin]
    afficherListePositions(pos,2)
    return chemin
    
def findPathSimpl(initialState):
    #retourne toutes les étapes pour arriver à la position résolue à partire d'une position donnée
    etapes=[]
    solved=4
    actuel = initialState
    dicSimp={"1":2,"2":3,"3":4}
    etapes.append(actuel)
    while actuel!=solved:
        new=dicSimp[str(actuel)]
        if new==actuel:
            print("probleme")
        actuel=new
        etapes.append(actuel)
    return etapes    

def testAffichage(prof,temps=1,key=True):
    res=createDic(prof)
    print(len(res))
    pos=0
    if key :
        pos= list(map(literal_eval,list(res.keys()))) #converting string to array
    else :
        pos=[etat["posPrec"] for etat in res.values()]
    afficherListePositions(pos,temps)
    
def dicStats():
    profs=[val["prof"] for val in dicPos.values()]
    counter=Counter(profs)
    print(counter)
    return counter
    
def testKeyVal(prof):
    res=createDic(prof)
    print(len(res))
    #print(dicPos)
    counter=0
    keys= list(res.keys()) #converting string to array
    for k in keys:
        pass
        if k==dicPos[k]["posPrec"]:
            counter+=1
    print("total errors : ",counter)
    
def saveDic():
    with open('dicPos.txt', 'w') as file:
        file.write(json.dumps(dicPos)) # use `json.loads` to do the reverse
        
def loadDic():
    global dicPos
    with open('dicPos.txt', 'r') as file:
        dicPos=json.load(file)
    dicStats()
    return dicPos
    


if __name__=="__main__":
    #timeFunc(3)
    loadDic()
    addToDic(10, 12)
    #testFindPathNRandom(4)
    saveDic()
    dicStats()
    #len(dicPos)
    
    
    


