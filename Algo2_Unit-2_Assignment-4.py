# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 00:50:57 2018

@author: Tawanda Vera
"""


##############################################################################
# Problem 2: Disjoint Sets
# a) Use Tree representation of disjoint set ADT to do the following operations:
# for i=1 to i=8 Make_set(i) union(5,6) union(7,8) union(5,7)
# b) Give a non-recursive implementation of FIND-SET with path compression.
##############################################################################
class DisjointSet(object):

    
    def __init__(self):

        self.sets = {}
    
    #------------------------------------------------------------
    # creates a new set whose only member (and thus representative) is x.
    # Since the sets are disjoint, we require that x not already be in some 
    # other set.
    
    def make_set(self, x):
    
        """post: adds a set to the group of sets for the single element x
        raises KeyError if already a set containing x"""
        
        # check if set for this item already exists
        if x in self.sets:
            raise KeyError('%s already in DisjointSet' % str(x))
        # map element to the set/list containing it
        self.sets[x] = [x]

    #------------------------------------------------------------
    # b) Give a non-recursive implementation of FIND-SET with path compression.
    def find(self, x):
    
        '''post: returns set/list containing x
        raises KeyError if there is not a set containing x

        for efficiency use the "is" operator to determine if two
        elements are in the same set by making two calls to find
        (e.g., if dj.find(x) is dj.find(y):)'''
        
        return self.sets[x]

    #------------------------------------------------------------
    # Union unites the dynamic sets that contain x and y, say Sx and Sy, into
    # a new set that is the union of these two sets. Since we require the sets 
    # in the collection to be disjoint, we “destroy” sets Sx and Sy, removing 
    # them from the collection S.
    
    def union(self, x, y):

        '''post: the sets containing x and y are merged/joined
        raises KeyError if the two sets are already the same'''
        
        if self.sets[x] is self.sets[y]:
            raise KeyError('%s and %s are in the same set' % (
            str(x), str(y)))

        # determine smaller list so we are adding fewer items to the
        # existing list
        if len(self.sets[x]) > len(self.sets[y]):
            # save list of elements in smaller set
            temp = self.sets[y]
            # for each element in smaller set, map it to the larger list
            for k in self.sets[y]:
                self.sets[k] = self.sets[x]
            # add all elements in smaller set/list to larger set/list
            self.sets[x].extend(temp)
        else:
            # save elements in smaller set
            temp = self.sets[x]
            # for each element in smaller set, map it to the larger list
            for k in self.sets[x]:
                self.sets[k] = self.sets[y]
            # add all elements in smaller set/list to larger set/list
            self.sets[y].extend(temp)


# Implementation
#a) Use Tree representation of disjoint set ADT to do the following operations:
# for i=1 to i=8 Make_set(i) union(5,6) union(7,8) union(5,7)

s = DisjointSet()
for i in range(1, 9):
    s.make_set(i)

# Sets before the union    
print(s.sets)

# Union of sets
s.union(5, 6)
s.union(7, 8)
s.union(5, 7)

#Final sets
print(s.sets)

#To check the Find-Set method
s.find(5) is s.find(8)  # This is true, since the union function combined them

print(s.find(5))

###############################################################################

"""Disjoint-set data structures are one of the most useful data structures for
 its simplicity and amazing running time. One of the most well-known 
 applications is its use in Kruskal’s Minimal Spanning Tree algorithm, 
 which has a lot of applications in many ways. 
 Using a graph with random weights, Kruskal’s algorithm generates nice 
 random trees, and in particular, this can be used to easily generate mazes 
 of all kinds.
 """
 