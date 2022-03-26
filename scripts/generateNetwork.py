from loadReactions import getReactions
from loadSpecies import getSpecies
from kinetics import Kinetics
from species import Species
from reactions import Reaction
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

kinetics,species = getSpecies()
reactions = getReactions()

speciesNames = []
G = nx.Graph()
for e in species:
    speciesNames.append(e.name)

G.add_nodes_from(speciesNames)

for e in reactions:
    elements=list(e.reactantsObject.keys())+list(e.productsObject.keys())
    i=0
    for s in elements:
        for node in elements[i+1:]:
            if(G.has_edge(elements[i], node)==False):
                G.add_edge(elements[i], node)
        i=i+1

#nx.draw(G, with_labels=True)
#plt.show()
pos = nx.spring_layout(G, k=0.5, iterations=50)
for n, p in pos.items():
    G.nodes[n]['pos'] = p

print('1')

edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

print('1a')

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])

print('2')

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
    x, y = G.node[node]['pos']
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])

print('3')


for node, adjacencies in enumerate(G.adjacency()):
    node_trace['marker']['color']+=tuple([len(adjacencies[1])])
    node_info = adjacencies[0] +' # of connections: '+str(len(adjacencies[1]))
    node_trace['text']+=tuple([node_info])

print('4')


fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>AT&T network connections',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="No. of connections",
                    showarrow=False,
                    xref="paper", yref="paper") ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

print('5')

go.iplot(fig)
go.plot(fig)
fig.show()