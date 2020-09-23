Stacks

A stack is a data structure which contains an ordered set of data.

Stacks provide three methods for interaction:

Push - adds data to the "top" of the stack
Pop - returns and removes data from the "top" of the stack
Peek - returns data from the "top" of the stack without removing it


Stacks mimic a physical "stack" of objects. Consider a set of gym weights.
Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. 
Each weight added becomes the new top of the stack.
At any point, the only weight you can remove, or pop, from the stack is the top one. 
You can peek and read the top weight without removing it from the stack.



Stacks Implementation
Stacks can be implemented using a linked list as the underlying data structure because it's more efficient than a list or array.'

Attempting to push data onto an already full stack will result in a stack overflow. 
Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.




from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      
    	item = Node(value)
    	item.set_next_node(self.top_item)
    	self.top_item = item
    # Increment stack size by 1 here:
    	self.size += 1
    else:
      print("All out of space!")
        

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if not self.is_empty():
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0





Stacks Review
Stacks:

Contain data nodes
Support three main operations
Push adds data to the top of the stack
Pop removes and provides data from the top of the stack
Peek reveals data on the top of the stack
Implementations include a linked list or array
Can have a limited size
Pushing data onto a full stack results in a stack overflow
Stacks process data Last In, First Out (LIFO)



from node import Node

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))