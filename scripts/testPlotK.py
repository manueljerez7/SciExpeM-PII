from getReactions import getReactions
from getSpecies import getSpecies
from plotK import *

#First we need to get the species and reactions objects
kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
#Plot the forward reaction rate of a elementary reaction
plotKElementary(reactions[5],1,600)
