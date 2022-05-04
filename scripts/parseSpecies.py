import xml.etree.ElementTree as ET

####################################################################
#Gets the name of the kinetics file and returns various lists needed
#to create the species objects
####################################################################
def parseSpecies(data):
    #Parse the file
    tree = ET.parse(data)
    root = tree.getroot()
    

    #First we get the elements in an array
    elements=str.splitlines(root[2].text)[1]
    elements=elements.split(' ')[:-1] #We have to remove the last element
    numberOfElements=len(elements)

    #Now we will create a matrix with the atomic compositions
    atomicCompStr=str.splitlines(root[3].text)
    atomicCompStr.pop(0)
    atomicComp=[]
    i=0
    for row in atomicCompStr:
        values=row[:-1]
        values=row.split(' ')[:-1]
        valuesN=[int(float(x)) for x in values] #We got the numbers in a array
        atomicComp.insert(i,valuesN)
        i=i+1

    #Now we will create an array with the name of species 
    speciesStr=str.splitlines(root[5].text)
    speciesStr.pop(0)
    species=[]
    i=0
    for row in speciesStr:
        values=row[:-1]
        values=row.split(' ')[:-1]
        for element in values:
            species.insert(i,element)
            i=i+1
    numberOfSpecies=len(species)

    #Now we will create an array for NASA-coef
    nasaCoefStr=str.splitlines(root[6][0].text)
    nasaCoefStr.pop(0)
    nasaCoef=[]
    i=0
    for row in nasaCoefStr:
        values=row.split(' ')
        valuesN=[float(x) for x in values]
        nasaCoef.insert(i,valuesN)
        i=i+1


    #Now we will create an array for Lennard-Jones numbers
    lennardStr=str.splitlines(root[8].text)
    lennardStr.pop(0)
    lennard=[]
    i=0
    for row in lennardStr:
        values=row.split(' ')
        valuesN=[float(x) for x in values]
        lennard.insert(i,valuesN)
        i=i+1

    return elements, atomicComp, numberOfSpecies, species, nasaCoef, lennard

