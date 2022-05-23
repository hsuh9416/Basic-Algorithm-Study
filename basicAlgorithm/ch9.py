"""
    Ch9 Tree(트리)
    * Skipped too simple examples

    * important notes
    1) Main concepts of tree data structure
        a> root: The head node of tree data structure; Only one exists in tree data structure
        b> leaf: The bottom nodes of tree data structure; Terminal node or External node; Can exist multiple
        c> non-terminal node: The nodes which are not root and leaf; Internal node
        d> child: The direct-descendant node of base node; Each node can have multiple child nodes
        e> parent: The direct-ascendant node of base node; Each node can have only one parent node
        f> sibling: The nodes which having the same parent node with base node
        g> ancestor: All ascendant nodes of base node
        h> descendant: All descendant nodes of base node
        i> level: Representing how many steps to reach to root node
            ex> level or root: 0, level of child of root: 1, etc.
        j> degree: The number of each node's children
        k> height: The max level of tree data structure; The level representing from the leaf to the root
        l> subtree: Having a particular internal node as head node, forming tree structure of itself
        m> None tree: The tree structure has no node; null tree
        n> order tree: Tree structure having order among sibling nodes cf. unordered tree
    2) Methods to scan tree data structure
        a> breadth-first search
            => Also called as horizontal search
            => Scan the data horizontally first, then go down to the child node (until reach to the bottom)
            => Horizontal scan will conducted from left to right
        b> depth-first search:
            => Also called as vertical search
            => Scan from top to bottom first, then return to the parent node to find un-scanned node
            => 3 type of detailed scanning included: preorder, inorder, postorder
                - preorder: base node visit -> left child visit -> right child visit
                - inorder: left child -> base node visit -> right child visit
                - postorder: left child -> right child -> base node visit
            => Each node can be visited maximum 3 times(by each preorder, inorder, postorder)


"""

if __name__ == '__main__':
    print('To be continued')