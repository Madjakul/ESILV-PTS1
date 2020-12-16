# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:53:01 2020

@author: ulyss
"""



def n_random(n): #fait n mouvements aléatoires
    #initialisation
    redi=RediClass.Redi()
    window=gui.GUI(redi.cube)
    
    #10 mouvements aléatoires
    for i in range(10):
        time.sleep(2)
        side=random.randint(0,4)
        y=random.choice(["up","down"])
        z=random.choice([-1,1])
        print(f" side : {side} \n y : {y} \n z : {z} \n")
        redi.rotate(side,y,z)
        window.afficher(redi.cube)
        
    window.quit()
    
def one_move(side,y,z):
    #initialisation
    redi=RediClass.Redi()
    window=gui.GUI(redi.cube)
    redi.rotate(side,y,z)
    window.afficher(redi.cube)
    time.sleep(10)
    
    window.quit()

if __name__=="__main__": 
    import gui
    import RediClass
    import time
    import random
    
    one_move(3, "up", 1)