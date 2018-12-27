
# coding: utf-8

# # Introduction to Artificial Intelligence for Non Computing

# ## Practical 2 (weeks 3 - 4)

# ## Search Techniques

# The following links provide additional information about depth first search and breath first search

# - Depth first search:   link：https://pan.baidu.com/s/1bkLHKKbSBNpfFuKwDyURqw  password：oy76
# - Breath first search:  link：https://pan.baidu.com/s/176g5q0W3rGbSAM5tZMraeg   password：7mdh

# #### Theory Questions 

# 1\. What is an algorithm? A sequence of steps such as a recipe or a movie script.
# 
# As a movie viewer, please write an algorithm for a process to "see a movie". Include details of the following for example (add additional information yourself):
# 	- The start conditions 
# 	-- I want to watch a movie
# 	- Roles (people/actors involved) 
#     --watcher, ticket seller etc 
#     -Equipment required ("props")
#     --seats, ticket etc
#     - The scenes 
#     -- scene 1 - buy ticket 
#     -- ??? what happens next
#     -- scene 3, scene 3 ...
#     - Results/outcomes
#     -- ?
# 

# 1. "a.want to watch a movie""b.have enough money to buy ticket"
# if condition a&b satisfied, go next
# 2."input the roles people/actors you want to watch"
# go next
# 3.if have,set seat and ticket
# go next
# 4.buy tickets
# go next
# 5.outcome 
# 
# ***

# 2\. A farmer with his wolf, duck and bag of corn come to the east side of a river they wish to cross. There is a boat at the rivers edge, but of course only the farmer can row. The boat can only hold two things (including the rower) at any one time. If the wolf is ever left alone with the duck, the wolf will eat it. Similarly if the duck is ever left alone with the corn, the duck will eat it. How can the farmer get across the river so that all four arrive safely on the other side? 

# _your answer here..._ 
# (1) Farmer takes duck to left bank
# (2) Farmer returns alone to right bank
# (3) Farmer takes wolf to left bank
# (4) Farmer returns with duck
# (5) Farmer takes corn to left bank
# (6) Farmer returns alone
# (7) Farmer takes duck to left bank
# (8) Success
# ***

#  

# 3\.Explain why we determine our problem goals before we write the problem formulation (including the model and deciding what algorithm or techniques to use - for example search, or other method).
# 
# See Chapter3.1 (Russel & Norvig)

# _your answer here..._ 
# In goal formulation, we decide which aspects of the world we are interested in, and which can be ignored or abstracted away. Then in problem formulation we decide how to manipulate the important aspects (and ignore the others). If we did problem formulation first we would not know what to include and what to leave out. That said, it can happen that there is a cycle of iterations between goal formulation, problem formulation, and problem solving until one arrives at a sufficiently useful and efficient solution.
# ****

# 4\. This question requires you to perform BFS and DFS on paper.
# 
# <img src="img/p1.png" width="180" height="180" >
# 
# 1. Simulate (on pencil-and-paper) breadth-first search starting from node A when the goal node is K.
# 2. Simulate (on pencil-and-paper) depth first search starting from node A when the goal node is I.
# 

# 1. _your answer here..._ 
# 2. _your answer here..._ 
# 
# ***1\.BFS
#     A:[B]
#     B:[C,D]
#     C:[D,E,F]
#     D:[E,F,H,G]
#     E:[F,H,G]
#     F:[H,G]
#     H:[G,K,I]
#     G:[K,I]
#     K=goal
# - 2\. DFS
#     A:[B]
#     B:[C,D]
#     C:[E,G,D]
#     E:[F,D]
#     F:[D]
#     D:[H,G]
#     H:[I,K,G]
#     I=goal

# 5\.Consider a state space where the start state is number 1 and each state  k has two successors: numbers 2k and 2k + 1.
# - a. Draw the portion of the state space for states 1 to 15.
# - b. Suppose the goal state is 11. List the order in which nodes will be visited for breadthfirst
# search, depth-limited search with limit 3, and iterative deepening search.
# - c. How well would bidirectional search work on this problem? What is the branching
# factor in each direction of the bidirectional search?
# - d. Does the answer to (c) suggest a reformulation of the problem that would allow you to
# solve the problem of getting from state 1 to a given goal state with almost no search?
# - e. Call the action going from k to 2k Left, and the action going to 2k + 1 Right. Can you
# find an algorithm that outputs the solution to this problem without any search at all?
# 
# See textbook Chapter3.15

#    a.               1
#            2               3
#         4     5        6       7
#       8 9    10 11   12 13    14 15
#    b.1 2 3 4 5 6 7 8 9 10 11
#      1 2 4 8 9 5 10 11
#      1;   1 2 3;   1 2 4 5 3 6 7;  1 2 4 8 9 5 10 11
#    c.Bidirectional search is very useful, because the only successor of n in the reverse direction is ⌊(n/2)⌋. This helps focus the search. The branching factor is 2 in the forward  direction; 1 in the reverse direction.
#    d.yes
#    e. The solution can be read off the binary numeral for the goal number. Write the goal number in binary. Since we can only reach positive integers, this binary expansion beings with a 1.  From  most- to least- significant bit, skipping the initial 1, go Left to the node 2n if this bit is 0 and go Right to node 2n + 1 if it is 1.
#       
#   

# ### Programming Excercises

# 1\.Write a program to solve a classic ancient Chinese puzzle:  
#  We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? 

# In[1]:


##Hint:Use for loop to iterate all possible
## write your answer here!
def solve(heads,legs): 
    ns='No solutions!' 
    for i in range(heads+1): 
        j=numheads-i 
        if 2*i+4*j==legs: 
            return i,j 
    return ns,ns 
heads=35 
legs=94 
solutions=solve(heads,legs) 
print (solutions) 


# 2\. _Social networking_ Please look at the graph below of social relationships. You have a mango farm, you need to find a mango buyer and sell him your mango that you have grown (just a small farm). To this end, our principle is to use our social network of friends separated by one degree, and then second degree friends (friends of friends), third degree friends (friends of friends of friends).
# 
# Use the depth first algorithm to search your network until you find a mango seller. 
# 
# We make an assumption that if the person's name ends with m, then it means the person must be the mango seller!
# 
# 
# <img src="img/p3.png" width="500" height="400" >

# In[4]:


## write your answer here!
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# Suppose we judge this way, if the person's name ends with m, then it is the mango seller.
def person_is_seller(name):
    return name[-1] == "m"

def main():
    # Create a queue
    search_queue = deque()
    # Add your neighbor to this search queue.
    search_queue += graph["you"]

    # This data is used to record people who have checked.
    searched = []

    # As long as the queue is not empty, the first person will be taken out.
    while search_queue:
        person = search_queue.popleft()
        # It is only when the person has not checked.
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Mark this person as checked.
                searched.append(person)
    return False
if __name__ == '__main__':
    main()


# 3\. Depth First traverse：Use depth first traversal to traverse all the DLL files on the C disk and output the file names.
# 
# Update your code to search for a particular filename.
# 
# What protocol did you use to select the next node to expand on the fringe?

# In[ ]:


## write your answer here!
import os
import fnmatch
from collections import deque
def get(path):

        queue = deque()
        queue.append(path)
        while len(queue)>0:
            temp = queue.popleft()
            try:
                list = os.listdir(temp)
            except WindowsError as e:
                pass
            for filename in list:
                next = os.path.join(temp,filename)
                if os.path.isfile(next):
                    if fnmatch.fnmatch(filename,'*.dll'):
                        print (filename)
                elif os.path.isdir(next):
                    queue.append(next)

get('C:\\')


# 4\.
# Breadth First traverse：Use breadth traversal to traverse all the DLL files on the C disk and output the filename.
# 
# Update your code to search for a particular filename.

# In[ ]:


## write your answer here!
import  os
list = []
path = "C:\\"
count = 0
for name in os.listdir(path):
    list.append(os.path.join(path,name))
while len(list)!=0:
    last = list.pop()
    if os.path.isfile(last):
        str = last.split("\\")[-1]
        if str.split(".")[-1] == "dll":
            str2 = str.split(".")[0]
            print(str2)
    else:
        try:
            for name in os.listdir(last):
                list.append(os.path.join(last,name))
        except:
            count+=1
print(count)


# 5\. Uniform cost search

# Consider a state space where the start state is 2 and each state k has three successors: numbers 2k, 2k+1, 2k+2. The cost from state k to each respective child is k, ground(k/2), k+2.
# 
# can you implement a uniform-cost-search algorithm with python. The goal state is number 85.
# 

# In[ ]:


import math
goal = 85
state = [-1] * (goal + 1)
state[2] = 0
for k in range(2 , int(goal/2) + 1):
    if state[k] < 0: continue
    for pos, cost in [
        (k*2, k),
        (k*2 + 1, math.floor(k/2)),
        (k*2+2, k+2)]:
        if pos > goal: continue
        if state[pos] == -1 or state[pos] > state[k] + cost:
          state[pos] = state[k] + cost
      # Possibly store k somewhere to build the solution.
print (state[goal])


# 6\.a* question

# A cute cat stays in the A position, he is hungry. But the food is placed in the B position. Can you help him to find the food? 
# Hint:  The problem isn't easy. It's essential for you to understand the A* algorithm before you solve this problem. Then, you can use some thought of Node in java, when you are in code.
# 
# <img src="img/p4.png" width="500" height="400" >
# 

# In[ ]:


## write your answer here!
import math

AB_MAP = [[1]*20 for i in range(20)]
POS_UP = 1
POS_LEFT = 2
POS_DOWN = 3
POS_RIGHT = 4


def mod_map(m_map, pos_x, pos_y, val):
    m_map[pos_x][pos_y] = val

def print_map(m_map):
    rows = len(m_map)
    for i in range(0, rows - 1):
        cols = len(m_map[i])
        for j in range(0, cols - 1):
            print str(m_map[i][j]) + "\t",
            j = j + 1
        print
        i = i + 1


class Node(object):
    def __init__(self, x, y, h_n=0, g_n=0):
        self.pos_x = x
        self.pos_y = y
        self.parent = None
        self.h_n = h_n
        self.g_n = g_n
        self.f_n = self.h_n + self.g_n

    def update_h_n(self, target):
        self.h_n = int(math.sqrt((target.pos_x - self.pos_x)**2 + (target.pos_y - self.pos_y)**2))
        return self.h_n

    def update_g_n(self, source):
        self.g_n = int(math.sqrt((source.pos_x - self.pos_x)**2 + (source.pos_y - self.pos_y)**2))
        return self.g_n

    def update_f_n(self, source, target):
        self.f_n = self.update_g_n(source) + self.update_h_n(target)
        return self.f_n

    def update_parent(self, par):

        self.parent = par

    def get_adj_node(self, flag, source, target):
        if flag == POS_UP:
            cur_node = Node(self.pos_x, self.pos_y - 1)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_LEFT:
            cur_node = Node(self.pos_x - 1, self.pos_y)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_DOWN:
            cur_node = Node(self.pos_x, self.pos_y + 1)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_RIGHT:
            cur_node = Node(self.pos_x + 1, self.pos_y)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        else:
            return None


def node_addible(node, open_list, close_list):
    index = str(node.pos_x) + '_' + str(node.pos_y)
    if index not in open_list and index not in close_list:
        open_list[index] = node


def reach_end(node, target):
    if node and target and node.pos_x == target.pos_x and node.pos_y == target.pos_y:
        return True
    else:
        return False

# 该方法用于打印路径
def handle_reach_end(node, mmap, modval, print_path=False):
    if node and mmap:
        while node:
            if print_path:
                print "x: %s, y: %s" % (node.pos_x, node.pos_y)
            mod_map(mmap, node.pos_x, node.pos_y, modval)
            node = node.parent

def main(source, target, open_list, close_list, mmap):
    open_list[str(source.pos_x) + '_' + str(source.pos_y)] = source
    while open_list:
        tmp_dict = sorted(open_list.iteritems(), key=lambda d: d[1].f_n)
        first_key = tmp_dict[0][0]
        first_node = open_list[first_key]
        del open_list[first_key]

        up_node = first_node.get_adj_node(POS_UP, source, target)
        if reach_end(up_node, target):
            handle_reach_end(up_node, mmap, 2)
            break

        left_node = first_node.get_adj_node(POS_LEFT, source, target)
        if reach_end(left_node, target):
            handle_reach_end(left_node, mmap, 2)
            break

        down_node = first_node.get_adj_node(POS_DOWN, source, target)
        if reach_end(down_node, target):
            handle_reach_end(down_node, mmap, 2)
            break

        right_node = first_node.get_adj_node(POS_RIGHT, source, target)
        if reach_end(right_node, target):
            handle_reach_end(right_node, mmap, 2)
            break

        if first_key not in close_list:
            close_list[first_key] = first_node

        node_addible(up_node, open_list, close_list)
        node_addible(down_node, open_list, close_list)
        node_addible(left_node, open_list, close_list)
        node_addible(right_node, open_list, close_list)


if __name__ == '__main__':
    print "** before **"
    print_map(AB_MAP)
    OPEN_LIST = {}
    CLOSE_LIST = {}

    SOURCE = Node(3, 4)
    TARGET = Node(13, 9)
    main(SOURCE, TARGET, OPEN_LIST, CLOSE_LIST, AB_MAP)

    print "** after **"
    mod_map(AB_MAP, SOURCE.pos_x, SOURCE.pos_y, 0)
    mod_map(AB_MAP, TARGET.pos_x, TARGET.pos_y, 0)
    print_map(AB_MAP)

