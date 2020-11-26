# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:53:01 2020

@author: ulyss
"""

import gui
import RediClass
import time
import random

#initialisation
redi=RediClass.Redi()
window=gui.GUI(redi.cube)

#10 mouvements aléatoires
for i in range(10):
    time.sleep(2)
    side=random.randint(0,3)
    y=random.choice(["up","down"])
    z=random.choice([-1,1])
    print(f" side : {side} \n y : {y} \n z : {z} \n")
    redi.rotate(side,y,z)
    window.afficher(redi.cube)
    
window.quit()