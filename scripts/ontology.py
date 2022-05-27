from species import Species
from reactions import Reaction
import csv
import numpy as np

#################################################################################################################################
    #The following implementation of the knowledge graph was done using the OntoKin definition in the paper
    #https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00960
    #The explanation for each of the implementations done is present before the code that generates the 
    #list that will write that section of the graph.
    #Apart from that, due to the lack of the information needed to implement some relations and entities,
    #the following entities and their incoming/outgoing relations were not implemented:
    #ReactionMechanism, 
    #In Phase Group: Phase, Material, GasPhase, SitePhase, BulkPhase
    #In ChemicalReaction group: GasPhaseReaction, SurfaceReaction, LandauTellerReaction,
    #                           SurfaceCoverageReaction, StickingCoefficientReaction
    #In Species Group: ThermoModel, TransportModel
    #In Rate Coefficients Group: FallOffModelCoefficient, LandauTellerRateCoefficient, CoverageDependendy, StickingCoefficient
#################################################################################################################################

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
        #The reversability of the reaction is checked with a boolean attribute of the Reaction object
        #Examples:
        #ReverseReaction,is-a,H2+M=2H+M (it is reversible as it only has the equal sign)
        #ForwardReaction,is-a,O2+CH2(S)=>H+OH+CO (it is not reversible as it has the arrow sign)

        if (r.reversability==True):
            reversability.append(["ReverseReaction","is-a",r.name])
        else:
            reversability.append(["ForwardReaction","is-a",r.name])
        
        #arheniusReaction arheniusCoefficient arheniusIsACoeff  fallOffReaction
        #Following the OntoKin schema, all the reactions should be considered as arheniusReactions as all have arhenius coefficients
        #Only some reactions are fallOffReactions, this is checked with two booleans, which are isTroe and isLindemann in the Reaction object
        #Note that TROE and Lindemann are subtypes of FallOff, so that's why we check both
        #Examples:
        #ArrheniusReaction,is-a,H2+M=2H+M
        #H2+M=2H+M,hasArrheniusCoefficient,38.362405249576234
        #38.362405249576234,is-a,RateCoefficient
        #FallOffReaction,is-a,H2O2+M=2OH+M

        arheniusReaction.append(["ArrheniusReaction","is-a",r.name])
        arheniusCoef.append([r.name,"hasArrheniusCoefficient",str(r.lnA)])
        arhIsACoef.append([str(r.lnA),"is-a","RateCoefficient"])
        if(r.isTroe==True or r.isLindemann==True):
            fallOffReaction.append(["FallOffReaction","is-a",r.name])
        
        #hasReactionOrder
        #The reaction order is the sum of the coefficients that are multiplying each of the reactants and products (which are called stoichiometric numbers)
        #Examples:
        #H2+M=2H+M,hasReactionOrder,3.0 (in the case of ThreeBody and FallOff reactions we don't take M into account)
        #H2+O=H+OH,hasReactionOrder,4.0

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
        #Indicates the stoichometric coefficients present in a reaction
        #we already computed a list with all the stoichometry coefficients in the previous step, 
        #so we just need to iterate through that list to create this relation. Again, in threebody and falloff reactions, M doesn't appear
        #Examples:
        #H2+M=2H+M,hasStoichiometricCoefficient,1.0
        #H2+M=2H+M,hasStoichiometricCoefficient,2.0

        for n in n3:
            hasStoichiometricNumber.append([r.name,"hasStoichiometricCoefficient",str(n)])

        #hasReactant    hasProduct  appliesTo   indicatesMultiplicityOf participatesIn
        #hasReactant and hasProduct are easily implemented with lists of the speciesthat appear on the reaction, we just iterate through them
        #The relation appliesTo matches the reaction order to the reactants and products of the reaction, so we use the number previously computed
        #indicatesMultiplicityOf matches the stoichiometry number with the species, indicating the multiplicity of the given reactant/product
        #participatesIn is a way to express that a reactant participates in a forward reaction and a product in a reverse reaction
        #Examples:
        #H2+O=H+OH,hasReactant,H2
        #H2+O=H+OH,hasReactant,O
        #H2+O=H+OH,hasProduct,H
        #H2+O=H+OH,hasProduct,OH

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
    #isASpecies is a list that will indicate if a given reactant/product is a species or a molecular entity
    #   It will be a species if only 1 element was present on the compound, while a molecular entity if it has more than 1 element
    #   this is checked with the atomic composition of the compound, which is a dictionary object on the Species class
    #hasElement indicates the elements that each compound is formed of. 
    #hasElement number indicates the same as the previous one, but instead of saying the name of the element, says the atomic number (unique, present on the periodic table)
    #indicatesNumberOf matches each of the 6 elements of the model with their atomic number
    #Examples:
    #H,is-a,species
    #O2,is-a,species
    #H2O,is-a,molecularEntity
    #H2O,hasElement,H
    #H2O,hasElement,O
    #H2O,hasElementNumber,1 (1 is the atomic number of Hydrogen)
    #H2O,hasElementNumber,8 (8 is the atomic number of Oxigen)
    #8,indicatesNumberOf,O

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
        composition=list(s.elementComp.values())
        if(composition.count(0)==5):
            isASpecies.append([s.name,"is-a","species"])
        else:
            isASpecies.append([s.name,"is-a","molecularEntity"])
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
            write.writerows(hasStoichiometricNumber)
            write.writerows(applyReactionNumber)
            write.writerows(indicatesMultiplicityOf)
            write.writerows(isASpecies)
            write.writerows(hasElement)
            write.writerows(hasElementNumber)
            write.writerows(indicatesNumberOf)
            write.writerows(participatesIn)
            write.writerows(arheniusReaction)
            write.writerows(arheniusCoef)
            write.writerows(arhIsACoef)
            write.writerows(fallOffReaction)
            
            print('File written')