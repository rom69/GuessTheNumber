############################
# Game project             #
# Created the 2014-12-27   #
#        Main file         #
############################

import util #miscellaneous functions utilities
import random

debug = 0

## Main program ##
#Say hi
util.greeting()

#Randomly pick a number:
numberToGuess = random.randint(0, 100)
if(debug):
    print 'numberToGuess is %d ' % numberToGuess


from random import randrange
 
def initialize():
    global ChiffreAleatoire
    ChiffreAleatoire = randrange(1, 100)
    print("Entrez un chiffre entre 1 et 100")
 
def VerifieNombre(Chiffre, ChiffreAleatoire):
    if Chiffre == ChiffreAleatoire:
        print("C'est le bon chiffre, bravo!")
        Possible = True
    elif Chiffre > ChiffreAleatoire:
        print("C'est moins!")
        Possible = False
    elif Chiffre < ChiffreAleatoire:
        print("C'est plus!")
        Possible = False
    return Possible
 
def Continuer():
    Reponse = input("Voulez vous rejouer (o/n) ? ")
    if Reponse.upper() == "O":
        initialize()
        Boucle = True
    elif Reponse.upper() == "N":
        Boucle = False
    return Boucle
 
Boucle = True
initialize()
while Boucle == True:
    Chiffre = int(input())
    Possible = VerifieNombre(Chiffre, ChiffreAleatoire)
    if Possible == True:
         Boucle = Continuer()




#Say bye
util.seeyouing()
