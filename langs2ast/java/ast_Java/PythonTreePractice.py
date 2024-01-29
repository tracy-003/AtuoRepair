import sys

from anytree import Node, RenderTree, AnyNode
from anytree import SymlinkNode, Node, RenderTree
root = Node("root")
s1 = Node("sub1", parent=root)
l0 = Node("l0", parent=s1)
print(RenderTree(root))

#[
    # ['void'
    # , 'main'
    # , [[String[], args]]
    # , [
        # [Assign,s, "Test"]]
        # ,[[Print, s]]
        # ,[[Println,"hello"]]
    # ] 
    # ['void'
        # ,'printS'
        # , [
            # [[String, s],[int, i]]
        # ]
        # , [
            # [Println,s]
        # ]
    # ]
# ]
