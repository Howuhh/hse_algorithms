import sys
import threading

# On AVL trees:
# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# https://medium.com/@aksh0001/avl-trees-in-python-bc3d0aeb9150
# stepick from CS Center, Kulikov

class Node:
    def __init__(self, key):
        self.key = key

        self.height = 1
        self.left = None
        self.right = None
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def next(self, key):
        next_node = self._next(self.root, key, None)
        
        if next_node is None:
            return 
        return next_node.key
        
    # от корня -> когда налево запоминаем min
    def _next(self, root, key, acc):
        if root is None:
            return acc
        
        if key < root.key:
            if acc is None or root.key < acc.key:
                return self._next(root.left, key, root)
            else:
                return self._next(root.left, key, acc)
        else:
            return self._next(root.right, key, acc)

    # от корня -> когда направо запоминаем max
    def prev(self, key):
        prev_node = self._prev(self.root, key, None)
        
        if prev_node is None:
            return
        return prev_node.key
                    
    def _prev(self, root, key, acc):
        if root is None:
            return acc
        
        if key <= root.key:
            return self._prev(root.left, key, acc)
        else:
            if acc is None or root.key > acc.key:
                return self._prev(root.right, key, root)
            else:
                return self._prev(root.right, key, acc)
            
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        
        return self._rebalance(root)
        
    def exists(self, key):
        return self._exists(self.root, key)
    
    def _exists(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._exists(root.left, key)
        else:
            return self._exists(root.right, key)
    
    def _get_node(self, root, key):
        if root is None:
            return root
        
        if key == root.key:
            return root
        elif key < root.key:
            return self._get_node(root.left, key)
        else:
            return self._get_node(root.right, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None or root.right is None:
                leaf = root.left or root.right
                return leaf
            else:
                min_leaf = self._get_min_leaf(root.right)

                root.key = min_leaf.key
                root.right = self._delete(root.right, min_leaf.key)
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        
        return self._rebalance(root)
                
    def _get_min_leaf(self, root):
        if root.left is None:
            return root
        return self._get_min_leaf(root.left)

    def _height(self, root):
        return 0 if root is None else root.height
    
    def _balance(self, root):
        if root is None:
            return 0
        return self._height(root.left) - self._height(root.right)
                
    def _rebalance(self, root):
        root_balance = self._balance(root)
        root_left_balance = self._balance(root.left)
        root_right_balance = self._balance(root.right)
        
        ## Left-Left
        if root_balance > 1 and root_left_balance >= 0:
            return self._right_rotate(root)
        
        # Left-Right
        if root_balance > 1 and root_left_balance < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        # Right-Right
        if root_balance < -1 and root_right_balance <= 0:
            return self._left_rotate(root)
        
        # Right-Left
        if root_balance < -1 and root_right_balance > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
                              
    def _left_rotate(self, root):
        new_root = root.right
        
        root.right = new_root.left

        new_root.left = root
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        
        return new_root
    
    def _right_rotate(self, root):         
        new_root = root.left

        root.left = new_root.right
        
        new_root.right = root        
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        
        return new_root
        
    
def main():
    tree = AVLTree()
    
    for operation in sys.stdin:
        operation, x = operation.split()
        x = int(x)
                
        if operation == "insert":
            tree.insert(x)
        elif operation == "delete":
            tree.delete(x)
        elif operation == "exists": 
            print("true" if tree.exists(x) else "false")
        elif operation == "next":
            next_val = tree.next(x)
            print("none" if next_val is None else next_val)
        elif operation == "prev":
            prev_val = tree.prev(x)
            print("none" if prev_val is None else prev_val)
 
        

if __name__ == "__main__":
    main()