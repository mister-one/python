QUEUES


A queue is a data structure which contains an ordered set of data.

three methods for interaction:

Enqueue - adds data to the "back" or end of the queue
Dequeue - provides and removes data from the "front" or beginning of the queue
Peek - reveals data from the "front" of the queue without removing it


Queues can be implemented using a linked list as the underlying data structure. The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.

queue overflow. 
queue underflow. #If you attempt to dequeue data from an empty queue



from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
      
  # Add your dequeue method below:    
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
  
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("some guy with a mustache")
q.dequeue()



>>> Adding some guy with a mustache to the queue!
>>> Removing some guy with a mustache from the queue! 



n Python by creating a Queue class that:

follows FIFO protocol with enqueue(), dequeue(), and peek() methods
gives you the option of creating bounded queues with a max_size
prevents queue "overflow" and "underflow" by keeping track of size





from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
         
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")
  
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #





Creating a deli line with up to 10 orders...
------------
Adding orders to our deli line...
------------
Adding egg and cheese on a roll to the queue!
Adding bacon, egg, and cheese on a roll to the queue!
Adding toasted sesame bagel with butter and jelly to the queue!
Adding toasted roll with butter to the queue!
Adding bacon, egg, and cheese on a plain bagel to the queue!
Adding two fried eggs with home fries and ketchup to the queue!
Adding egg and cheese on a roll with jalapeos to the queue!
Adding plain bagel with plain cream cheese to the queue!
Adding blueberry muffin toasted with butter to the queue!
Adding bacon, egg, and cheese on a roll to the queue!
Sorry, no more room!
------------
Our first order will be egg and cheese on a roll
------------
Now serving...
------------
egg and cheese on a roll is served!
bacon, egg, and cheese on a roll is served!
toasted sesame bagel with butter and jelly is served!
toasted roll with butter is served!
bacon, egg, and cheese on a plain bagel is served!
two fried eggs with home fries and ketchup is served!
egg and cheese on a roll with jalapeos is served!
plain bagel with plain cream cheese is served!
blueberry muffin toasted with butter is served!
bacon, egg, and cheese on a roll is served!
The queue is totally empty!

















