'''Unfortunately,
List has a few shortcomings compared to other data structures you’ll look at.
The biggest issue is that it can run into speed issues as it grows.
The items in a list are stored with the goal of providing
fast access to random elements in the list. At a high level,
this means that the items are stored next to each other in memory.

As your list stack grows in size than that of memory it may need more time
for some memory allocations... taking much longer time for .append()

and

.insert() other than that at end position can take much longer time.

Now List v/s Deque

Lists:
    #contiguous memory allocations for easy and fast indexing.
    #The contiguous memory layout is the reason that list might
        need to take more time to .append() some objects than others.
    #not thread safe

Deque( if you’re not using threading ):
    #deque, on the other hand, is built upon a doubly linked list.
    
    #In a linked list structure, each entry is stored in its own memory block and
        has a reference to the next entry in the list.
        
    #A doubly linked list is just the same, except that each entry has references
        to both the previous and the next entry in the list.
        This allows you to easily add nodes to either end of the list.
        
    #Adding a new entry into a linked list structure only requires setting
        the new entry’s reference to point to the current top of the stack and
        then pointing the top of the stack to the new entry:
    #HOWEVER,
        Indexing is slower than that of lists, because Python needs
        to walk through each node of the list to get to the third element.
        
'''
