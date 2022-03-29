from species import Species
import numpy as np

#Gets two species and returns 3 distances related to them
#If the species have tha same composition, they are the same, thus all distances are true
#If they are not the same, the distances returned are the distance between NASA coeff, lennJones coeff and absolute
#The distance between NASA and LenJones are sqrt(sum(Xi-Yi)^2)
def getDistanceBetweenSpecies(el1,el2):
    l1=np.array(el1.nasaCoef)
    l2=np.array(el2.nasaCoef)
    nasaSubs = np.subtract(l1, l2)
    power=np.power(nasaSubs,2)
    nasaDist=np.sqrt(np.sum(power))

    l1=np.array(el1.lennJones)
    l2=np.array(el2.lennJones)
    lennJonesSubs = np.subtract(l1, l2)
    lennJonesDist=np.sqrt(np.sum(np.power(lennJonesSubs,2)))

    absDist=np.sqrt(nasaDist**2+lennJonesDist**2)

    return nasaDist,lennJonesDist,absDist

