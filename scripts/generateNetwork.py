from loadReactions import getReactions
from loadSpecies import getSpecies
from species import Species
from reactions import Reaction
import networkx as nx
from plotNetwork import plotNetwork

def generateNetwork(speciesList):
    kinetics,species = getSpecies()
    reactions = getReactions()

    speciesNames = []
    G = nx.Graph()
    for e in species:
        speciesNames.append(e.name)

    G.add_nodes_from(speciesNames)

    for e in reactions:
        elements=list(e.reactantsObject.keys())+list(e.productsObject.keys())
        elements = list(dict.fromkeys(elements))
        i=0
        for s in elements:
            for node in elements[i+1:]:
                if(G.has_edge(elements[i], node)==False and G.has_edge(node,elements[i])==False):
                    G.add_edge(elements[i], node)
            i=i+1

    plotNetwork(speciesList,G)

