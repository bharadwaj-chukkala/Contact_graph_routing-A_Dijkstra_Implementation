import numpy as np
import heapq
from crp import contact_review_procedure
from csp import contact_selection_procedure
from tqdm import tqdm

owlt_mgn = 0.000000

class Contact:
    """
    Represents a contact between two nodes in a communication network.
    """
    def __init__(self, id, start, end, sender, receiver, owlt):
        """
        Initializes a new instance of the Contact class.

        Args:
            id (int): The unique identifier of the contact.
            start (float): The start time of the contact.
            end (float): The end time of the contact.
            sender (int): The ID of the node that initiated the contact.
            receiver (int): The ID of the node that received the contact.
            owlt (float): The one-way latency time for the contact.
        """
        self.id = id
        self.start = start
        self.end = end
        self.sender = sender
        self.receiver = receiver
        self.owlt = owlt
        self.pred = None                # Predecessor contact in the shortest path
        self.arr_time = np.inf          # Arrival time at the contact 
        self.visited = False            # Flag to indicate if the contact has been visited
        self.visited_n = set()          # Set of visited nodes 
    
    def __lt__(self, other):
        """
        Compares two Contact objects based on their arrival times for use in a priority queue.

        Args:
            other (Contact): The Contact object to compare with this Contact.

        Returns:
            bool: True if this Contact's arrival time is less than the other Contact's, False otherwise.
        """
        return self.arr_time < other.arr_time
        

def dijkstra_contact_search(contact_graph, C_root, D):
    """
    
    The function implements the Dijkstra's algorithm for searching the shortest path in a contact graph, 
    starting from a given source contact C_root and ending at a destination contact D. 

    Args:

        contact_graph (list): A list of Contact objects representing the contact graph.
        C_root (Contact): The source contact object to start the search from.
        D (Contact): The destination contact object to end the search at.
    
    Returns:

        path (list): A list of Contact objects representing the shortest path from C_root to D.
        BDT (float): The earliest possible arrival time at D from C_root.
        
    """
    # Initializations 
    path = []               # Initialize the path to be returned
    C_fin = None            # Initialize the earliest contact found so far
    BDT = np.inf            # Initialize the earliest arrival time found so far
    C_root.arr_time = 0     # Set the arrival time of the source contact to 0
    C_curr = C_root         # Set the current contact to the source contact
    
    while True:
        # Review and Selection Procedures
        
        C_fin, BDT = contact_review_procedure(contact_graph, C_curr,C_fin, BDT, D)
        C_next = contact_selection_procedure(contact_graph, BDT)
        #C_next.pred = C_curr
        
        if C_next != None:
            C_curr = C_next
        else:
            break    
           
        # Review and Selection Procedures are finished
    
    # Construct the path from the destination contact to the source contact
    if C_fin != None:
        C = C_fin
        while C != C_root:
            path.append(C)
            C = C.pred
        path.reverse()
    
    return path, BDT
  
if __name__ == '__main__':
   
    contact_graph = []                              # Contact Plan
    C_art = Contact(0,0,np.inf,1,1,0)               # Artificial Contact to start the search
    contact_graph.append(C_art)                     # Append the artificial contact to the contact plan
    
    # Read the contact graph from the file
    with tqdm(total=100, desc='Reading contact graph', unit='%') as pbar:   
        with open('ContactList.txt', 'r') as f:
            for line in f:
                id, start, end, sender, receiver, owlt = map(float, line.split())
                contact = Contact(id, start, end, sender, receiver, owlt)
                contact_graph.append(contact)
        pbar.update(100)
    
    # Run the search algorithm
    with tqdm(total=100, desc='Searching for optimal path', unit='%') as pbar:
        path, cost = dijkstra_contact_search(contact_graph, contact_graph[0], contact_graph[-1])
        pbar.update(100)

    # Output the results
    with tqdm(total=100, desc='Printing Results of search', unit='%') as pbar:
        if path is None:
            print("No path found")
        else:
            print("\nOptimal path has been found:")
            for i, C in enumerate(path):
                print("------------------------------------")
                if i == 0:
                    print(f"Hop {i+1}: {C.sender} -> {C.receiver} | Contact - {C.id}")
                else:
                    prev_C = path[i-1]
                    print(f"Hop {i+1}: {prev_C.receiver} -> {C.receiver} | Contact - {C.id}")
                print("------------------------------------")
            
            print("\nNodes visited:", [C.sender for C in path] + [path[-1].receiver])
            print("Optimal path:", [C.id for C in path])
            print("Best arrival time:", format(cost, ".2f"))
            print("\n------------------------------------")
            print("Results Printed")
        pbar.update(100)

