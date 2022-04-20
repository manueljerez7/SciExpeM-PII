from ast import parse
from parseReactions import parseReactions
from reactions import Reaction
from getSpecies import getSpecies
from species import Species

def getReactions(species,dataKinetics,dataNames):

    reactionNames,lnA,beta,eOverR,threeBodyList,lindList,troeList,pressLogList,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList = parseReactions(dataKinetics,dataNames)
    i=0
    reactionList = []
    for e in reactionNames:
        index=i+1
        if(index in threeBodyList):
            threeBodyBool=True
        else:
            threeBodyBool=False

        if(index in lindList):
            lindBool=True
        else:
            lindBool=False

        if(index in troeList):
            troeBool=True
        else:
            troeBool=False

        if(index in pressLogList):
            pressBool=True
        else:
            pressBool=False
        
        #Is not any of the cases above, so we use the standard constructor
        newSpecies = Reaction(index,e,species,lnA[i],beta[i],eOverR[i],threeBodyBool,lindBool,troeBool,pressBool,pressLogDict,lnaFallOffDict,betaFallOffDict,eOverRFallOffDict,threeBodyDict,fallOffThreeBodyDict,troeCoefList)
        reactionList.insert(i,newSpecies)
        i=i+1
    return reactionList

