#============================== BINARY TREE ==============================

# >>Full binary tree >>
# - each node has either 0 or 2 children
# - no node has a single child

# >>Complete binary tree >>
# - All levels except possibly the last are completly filled
# - Nodes in the last level are filled from left to right

# >>Perfect Binary >>
# - All internal nodes have exactly two nodes
# - all leaf node at same level

#-------------------------------------------------------------------
#                     N1

#              N2           N3

#        N4       N5   N6       N7

#   N9       N10

# >Postorder - N9 > N10 > N4 > N5 > N2 > N6 > N7 > N3 >N1
# leaf Subtree >> Root node >> Right Subtree 

# level order traversal
# level1:   N1
# level2:   N2,N3
# level3:   N4,N5,N6,N7
# level4:   N9,N10
# Final- N1>N2>N3>N4>N5>N6>N7>N9>N10
#-------------------------------------------------------------------


# Why Binary Search Tree?
# It perform faster than binary tree when inserting and deleting node.

#-----------------------------------------------------------------------------------------------------------------------

#Q1
#                       70

#              50               90

#        30       60       80       100

#   20       40               95

#10

#---------------------------------------------------
<<<<<<< HEAD
# class BSTNode:
#     def __init__(self,data):
#         self.data       = data
#         self.leftchild  = None
#         self.rightchild = None

# def insertNode(rootnode,nodevalue):
#     if rootnode.data == None:                       #checks for empty rootnode
#         rootnode.data = nodevalue
#     elif nodevalue <= rootnode.data:                #checks for nodevalue is smaller than rootnode
#         if rootnode.leftchild is None:
#             rootnode.leftchild = BSTNode(nodevalue)
#     else:                                           #checks for nodevalue is greater than rootnode
#         if rootnode.rightchild is None:
#             rootnode.rightchild = BSTNode(nodevalue)

# newBST = BSTNode(data)
# insertNode(newBST,70)
# insertNode(newBST,50)
# insertNode(newBST,90)
=======
class BSTNode:
    def __init__(self,data):
        self.data       = data
        self.leftchild  = None
        self.rightchild = None

def insertNode(rootnode,nodevalue):
    if rootnode.data == None:                       #checks for empty rootnode
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:                #checks for nodevalue is smaller than rootnode
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(nodevalue)
    else:                                           #checks for nodevalue is greater than rootnode
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(nodevalue)

newBST = BSTNode(data)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
>>>>>>> 314e8056e6486458c8a7546f6a20a07fdc911ea5

