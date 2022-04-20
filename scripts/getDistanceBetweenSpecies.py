from matplotlib.pyplot import table
from networkFunctions import generateNetwork, getPropertiesOfNode
from species import findSpeciesByName
from species import Species
import numpy as np
import matplotlib.pyplot as plt

#Gets two species and returns a normalized vector of the distance between them
#where the first number is the nasa coeff distance, the second is the lennard jones distance
#and the third one is the graphical distance based on different parameters of the Network Graph

def getDistanceBetweenSpecies(el1,el2,G1,G2):
    l1=np.sort(np.array(el1.nasaCoef))
    l2=np.sort(np.array(el2.nasaCoef))
    nasaSubs = np.subtract(l1, l2)
    power=np.power(nasaSubs,2)
    nasaDist=np.sqrt(np.sum(power))

    l1=np.sort(np.array(el1.lennJones))
    l2=np.sort(np.array(el2.lennJones))
    lennJonesSubs = np.subtract(l1, l2)
    lennJonesDist=np.sqrt(np.sum(np.power(lennJonesSubs,2)))

    absDist=np.sqrt(nasaDist**2+lennJonesDist**2)
    if(absDist!=0):
        nasaDist=nasaDist/absDist
        lennJonesDist=lennJonesDist/absDist

#Now we get parameters on the network related to each of the networks and elements
    
    v1 = np.array(getPropertiesOfNode(G1,el1.name))
    v2 = np.array(getPropertiesOfNode(G2,el2.name))
    vSubs=np.subtract(v1,v2)
    power=np.power(vSubs,2)
    vDist=np.sqrt(np.sum(power))

    absDist=np.sqrt(nasaDist**2+lennJonesDist**2+vDist**2)

    return nasaDist,lennJonesDist,vDist, absDist

#Compares and plots distance between one element from one model and a list of elements from other model
def compareElements(el1, listElements, species1, species2, reactions1, reactions2):
    NASAdistances=[]
    LJdistances=[]
    Ndistances=[]
    ABSdistances=[]

    el1=findSpeciesByName(species1,el1)

    G1 = generateNetwork(species1,reactions1)
    G2 = generateNetwork(species2,reactions2)
    for element in listElements:
        el2=findSpeciesByName(species2,element)
        v1,v2,v3,v4=getDistanceBetweenSpecies(el1,el2,G1,G2)
        NASAdistances.append(v1)
        LJdistances.append(v2)
        Ndistances.append(v3)
        ABSdistances.append(v4)


    N=len(listElements)
    ind = np.arange(N) 
    width = 0.2
    bar1 = plt.bar(ind, NASAdistances, width, color = 'r')
    bar2 = plt.bar(ind+width, LJdistances, width, color = 'y')
    bar3 = plt.bar(ind+width*2, Ndistances, width, color = 'g')
    bar4 = plt.bar(ind+width*3, ABSdistances, width, color = 'b')

    plt.xticks(ind+width,listElements,rotation=70) 
    plt.xlabel('Element') 
    plt.ylabel('Distance') 
    plt.title('Distance comparison to '+el1.name)
    plt.grid(color='gray',linestyle='--', linewidth=0.5)
    plt.legend( (bar1, bar2, bar3, bar4), ('NASA Distance', 'Lennard Jones Distance', 'Network Distance', 'Absolute Distance') )
    plt.show()