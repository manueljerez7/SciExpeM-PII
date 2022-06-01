from getReactions import getReactions
from getSpecies import getSpecies
from compare import *

#First we need to get the species and reactions objects
kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
#We will compare element H2O against other elements of the same model
compareSpecies('H2O',['AR','H2','CO2'],species,species,reactions,reactions)
