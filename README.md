# Contact Graph Routing

## Introduction

This is a Python implementation of Dijkstra's algorithm to find the shortest path in a contact graph. A contact graph is a directed graph where each edge represents a contact between two nodes at a specific time period. The goal is to find the optimal path from **node 1** to **node 12**, where the optimal path is defined as the path with the least overall one-way light time (OWLT).

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

The program reads gets it's inouts and created ``Contact`` objects for each contact in the contact list. Each ``Contact`` object has the following attributes and more:

- `contact_id` is a unique identifier for the contact,
- `start_time` and `end_time` represent the start and end times of the contact
- `sender` and `receiver` are the IDs of the nodes involved in the contact
- `owlt` is the one-way light time of the contact.
- `arr_time` is the arrival time of the contact.
- `pred` is the predecessor of the contact in the optimal path.
- `visited` is a boolean flag to indicate if the contact has been visited.
- `visisted_n` is a set of all the nodes that have been visited.

The program then uses Dijkstra's algorithm to find the shortest path from node 1 to node 12 in the contact graph. The optimal path is defined as the path with the least overall one-way light time (OWLT).

The program outputs the contact IDs corresponding to the optimal path and the resulting best arrival time.

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

**Bharadwaj Chukkala**<br>
UID: 118341705<br>
Bharadwaj Chukkala is currently a Master's student in Robotics at the University of Maryland, College Park, MD (Batch of 2023). His interests include Machine Learning, Perception and Path Planning.<br>
[![Contact](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](bchukkal@umd.edu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bharadwaj-chukkala/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bharadwaj-chukkala)

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
