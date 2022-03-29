from gettext import find
import numpy as np
from species import Species
from loadSpecies import getSpecies
from getDistanceBetweenSpecies import getDistanceBetweenSpecies
from species import findSpeciesByName

kinetics,species = getSpecies()

print(getDistanceBetweenSpecies(findSpeciesByName('O2',species),findSpeciesByName('O',species)))
