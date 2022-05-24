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
    3) Binary tree: Tree data structure that each node can have maximum two child nodes
        => Distinguishes each child node as left child and right child
        => left subtree: Subtree having left child as a root
           right subtree: Subtree having right child as a root
    4) Complete binary tree: Tree data structure that each node having maximum two child nodes
        => Each node should have two child nodes except leaf nodes
        => Maximum number of nodes: 2^(k+1) - 1
        => Height of tree having n number of nodes: log n
    5) Self-balancing search tree
        => Tree data structure designed to limit the height as O(log n)
        => When nodes were inserted in ascending order of key, the depth of tree structure would be deeper
        => So this make tree structure acting like linear list getting lower efficiency when searching
        => By using self-balancing search, enable to limit depth of tree structure
        => Types of self-balancing search tree for binary structure: AVL tree, red-black tree
        => Types of self-balancing search tree for non-binary structure: B tree, 2-3 tree
    6) Properties of binary search tree
        a> Conditions of node in binary search tree
            - Key value of left subtree < Key value of base node
            - Key value of right subtree > Key value of base node
        b> Structure is simpler than other data structure
        c> Enable to get the node values in ascending order by inorder search in depth-first search
        d> Promptly processes searching similar as binary searching
        e> Easy node insertion

"""
from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key  # Key
        self.value = value  # Value
        self.left = left  # Left node pointer
        self.right = right  # Right node pointer


class BinarySearchTree:

    def __init__(self):
        self.root = None  # Root/Head node

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:

        def add_node(node: Node, _key: Any, _value: Any) -> bool:
            if _key == node.key:
                return False
            elif _key < node.key:
                if node.left is None:
                    node.left = Node(_key, _value, None, None)
                else:
                    add_node(node.left, _key, _value)

            else:
                if node.right is None:
                    node.right = Node(_key, _value, None, None)
                else:
                    add_node(node.right, _key, _value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

            if p.left is None:
                if p is self.root:
                    self.root = p.right
                elif is_left_child:
                    parent.left = p.right
                else:
                    parent.right = p.right

            elif p.right is None:
                if p is self.root:
                    self.root = p.left
                elif is_left_child:
                    parent.left = p.left
                else:
                    parent.right = p.left

            else:
                parent = p
                left = p.left
                is_left_child = True
                while left.right is not None:
                    parent = left
                    left = left.right
                    is_left_child = False

                p.key = left.key
                p.value = left.value
                if is_left_child:
                    parent.left = left.left
                else:
                    parent.right = left.left
            return True

    def dump(self, reverse=False) -> None:

        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node: Node):
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key




if __name__ == '__main__':
    print('To be continued')
