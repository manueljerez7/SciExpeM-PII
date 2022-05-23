from species import Species
from reactions import Reaction
import csv
import numpy as np

def ontology(species,reactions):
    reactantsOntology=[]
    productsOntology=[]
    reversability=[]
    reactionOrder=[]
    applyReactionNumber=[]
    hasStoichiometricNumber=[]
    indicatesMultiplicityOf=[]
    participatesIn=[]
    arheniusReaction=[]
    arheniusCoef=[]
    arhIsACoef=[]
    fallOffReaction=[]

    for r in reactions:
        #is-a (ReverseReaction    ForwardReaction)
        if (r.reversability==True):
            reversability.append(["ReverseReaction","is-a",r.name])
        else:
            reversability.append(["ForwardReaction","is-a",r.name])
        
        #arheniusReaction arheniusCoefficient arheniusIsACoeff  fallOffReaction
        arheniusReaction.append(["ArrheniusReaction","is-a",r.name])
        arheniusCoef.append([r.name,"hasArrheniusCoefficient",str(r.lnA)])
        arhIsACoef.append([str(r.lnA),"is-a","RateCoefficient"])
        if(r.isTroe==True or r.isLindemann==True):
            fallOffReaction.append(["FallOffReaction","is-a",r.name])
        

        #hasReactionOrder
        aux1=r.reactants
        aux2=r.products
        if('M' in list(aux1.keys())):
            aux1.pop('M')
            aux2.pop('M')
        n1=list(aux1.values())
        n2=list(aux2.values())
        n3=n1+n2
        number=np.sum(n3)
        reactionOrder.append([r.name,"hasReactionOrder",str(number)])

        #hasStoichiometricCoefficient
        #we already computed a list with all the stoichometry coefficients
        for n in n3:
            hasStoichiometricNumber.append([r.name,"hasStoichiometricNumber",str(n)])

        #hasReactant    hasProduct  appliesTo   indicatesMultiplicityOf participatesIn
        reactants=list(r.reactants.keys())
        products=list(r.products.keys())
        for re in reactants:
            reactantsOntology.append([r.name,"hasReactant",re])
            applyReactionNumber.append([str(number),"appliesTo",re])
            indicatesMultiplicityOf.append([r.reactants[re],"indicatesMultiplicityOf",re])
            if (r.reversability==False):
                participatesIn.append([re,"participatesIn","ForwardReaction"])

        for p in products:
            productsOntology.append([r.name,"hasProduct",p])
            applyReactionNumber.append([str(number),"appliesTo",p])
            indicatesMultiplicityOf.append([r.products[p],"indicatesMultiplicityOf",p])
            if (r.reversability==True):
                participatesIn.append([re,"participatesIn","ReverseReaction"])

    #isASpecies hasElement  hasElementNumber    indicatesNumberOf
    isASpecies=[]
    hasElement=[]
    hasElementNumber=[]
    d1=["C","H",'O','N','HE','AR']
    d2=['6','1','8','7','2','18']
    dictElements=dict(zip(d1,d2))
    indicatesNumberOf=[]
    for e in d1:
        indicatesNumberOf.append([dictElements[e],"indicatesNumberOf",e])
    for s in species:
        isASpecies.append([s.name,"is-a","species"])
        keys=list(s.elementComp.keys())
        for k in keys:
            if(s.elementComp[k]>0):
                hasElement.append([s.name,"hasElement",k])
                hasElementNumber.append([s.name,"hasElementNumber",dictElements[k]])
    

    with open('ontology/test.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(reactantsOntology)
            write.writerows(productsOntology)
            write.writerows(reversability)
            write.writerows(reactionOrder)
            write.writerows(applyReactionNumber)
            write.writerows(indicatesMultiplicityOf)
            write.writerows(isASpecies)
            write.writerows(hasElement)
            write.writerows(hasElementNumber)
            write.writerows(indicatesNumberOf)
            write.writerows(participatesIn)
            write.writerows(arheniusReaction)
            write.writerows(arheniusCoef)
            write.writerow(arhIsACoef)
            write.writerows(fallOffReaction)
            
            print('File written')