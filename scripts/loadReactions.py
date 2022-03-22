from ast import parse
from parseReactions import parseReactions
from reactions import Reaction
from loadSpecies import getSpecies
from species import Species
from kinetics import Kinetics

kinetics,species = getSpecies()

reactionNames,lnA,beta,eOverR,threeBodyList,lindList,troeList,pressLogList,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList = parseReactions()
i=0
reactionList = []
for e in reactionNames:
    index=i+1
    if(index in threeBodyList):
        threeBodyBool=1
    else:
        threeBodyBool=0

    if(index in lindList):
        lindBool=1
    else:
        lindBool=0

    if(index in troeList):
        troeBool=1
    else:
        troeBool=0

    if(index in pressLogList):
        pressBool=1
    else:
        pressBool=0
    
    #Is not any of the cases above, so we use the standard constructor
    newSpecies = Reaction(index,e,species,lnA[i],beta[i],eOverR[i],threeBodyBool,lindBool,troeBool,pressBool,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList)
    reactionList.insert(i,newSpecies)
    i=i+1

print('Finished Generation')
