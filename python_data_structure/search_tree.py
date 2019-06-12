#!/usr/bin/python
# coding: utf-8


class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)

    def has_any_child(self):
        return self.rightChild or self.leftChild

    def has_both_child(self):
        return self.leftChild and self.rightChild

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.payload = value
        self.rightChild = right_child
        self.leftChild = left_child
        if self.has_left_child():
            self.leftChild.parent = self
        if self.has_right_child():
            self.rightChild.parent = self

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, Key not in Tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Key not in Tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.leftChild:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        elif node.has_both_child():
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.payload = succ.payload
        else:
            if node.has_left_child():
                if node.is_left_child():
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                elif node.is_right_child():
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                else:
                    node.replace_node_data(
                        node.leftChild.key,
                        node.leftChild.payload,
                        node.leftChild.leftChild,
                        node.leftChild.rightChild)
            else:
                if node.is_left_child():
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                elif node.is_right_child():
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                else:
                    node.replace_node_data(
                        node.rightChild.key,
                        node.rightChild.payload,
                        node.rightChild.leftChild,
                        node.rightChild.rightChild)

    def _pre_order(self, root):
        if root:
            print(root.key, root.payload)
            self._pre_order(root.leftChild)
            self._pre_order(root.rightChild)

    def pre_order(self):
        self._pre_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.leftChild)
            print(root.key, root.payload)
            self._in_order(root.rightChild)

    def in_order(self):
        self._in_order(self.root)


myTree = BinarySearchTree()
myTree[3] = "book"
myTree[5] = "water"
myTree[4] = "finger"
myTree[6] = "red"
myTree[2] = "pink"

print(myTree[6])
print(myTree[2])
myTree.pre_order()
print("-" * 10)
myTree.in_order()
