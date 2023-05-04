import heapq

def contact_selection_procedure(contact_graph, BDT):
    """
    Returns the next contact to be processed, according to a selection procedure.

    Args:
        contact_graph (list): A list of Contact objects to be processed.
        BDT (float): The current time, as a float.

    Returns:
        Contact or None: The next Contact to be processed, or None if there are no Contacts to be processed.
    """
    queue = []
    for C in contact_graph:
        if C.arr_time > BDT or C.visited:
            continue # Skip C
        
        "Commented Linear Search Implementation"
            # if C.arr_time < t_earliest_arrival:
            #     C_next = C
            #     t_earliest_arrival = C.
        
        "Priority Queue Implementation"
        heapq.heappush(queue, (C.arr_time, C))
    if queue:
        # Return the contact with the shortest arrival time in the heap
        return heapq.heappop(queue)[1]
    else:
        # if heap is empty, return None
        return None
    
    
    """
    Notes:
        -> This function selects the next Contact to be processed based on the earliest arrival time.
        -> Considering only Contacts that haven't been visited yet and whose arrival time is not later than the current time `BDT`. 
        -> If multiple Contacts have the same earliest arrival time, the one that appears first in the `contact_graph` list is selected. 
        -> The Contacts in the `contact_graph` list must have an `arr_time` attribute that represents their arrival time as a float, and a `visited` attribute that is initially False.

    Examples:
        >>> c1 = Contact(arr_time=1.0)
        >>> c2 = Contact(arr_time=2.0)
        >>> c3 = Contact(arr_time=0.5)
        >>> contact_graph = [c1, c2, c3]
        >>> contact_selection_procedure(contact_graph, BDT=1.5)
        c2
        >>> contact_selection_procedure(contact_graph, BDT=2.5)
        None
        >>> c3.visited = True
        >>> contact_selection_procedure(contact_graph, BDT=0.0)
        c1
    """