from species import Species

########################################################################
#gets the list of species and the name of a species and returns the
#species object matching that name
########################################################################
def findSpeciesByName(species,name):
    for e in species:
        if(name==e.name):
            return e
        else:
            pass