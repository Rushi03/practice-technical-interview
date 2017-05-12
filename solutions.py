'''
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return
a boolean True or False.
'''


def question1(s, t):
    # Check if there is a string or substring
    if s is None or t is None:
        return None

    # Create a list for the letters in the string
    string = list(s)
    substring = list(t)

    # Sort the strings in alphabetical order
    string.sort()
    substring.sort()

    # Count the number equivalent letters
    count = 0
    for i in range(len(t)):
        if substring[i] in string:
            count += 1

    # Check if count is same size as substring
    if count == len(substring):
        return True
    else:
        return False


print question1('udacity', 'ad')
# True
print question1('infinite', 'hi')
# False
print question1('beyond', 'on')
# True
print question1(' ', 'lie')
# False
print question1('beautiful', None)
# None
###############################################################################
'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your
function definition should look like question2(a), and return a string.
'''


def question2(a):
    '''
    # Check if a word is a palindrome
    if a == a[::-1]:
        return a
    else:
        print "Not a palindrome!"

    a = 'madam'
    '''

    # Check for string
    if a is None:
        return None

    # Split the string by the spaces
    words = a.split(' ')
    # How I will join the string and check it's palindrome
    s = ''
    # Inital index value to compare substrings
    index = 0

    # Check if the string is a palindrome
    if s.join(words) == s.join(words)[::-1]:
        # Return string if string is a palindrome
        return a
    else:
        for i in range(len(words)):
            # Check if substring is a palindrome
            if words[i] == words[i][::-1]:
                # Check if palindrome substring larger than previous
                if len(words[i]) >= len(words[index]):
                    index = i
        # Return largest substring palindrome
        return words[index]


print question2('never odd or even')
# never odd or even
print question2('madam likes bob')
# madam
print question2('rotor pop 1621261')
# 1621261
print question2(None)
# None
print question2(' ')
# ' '
##############################################################################
'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be
question3(G).
'''


def question3(G):
    vertices = G
    parent = {}
    minimum_spanning_tree = {}
    edge = []

    for vertex in vertices:
        parent[vertex] = G[vertex]
        for node in parent[vertex]:
            if node not in edge:
                edge.append(node)
                edge.sort()
    for edges in edge:
        start, finish, distance = edges
        weight = (finish, distance)
        if start not in minimum_spanning_tree:
            minimum_spanning_tree[start] = []
            if weight not in minimum_spanning_tree[start]:
                minimum_spanning_tree[start].append(weight)
        else:
            minimum_spanning_tree[start].append(weight)

    return minimum_spanning_tree


print question3({'A': [('A', 'B', 2)], 'B': [('B', 'A', 2), ('B', 'C', 5)],
                 'C': [('C', 'B', 5)]})
# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
print question3({'A': [('A', 'B', 2), ('A', 'D', 7)], 'B': [('B', 'A', 2),
                ('B', 'C', 5)], 'C': [('C', 'B', 5)], 'D': [('D', 'A', 7)]})
# {'A': [('B', 2), ('D', 7)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)],
#  'D': [('A', 7)]}
print question3({'F': [('F', 'B', 1)], 'B': [('B', 'F', 1), ('B', 'C', 5)],
                 'C': [('C', 'B', 5), ('C', 'H', 4)], 'H': [('H', 'C', 4)]})
# {'H': [('C', 4)], 'C': [('B', 5), ('H', 4)], 'B': [('C', 5), ('F', 1)],
#  'F': [('B', 1)]}
###############################################################################
'''
Question 4
Find the least common ancestor between two nodes on a binary search tree. The
least common ancestor is the farthest node from the root that is an ancestor of
both nodes. For example, the root is a common ancestor of all nodes on the
tree, but if both nodes are descendents of the root's left child, then that
left child might be the lowest common ancestor. You can assume that both nodes
are in the tree, and the tree itself adheres to all BST properties. The
function definition should look like question4(T, r, n1, n2), where T is the
tree represented as a matrix, where the index of the list is equal to the
integer stored in that node and a 1 represents a child node, r is a
non-negative integer representing the root, and n1 and n2 are non-negative
integers representing the two nodes in no particular order. For example, one
test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''


# Parent node to check if node has a child
def parent_node(T, child):
    for i in range(len(T)):
        if T[i][child] == 1:
            return i


def question4(T, r, n1, n2):
    # Check for root, n1, and n2:
    if r is None or n1 is None or n2 is None:
        return None

    # Common ancestor
    common = []

    # Check if n1 equals the root
    while n1 != r:
        n1 = parent_node(T, n1)
        common.append(n1)

    # If there are common nodes for n1 and root
    # check with n2 to find least common ancestor
    if len(common) != 0:
        while n2 != r:
            n2 = parent_node(T, n2)
            if n2 in common:
                return n2
    else:
        return


print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# 3
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                2,
                1,
                4)
# 2
print question4([[0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1]],
                1,
                0,
                4)
# 1
print question4([[0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1]],
                None,
                0,
                4)
# None
print question4([[0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1]],
                1,
                None,
                4)
# None
###############################################################################
'''
Question 5
Find the element in a singly linked list that's m elements from the end. For
example, if a linked list has 5 elements, the 3rd element from the end is the
3rd element. The function definition should look like question5(ll, m), where
ll is the first node of a linked list and m is the "mth number from the end".
You should copy/paste the Node class below to use as a representation of a node
in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    x = ll
    y = ll
    counter = 0

    # Check ll and m
    if ll is None or m is None:
        return None

    # Count length of linked list
    while x is not None:
        x = x.next
        counter += 1

    # Check if the counter is greater than m
    if counter < m:
        return

    # Find the mth from last number
    for i in range(counter - m):
        y = y.next
    # Return the mth from last number
    return y.data


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)
ll.next.next.next.next.next = Node(6)
ll.next.next.next.next.next.next = Node(7)
ll.next.next.next.next.next.next.next = Node(8)
ll.next.next.next.next.next.next.next.next = Node(12345)


print question5(ll, 5)
# 4
print question5(ll, 3)
# 6
print question5(ll, 1)
# 12345
print question5(ll, None)
