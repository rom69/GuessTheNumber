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

#Say bye
util.seeyouing()
