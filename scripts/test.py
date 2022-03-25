from ast import parse
from parseReactions import parseReactions
from reactions import Reaction
from loadSpecies import getSpecies
from species import Species
from kinetics import Kinetics

kinetics,species = getSpecies()

a=[species[0],species[5]]
b=[3,2]
c=dict(zip(a,b))
listkeys=list(c.keys())

print('a')