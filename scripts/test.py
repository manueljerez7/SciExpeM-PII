from gettext import find
import numpy as np
from getReactions import getReactions
from networkFunctions import getPropertiesOfNode
from species import Species
from getSpecies import getSpecies
from getDistanceBetweenSpecies import compareElements
from species import findSpeciesByName
from networkFunctions import generateNetwork
import matplotlib.pyplot as plt


kinetics,species1 = getSpecies("xml/kinetics.xml")
reactions1 = getReactions(species1,"xml/kinetics.xml","xml/reaction_names.xml")

kinetics,species2 = getSpecies("xml/kinetics2.xml")
reactions2 = getReactions(species2,"xml/kinetics2.xml","xml/reaction_names2.xml")

compareElements('CH4',['MANU','MANUEL','O2','CH3','H2O'],species1,species2,reactions1,reactions2)
