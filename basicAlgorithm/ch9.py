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
from enum import Enum
from ch3 import select_menu


Tree_Menu = Enum('Tree_Menu', ['INSERT', 'DELETE', 'SEARCH', 'SHOW', 'SHOW_REVERSE', 'KEY_RANGE', 'TERMINATE'])


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
            if _key == node.key:  # If key number already exists
                return False
            elif _key < node.key:  # No key assigned yet at left node
                if node.left is None:
                    node.left = Node(_key, _value, None, None)
                    return True  # Return True after data assigned
                else:
                    add_node(node.left, _key, _value)  # Go down to find out empty node

            else:  # No Key assigned yet at right node
                if node.right is None:
                    node.right = Node(_key, _value, None, None)
                    return True  # Return True after data assigned
                else:
                    add_node(node.right, _key, _value)  # Go down to find out empty node
            return False  # Return False if nothing done

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False  # Nothing to remove

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:  # Point left subtree from the parent node
                    is_left_child = True
                    p = p.left
                else:  # Point right subtree from the parent node
                    is_left_child = False
                    p = p.right

        if p.left is None:  # No left child/No child
            if p is self.root:
                self.root = p.right  # Remove link of p by reconnecting as p's child/None
            elif is_left_child:
                parent.left = p.right  # Remove link of p by reconnecting as p's child/None
            else:
                parent.right = p.right  # Remove link of p by reconnecting as p's child/None

        elif p.right is None:  # No right child
            if p is self.root:
                self.root = p.left  # Remove link of p by reconnecting as p's child/None
            elif is_left_child:
                parent.left = p.left  # Remove link of p by reconnecting as p's child/None
            else:
                parent.right = p.left  # Remove link of p by reconnecting as p's child/None

        else:  # Having two child
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:  # Find the biggest child node from left subtree
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left  # Delete
            else:
                parent.right = left.left  # Delete
        return True

    def dump(self, reverse=False) -> None:

        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)  # Print left subtree ascendant order
                print(f'{node.key} {node.value}')
                print_subtree(node.right)  # Print right subtree ascendant order

        def print_subtree_rev(node: Node):
            if node is not None:
                print_subtree_rev(node.right)  # Print right subtree descendant order
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)  # Print left subtree descendant order

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:  # Go down to the left side to find minimum key number
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:   # Go down to the right side to find maximum key number
            p = p.right
        return p.key


def key_insertion(purpose: str) -> int:
    key = None
    while key is None:
        try:
            temp = int(input(f'Enter key numbers to be {purpose}: ').strip())
            if temp < 0:
                raise TypeError
            key = temp
        except ValueError:
            print('Enter integer number for key only!')
        except TypeError:
            print(f'Enter the key number bigger then 0!')
    return key


def run_menu(bst: BinarySearchTree) -> None:
    while True:
        menu = select_menu(Tree_Menu)

        if menu == Tree_Menu.INSERT:  # Add node
            key = key_insertion('created')
            value = input('Enter the value of node to add: ')
            if not bst.add(key, value):
                print('Fail to add the data!')

        elif menu == Tree_Menu.DELETE:  # Delete node by key number
            key = key_insertion('deleted')
            bst.remove(key)

        elif menu == Tree_Menu.SEARCH:  # Search by key number
            key = key_insertion('searched')
            result = bst.search(key)
            if result is not None:
                print(f"The value of key '{key}': {result}")
            else:
                print(f"No value exists for key '{key}!")

        elif menu == Tree_Menu.SHOW:  # Show the tree nodes
            bst.dump()

        elif menu == Tree_Menu.SHOW_REVERSE:  # Show the tree nodes reversely
            bst.dump(reverse=True)

        elif menu == Tree_Menu.KEY_RANGE:  # Print minimum and maximum key number
            print(f'The minimum key number: {bst.min_key()}')
            print(f'The maximum key number: {bst.max_key()}')

        else:  # End the menu
            break


def binary_search_tree_test():
    bst = BinarySearchTree()
    run_menu(bst)


if __name__ == '__main__':
    binary_search_tree_test()
