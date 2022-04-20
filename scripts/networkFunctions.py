from getReactions import getReactions
from getSpecies import getSpecies
from species import Species
from reactions import Reaction
import networkx as nx
import plotly.graph_objects as go

#Gets species name and plots the graph network related
def plotNetwork(s,X):
    edges= X.edges(s)
    G=X.edge_subgraph(edges)
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='RdBu',
            reversescale=True,
            color=[],
            size=15,
            colorbar=dict(
                thickness=10,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=0)))

    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color']+=tuple([len(adjacencies[1])])
        node_info = adjacencies[0]
        node_trace['text']+=tuple([node_info])

    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>Species connections',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
    fig.show()


def generateNetwork(species,reactions):
    
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

    return G

def getNetwork(species,reactions,speciesList):
    G=generateNetwork(species,reactions)
    plotNetwork(speciesList,G)

def getPropertiesOfNode(G,el):
    centrality=nx.degree_centrality(G)[el]
    betweenness=nx.betweenness_centrality(G,normalized=True)[el]
    loadCent=nx.load_centrality(G,normalized=True)[el]
    closeness=nx.closeness_centrality(G)[el]
    eigen=nx.eigenvector_centrality(G)[el]
    return centrality,betweenness,loadCent,closeness,eigen