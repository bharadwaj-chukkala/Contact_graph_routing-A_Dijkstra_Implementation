# Contact Graph Routing

## Introduction

"[Routing in the Space Internet: A Contact Graph Routing Tutorial](https://www.sciencedirect.com/science/article/pii/S1084804520303489)" is a paper that provides an overview of contact graph routing, a routing technique used in the Space Internet. The Space Internet is a network of interconnected communication nodes, such as satellites, that operate in outer space.

A contact graph is a data structure that represents the connectivity of nodes in a network. In the context of the Space Internet, a contact graph represents the times at which communication links between satellites are available. The graph is constructed by considering each satellite as a node, and connecting them with edges that represent the times at which communication links can be established between them. This graph is dynamic, meaning that it changes over time as the satellites move and the communication links become available or unavailable.

Contact graph routing is a technique for routing data packets through the Space Internet using the contact graph. The routing algorithm determines the optimal path for a data packet to travel through the network by considering the availability of communication links between satellites. The algorithm searches the contact graph to find a path that meets certain constraints, such as minimizing the time it takes for the packet to reach its destination or maximizing the reliability of the communication link.

## Objective of Project

**The goal of this project is**to implement the Dijkstra algorithm on contact graphs as explained in Algorithm 1, Algorithm 2, and Algorithm 3 in section 4 of the paper. Dijkstra tries to find a valid path in the contact graph min**i**mizing the **arrival time** as its metric (which corresponds to the **path cost** in regular Dijkstra).

### Conditions

- Implement a minimum priority queue using a heap, which will be used inDijsktra.
- Implement Dijkstra as outlined in section 4 of the paper, butyou must use your min priority queue instead of the linear search used by the CSP() function in the paper

### Assumptions

- You dont have to include the parts in provided algorithms dealing with ``suppr``, ``suppr_nh`` and ``MAV``.
- Assume $owlt_{mgn} = 0$ so no need to include this either.

## Dependencies

- [Python 3](https://www.python.org/downloads/)
- [numpy](https://numpy.org/) ``pip install numpy``
- [tqdm](https://pypi.org/project/tqdm/) ``pip install tqdm``
- [heapq](https://docs.python.org/3/library/heapq.html)

## Usage

To run the program, you can use the following command:

```python
python contact_graph_routing.py
```

`ContactList.txt` is the name of the file containing the list of all contacts.

## How it Works

The program reads gets it's inputs and creates ``Contact`` objects for each contact in the contact list. Each ``Contact`` object has the following attributes and more:

- `contact_id` is a unique identifier for the contact,
- `start_time` and `end_time` represent the start and end times of the contact
- `sender` and `receiver` are the IDs of the nodes involved in the contact
- `owlt` is the one-way light time of the contact.
- `arr_time` is the arrival time of the contact.
- `pred` is the predecessor of the contact in the optimal path.
- `visited` is a boolean flag to indicate if the contact has been visited.
- `visisted_n` is a set of all the nodes that have been visited.

The program then uses a modified version of **Dijkstra's algorithm** to find the shortest path from node 1 to node 12 in the contact graph. The optimal path is defined as the path with the least overall one-way light time (OWLT). The dijksyra algorithm contains of two utility functions:

1. **The Contact Review Procedure (CRP)** updates the arrival time metric (cost) for all successor contacts of C_curr, by adding the cost of C_curr to the transmission delay of the contact. This gives an estimate of the total time it would take to transmit a message from the source node to the destination node, via the current path.
2. **The Contact Selection Procedure (CSP)** selects the contact with the best cost metric (minimum arrival time) among the successor contacts of C_curr, which becomes the new "current contact" (C_next) for the next iteration.

Finally the program outputs the contact IDs corresponding to the optimal path and the resulting best arrival time.

## Contact Graph Example

Here is an example of a contact graph:

```
contact_id   start_time   end_time sender receiver    owlt
   1          0.010000    0.400000   3       8       5.231711
   2          0.010000    0.400000   8       3       5.231711
   3          0.010000    0.930000   2       4       43.745523
   4          0.010000    0.930000   4       2       43.745523
   5          0.010000    2.640000   2       7       45.865161
```

## Result

```
Reading contact graph: 100%|████████████| 
Searching for optimal path: 100%|███████████████|
Printing Results of search:   0%|

Optimal path has been found

------------------------------------
Hop 1: 1.0 -> 4.0 | Contact - 41.0
------------------------------------
------------------------------------
Hop 2: 4.0 -> 2.0 | Contact - 34.0
------------------------------------
------------------------------------
Hop 3: 2.0 -> 8.0 | Contact - 97.0
------------------------------------
------------------------------------
Hop 4: 8.0 -> 6.0 | Contact - 96.0
------------------------------------
------------------------------------
Hop 5: 6.0 -> 12.0 | Contact - 135.0
------------------------------------

Nodes visited: [1.0, 4.0, 2.0, 8.0, 6.0, 12.0]
Optimal path: [41.0, 34.0, 97.0, 96.0, 135.0]
Best arrival time: 127.38

------------------------------------
Results Printed
Printing Results of search: 100%|█████████████████| 
```

## Authors

**Bharadwaj Chukkala** <br>
UID: 118341705 <br>
Bharadwaj Chukkala is currently a Master's student in Robotics at the University of Maryland, College Park, MD (Batch of 2023). His interests include Machine Learning, Perception and Path Planning.<br>
[![Contact](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](bchukkal@umd.edu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bharadwaj-chukkala/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bharadwaj-chukkala)

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
