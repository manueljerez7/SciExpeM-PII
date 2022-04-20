from parseSpecies import parseSpecies
from species import Species
from kinetics import Kinetics

def getSpecies(data):
    elementsList, atomicComp, numberOfSpecies, speciesNames, nasaCoef, lennard = parseSpecies(data)
    i=0
    speciesList = []
    for e in speciesNames:
        elements = dict(zip(elementsList,atomicComp[i]))
        newSpecies = Species(i+1,e,elements,nasaCoef[i],lennard[i])
        speciesList.insert(i,newSpecies)
        i=i+1

    kinetics = Kinetics(speciesList)
    return kinetics,speciesList
