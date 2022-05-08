from gettext import find
from getReactions import getReactions
from networkFunctions import getPropertiesOfNode
from species import Species
from getSpecies import getSpecies
from compare import *
from findSpeciesByName import findSpeciesByName
from networkFunctions import generateNetwork
from ontology import ontology

kinetics,species = getSpecies("xml/kinetics.xml")
reactions = getReactions(species,"xml/kinetics.xml","xml/reaction_names.xml")
ontology(species,reactions)
