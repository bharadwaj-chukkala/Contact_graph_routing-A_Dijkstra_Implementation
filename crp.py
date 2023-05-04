import heapq

# One way light time margin
owlt_mgn = 0.000000

def contact_review_procedure(contact_graph, C_curr, C_fin, BDT, D):
    """
    Finds the earliest contact between two nodes that haven't been visited yet.

    Args:
        contact_graph (list): A list of Contact objects representing all possible contacts.
        C_curr (Contact): The current contact being processed, from which the search starts.
        C_fin (Contact): The current earliest contact found so far.
        BDT (float): The current time, as a float.
        D (NodePair): The source-destination node pair.

    Returns:
        C_fin: The earliest Contact found between the two nodes 
        BDT: its arrival time, 
        Note: It will return the original values of C_fin and BDT if no earlier Contact is found.

    """
    queue = []
    for C in contact_graph:
        
        # Ignore Condtions Test
        if C.sender != C_curr.receiver:
            continue # Skip C           
        if C.end <= C_curr.arr_time:     
            continue # Skip C           # Ignore due contacts
        if C.visited:
            continue # Skip C           # Ignore visited
        if C.receiver in C_curr.visited_n:
            continue # Skip C           # ignore visited nodes
        
        "Ignoring these conditions because it is out of the project scope"
        # if C.suppr or C in C_curr.suppr_nh:
        #     continue # Skip C           # Ignore suppressed contacts
        # if C.MAV(0) == 0:
        #     continue # Skip C           # Ignore overbooked contacts
        
        if C.start < C_curr.arr_time:
            arr_time = C_curr.arr_time
        else:
            arr_time = C.start
        arr_time += C.owlt + owlt_mgn
        
        if arr_time < C.arr_time:
            C.arr_time = arr_time
            C.pred = C_curr
            C.visited_n = C_curr.visited_n.union({C.receiver}) 
            
            if C.receiver == D.sender and C.arr_time < BDT:
                C_fin = C
                BDT = C.arr_time
    
        heapq.heappush(queue, (C.arr_time, C))
    
    C_curr.visited = True
    
    return C_fin, BDT


##########################################################################################
"""
Notes:
    -> This function searches the `contact_graph` for Contacts that meet certain criteria. 
    -> A Contact is eligible if it involves the same two nodes as `C_curr`:
        - its end time is later than `C_curr.arr_time`
        - it hasn't been visited yet
        - its receiver node hasn't been visited yet either. 
    -> For each eligible Contact, the function calculates its arrival time.
    -> Then, updates the Contact's `arr_time`, `pred`, and `visited_n` attributes if a shorter arrival time is found. 
    -> If the updated Contact involves the destination node as receiver and arrives before `BDT`, 
       it becomes the new `C_fin` and `BDT` values. 
    -> The function returns a tuple with the updated `C_fin` and `BDT` values, or the original ones if no earlier Contact is found.

Examples:
    >>> c1 = Contact(sender=1, receiver=2, arr_time=1.0, start=2.0, end=3.0, owlt=0.1)
    >>> c2 = Contact(sender=2, receiver=1, arr_time=3.0, start=4.0, end=5.0, owlt=0.2)
    >>> c3 = Contact(sender=2, receiver=3, arr_time=1.5, start=2.5, end=3.5, owlt=0.15)
    >>> contact_graph = [c1, c2, c3]
    >>> D = Contact(sender=1, receiver=3)
    >>> C_fin, BDT = None, 2.5
    >>> C_curr = c1
    >>> contact_review_procedure(contact_graph, C_curr, C_fin, BDT, D)
    (c3, 2.75)
"""