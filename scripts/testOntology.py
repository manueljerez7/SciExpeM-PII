from getReactions import getReactions
from getSpecies import getSpecies
from ontology import ontology

########################################################
# Test script for generating the ontology CSV file
# Requirements:
# numpy
# csv
# xml
# ######################################################

#First we need to get the species and reactions objects
kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
#Although the file knowledge.csv is already generated on the ontology folder, here it is possible to re-generate it
ontology(species,reactions)
