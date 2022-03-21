import xml.etree.ElementTree as ET
from species import Species

class Kinetics:
    def __init__(self,speciesList):
        tree = ET.parse("xml/kinetics.xml")
        root = tree.getroot()
        self.author=root[0][0].text
        self.place=root[0][1].text
        self.date=root[0][2].text
        self.time=root[0][3].text
        self.species=speciesList

    def compareElements(self,el1,el2):
        equal = 1
        if(el1.elementComp == el2.elementComp):
            #They have same element composition, now compare other values
            #As we could have same values but disordered, we sort and compare
            if(sorted(el1.nasaCoef)==sorted(el2.nasaCoef) and sorted(el1.lennJones)==sorted(el2.lennJones)):
                pass
            else:
                equal=0
        else:
            equal=0
        return equal