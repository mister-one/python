Trees


Trees are an essential data structure for storing hierarchical data with a directed flow.
root node is at the very top and this is also a parent.
child or children nodes
When a node has no children, we refer to it as a leaf node.


Binary Search Tree

A binary tree is a type of tree where each parent can have no more than two children, known as the left child and right child.

review:

parent: A node which references other nodes.
child: Nodes referenced by other nodes.
sibling: Nodes which have the same parent.
leaf: Nodes which have no children.
level: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.



TreeNodes:

have a value
have a reference to zero or more other TreeNodes
can add a node as a child
can remove a child
can traverse (or travel through) connected nodes





class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # HELPER METHOD TO PRINT TREE!
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    self.children.append(child_node) 

### TEST CODE TO PRINT TREE
company = [
  "Monkey Business CEO", 
  "VP of Bananas", 
  "VP of Lazing Around", 
  "Associate Chimp", 
  "Chief Bonobo", "Produce Manager", "Tire Swing R & D"]
root = TreeNode(company.pop(0))
for count in range(2):
  child = TreeNode(company.pop(0))
  root.add_child(child)

root.children[0].add_child(TreeNode(company.pop(0)))
root.children[0].add_child(TreeNode(company.pop(0)))
root.children[1].add_child(TreeNode(company.pop(0)))
root.children[1].add_child(TreeNode(company.pop(0)))
print("MONKEY BUSINESS, LLC.")
print("=====================")
print(root)



>>>

MONKEY BUSINESS, LLC.
=====================
'Monkey Business CEO'
--->'VP of Bananas'
--->--->'Associate Chimp'
--->--->'Chief Bonobo'
--->'VP of Lazing Around'
--->--->'Produce Manager'
--->--->'Tire Swing R & D'






class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children







Heaps


We will focus on min-heaps, but the concepts for a max-heap are nearly identical.

Think of the min-heap as a binary tree with two qualities:

The root is the minimum value of the dataset.
Every childs value is greater than its parent.
These two properties are the defining characteristics of the min-heap. By maintaining these two properties, we can efficiently retrieve and update the minimum value.

Removing an Element: Heapify Down
Adding an Element: Heapify Up # the element is adde at the bottom 

left child: (index * 2) + 1
right child: (index * 2) + 2
parent: (index - 1) / 2 — not used on the root!



class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  

  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print("Left child is smaller")
        return self.left_child_idx(idx)
      else:
        print("Right child is smaller")
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    idx = self.count
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        tmp = self.heap_list[self.parent_idx(idx)]
        print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")
      
  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      smaller_child_idx = self.get_smaller_child_idx(idx)
      if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
        tmp = self.heap_list[smaller_child_idx]
        print("swapping {0} with {1}".format(self.heap_list[idx], tmp))
        self.heap_list[smaller_child_idx] = self.heap_list[idx]
        self.heap_list[idx] = tmp

      idx = smaller_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")    





# import random number generator
from random import randrange
# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  min_heap.add(el)

# remove minimum until min_heap is empty
while min_heap.count != 0:
  min_heap.retrieve_min()






Adding: 1 to [None]
HEAP RESTORED! [None, 1]

Adding: 1 to [None, 1]
HEAP RESTORED! [None, 1, 1]

Adding: 44 to [None, 1, 1]
HEAP RESTORED! [None, 1, 1, 44]

Adding: 13 to [None, 1, 1, 44]
HEAP RESTORED! [None, 1, 1, 44, 13]

Adding: 9 to [None, 1, 1, 44, 13]
HEAP RESTORED! [None, 1, 1, 44, 13, 9]

Adding: 30 to [None, 1, 1, 44, 13, 9]
swapping 44 with 30
HEAP RESTORED! [None, 1, 1, 30, 13, 9, 44]

Removing: 1 from [None, 1, 1, 30, 13, 9, 44]
Last element moved to first: [None, 44, 1, 30, 13, 9]
Left child is smaller
swapping 44 with 1
Right child is smaller
swapping 44 with 9
HEAP RESTORED! [None, 1, 9, 30, 13, 44]

Removing: 1 from [None, 1, 9, 30, 13, 44]
Last element moved to first: [None, 44, 9, 30, 13]
Left child is smaller
swapping 44 with 9
There is only a left child
swapping 44 with 13
HEAP RESTORED! [None, 9, 13, 30, 44]

Removing: 9 from [None, 9, 13, 30, 44]
Last element moved to first: [None, 44, 13, 30]
Left child is smaller
swapping 44 with 13
HEAP RESTORED! [None, 13, 44, 30]

Removing: 13 from [None, 13, 44, 30]
Last element moved to first: [None, 30, 44]
There is only a left child
HEAP RESTORED! [None, 30, 44]

Removing: 30 from [None, 30, 44]
Last element moved to first: [None, 44]
HEAP RESTORED! [None, 44]

Removing: 44 from [None, 44]
Last element moved to first: [None]
HEAP RESTORED! [None]










