import sys

class Node:
    def __init__(self, key):
        self.key = key

        self.height = 1
        self.size = 1
        
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None
        
    def k_max(self, k):
        k = self._size(self.root) - k + 1
        
        return self._k_max(self.root, k)

    def _k_max(self, root, k):
        if root.left is None and root.right is None:
            return root.key
            
        if self._size(root.left) == k - 1:
            return root.key
        elif self._size(root.left) < k:
            return self._k_max(root.right, k - self._size(root.left) - 1)
        else:
            return self._k_max(root.left, k)

    def _size(self, root):
        if root is None:
            return 0
        return root.size
            
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
        root.size = self._size(root.left) + self._size(root.right) + 1
        
        return self._rebalance(root)
                
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
        root.size = self._size(root.left) + self._size(root.right) + 1
        
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
        
        root.size = self._size(root.left) + self._size(root.right) + 1
        new_root.size = self._size(new_root.left) + self._size(new_root.right) + 1       
        
        return new_root
    
    def _right_rotate(self, root):         
        new_root = root.left
        
        root.left = new_root.right
                
        new_root.right = root        
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        
        root.size = self._size(root.left) + self._size(root.right) + 1
        new_root.size = self._size(new_root.left) + self._size(new_root.right) + 1
        
        return new_root

def main():
    tree = AVLTree()
    
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        operation, x = map(int, sys.stdin.readline().split())
        
        if operation == 1:
            tree.insert(x)
        elif operation == 0:
            print(tree.k_max(x))
        elif operation == -1:
            tree.delete(x)
        

if __name__ == "__main__":
    main()