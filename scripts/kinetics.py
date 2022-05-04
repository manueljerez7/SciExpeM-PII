import xml.etree.ElementTree as ET
from species import Species

class Kinetics:
    ########################################################################
    #Gets the name of the kinetics file and creates the Kinetics object
    ########################################################################
    def __init__(self,kineticsFile):
        tree = ET.parse(kineticsFile)
        root = tree.getroot()
        self.author=root[0][0].text
        self.place=root[0][1].text
        self.date=root[0][2].text
        self.time=root[0][3].text
