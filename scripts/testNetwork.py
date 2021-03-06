from getReactions import getReactions
from getSpecies import getSpecies
from networkFunctions import *

########################################################
# Test script for plotting the network graph for elements H2 and O2
# Requirements:
# networkX
# plotly
# xml
# ######################################################


#First we need to get the species and reactions objects
kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
#Plot the network of species related to H2 and O2
getNetwork(species,reactions,['H2','O2'])
