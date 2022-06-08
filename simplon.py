from  array import *
Salle=[         [True,True,True,True,True,True,True,True,True],
                [True,True,True,True,True,True,True,True,True],
                [False,False,False,False,True,True,True,True,True],
                [True,True,True,True,True,True,True,True,True],
                [False,True,True,False,True,True,True,True,True],
                [True,True,True,True,True,True,True,False,False],
                [True,True,True,True,False,True,True,True,True],
                [False,False,True,True,True,True,True,True,True]]


nbplace = int(input("Combien de place voulez vous acheter? "))
rangee = int(input("A quelle rangée voulez vous aller? "))
libre=0


for i in range ( len (Salle[rangee])):
    if Salle[rangee][i]==True:
        libre+=1

if nbplace>libre:
    print("Désolé il n'y a pas assez de place")

else:
    print("Vote séance est dans la Salle 3 au deuxieme étage")


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  