Nodes Introduction

Nodes are the fundamental building block of many computer science data structures. 
They form the basis for linked lists, stacks, queues, trees, and more.

The data contained within a node can be a variety of types, depending on the language you are using.
It can be an integer (the number 5), but it could be a string ("five"), decimal (5.1), an array ([5,3,4]) or nothing (null).



The link or links within the node are sometimes referred to as pointers. This is because they "point" to another node.



Node Linking
Often, due to the data structure, nodes may only be linked to from a single other node.
This makes it very important to consider how you implement modifying or removing nodes from a data structure.

If you inadvertently remove the single link to a node, that node's data and any linked nodes could be "lost" to your application.' 
When this happens to a node, it is considered an orphaned node.



Nodes:

Contain data, which can be a variety of data types
Contain links to other nodes. If a node has no links, or they are all null, you have reached the end of the path you were following.
Can be orphaned if there are no existing links to them





# Create the Node class below:
class Node:
  def __init__(self,value, link_node = None):
    self.value = value
    self.link_node = link_node
    





class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:

yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node ("enjoys spending time in movie lots")


yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)


>>> enjoys spending time in movie lots
>>> has a penchant for hoarding snacks




Consider the following nodes and links: a -> n -> t. If you want to remove node n, but preserve node t, what are the steps you would take?
Change the link on a to point to t using a.set_link_node(t)















Linked List Introduction 📌✅

Linked lists are one of the basic data structures used in computer science. 
They have many direct applications and serve as the foundation for more complex data structures.


The list is comprised of a series of nodes as shown in the diagram. 
The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. 
The list is terminated when a node's link is null. This is called the tail node.'



Linked List Review
Let's take a minute to review what we've covered about linked lists in this lesson.

Linked Lists:

Are comprised of nodes
The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
Can be unidirectional or bidirectional
Are a basic data structure, and form the basis for many other data structures
Have a single head node, which serves as the first node in the list
Require some maintenance in order to add or remove nodes
The methods we used are an example and depend on the exact use case and/or programming language being used



# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node
    
my_node = Node(44)







class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node






class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      string_list += str(current_node.value) + "."
      current_node = current_node.next_node
    return string_list
  
a = Node(5)
b = Node(70, a)
c = Node(5675, b)
d = Node(90, c)
ll = LinkedList(d)

print(ll.stringify_list())


>>> 90.5675.70.5.





