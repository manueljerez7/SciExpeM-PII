from getReactions import getReactions
from getSpecies import getSpecies
from compare import *

########################################################
# Test script for plotting a graph bar comparing species
# Requirements:
# numpy
# matplotlib
# xml
# networkX
# plotly
# ######################################################

#First we need to get the species and reactions objects
kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
kinetics2,species2 = getSpecies("xml/kinetics2.xml")
reactions2 = getReactions(species,"xml/kinetics.xml","xml/reaction_names2.xml")
#We will compare element HOCO against other elements of a modified model, with different species names and some values changed
compareSpecies('HOCO',['MANU','EL','MANUEL'],species,species2,reactions,reactions2)
