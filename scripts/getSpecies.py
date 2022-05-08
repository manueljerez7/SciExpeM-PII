from parseSpecies import parseSpecies
from species import Species
from kinetics import Kinetics

########################################################################
#Gets the name of the Kinetics file. Returns the kinetics object and the
#list of species object
########################################################################
def getSpecies(data):
    elementsList, atomicComp, numberOfSpecies, speciesNames, nasaCoef, lennard = parseSpecies(data)
    i=0
    speciesList = []
    for e in speciesNames:
        elements = dict(zip(elementsList,atomicComp[i]))
        newSpecies = Species(i+1,e,elements,nasaCoef[i],lennard[i])
        speciesList.insert(i,newSpecies)
        i=i+1

    kinetics = Kinetics(data)
    return kinetics,speciesList
