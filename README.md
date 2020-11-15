# Graph Clique

- This repository contains a library for calculating cliques in a undirected graph as well as utils for graph generation and visualization.
- In an undirected graph, a clique is a complete sub-graph of the given graph, where all the vertices are connected to all the other vertices of this sub-graph. The maximum clique problem is the computational problem of finding maximum clique of the graph
- Practical applications of the maximum clique include networking applications and systems (e.g. to understand the network topology, improve package routing), DNA analysis, economics, fault tolerance system.



### Visualization Tools

For easier visualization of the graphs a set of tools was developed using the PyGame library. The tools presented in Figure 1 allows do draw the graphs being analyzed.

It is possible to overlay graphs and highlight with a different color to verify and debug the results obtained from the developed solutions.

<img src="https://raw.githubusercontent.com/tentone/clique/master/readme/b.jpg" width="300"><img src="https://raw.githubusercontent.com/tentone/clique/master/readme/a.jpg" width="300">



### Brute-Force

The first solution was implemented using a brute-force approach, the existence of a clique can be tested for the combination of all vertices for a clique size n.

We start by testing all the combinations of vertices from C(v, 2) up to C(v, v) iterating trough all clique sizes available in the graph. After finding the first clique of the size being tested, we move to the next size it is not necessary to iterate all cliques for each size.

<img src="https://raw.githubusercontent.com/tentone/clique/master/readme/up.jpg" width="500">

Since we only need to find the maximum clique it can be more efficient to start directly from the biggest hypothesis, the first clique found can be directly assumed as the biggest available in the graph without need to iterate through all the smaller combinations.

<img src="https://raw.githubusercontent.com/tentone/clique/master/readme/down.jpg" width="500">



### Greedy

Any set of vertices that belong to the maximum clique in a graph is also a clique of that graph. It is possible to optimize the previous brute-force solutions by instead of testing all possible size of cliques start by the smaller ones expanding with additional vertices. This approach was first suggested in 1975.

We can start with the full list of edges that is by definition a list of cliques with size 2. Then we start expanding these cliques to include additional vertices that have full connectivity with the already existing vertices in the set.

When no more vertices with full connectivity are found we can assume that the set of vertices composes the maximum clique of the graph.

To further speed up this approach we can for each initial set store a list of all the other vertices that need to be tested to prevent repeating vertices edge existence test

<img src="https://raw.githubusercontent.com/tentone/clique/master/readme/greedy.jpg" width="500">



### License

The project is distributed under MIT license available on the GitHub page.

