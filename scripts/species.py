class Species:

    def __init__(self,i,name,dictElements,nasaList,lennardJonesList):
        self.index=i
        self.name=name
        self.elementComp=dictElements
        self.nasaCoef=nasaList
        self.lennJones=lennardJonesList
    
    def __eq__(self,other):
        equal = 1
        if(self.elementComp == other.elementComp):
            #They have same element composition, now compare other values
            #As we could have same values but disordered, we sort and compare
            if(sorted(self.nasaCoef)==sorted(other.nasaCoef) and sorted(self.lennJones)==sorted(other.lennJones)):
                pass
            else:
                equal=0
        else:
            equal=0
        return equal
    
    def __hash__(self):
        return self.index

def findSpeciesByName(species,name):
    for e in species:
        if(name==e.name):
            return e
        else:
            pass
