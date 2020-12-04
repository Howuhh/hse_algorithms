import sys
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

class Node:
    def __init__(self, key):
        self.key = key

        self.height = 1

        self.parent = None
        self.left = None
        self.right = None
        

class AVLTree:
    def __init__(self):
        self.root = None
        
    def next(self, key):
        check_ex = self.exists(key)

        if not check_ex:
            self.insert(key)
        
        next_elem = self._next(key)
        
        if not check_ex:
            self.delete(key)
        return next_elem
        
    def _next(self, key):  
        node = self._get_node(self.root, key)
        
        if node.right is not None:
            head = node.right
            while head.left is not None:
                head = head.left
            return head.key    
        
        p = node.parent
        while p is not None and p.right == node:
            p = p.parent
            node = node.parent
        
        if p is not None:
            return p.key
         
    
    def prev(self, key):
        check_ex = self.exists(key)
        
        if not check_ex:
            self.insert(key)
            
        prev_elem = self._prev(key)
        
        if not check_ex:
            self.delete(key)
            
        return prev_elem
                    
    def _prev(self, key):
        node = self._get_node(self.root, key)

        if node.left is not None:
            head = node.left
            while head.right is not None:
                head = head.right
            return head.key
        
        p = node.parent
        while p is not None and p.left == node:
            p = p.parent
            node = node.parent
            
        if p is not None:
            return p.key
            
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
            root.left.parent = root
        elif key > root.key:
            root.right = self._insert(root.right, key)
            root.right.parent = root
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
            if root.left is not None:
                root.left.parent = root
        elif key > root.key:
            root.right = self._delete(root.right, key)
            if root.right is not None:
                root.right.parent = root
        else:
            if root.left is None or root.right is None:
                leaf = root.left or root.right
                if leaf is not None:
                    leaf.parent = None
                return leaf
            else:
                min_leaf = self._get_min_leaf(root.right)

                root.key = min_leaf.key
                root.right = self._delete(root.right, min_leaf.key)
                if root.right is not None:
                    root.right.parent = root
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        
        return self._rebalance(root)
                
    def _get_min_leaf(self, root):
        if root.left is None and root.right is None: # or or and ???
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
        
        # Right-Right
        if root_balance < -1 and root_right_balance <= 0:
            return self._left_rotate(root)
        
        # Left-Right
        if root_balance > 1 and root_left_balance < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        # Right-Left
        if root_balance < -1 and root_right_balance > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
                              
    def _left_rotate(self, root):
        new_root = root.right
        new_root.parent = root.parent
        
        root.right = new_root.left
        root.parent = new_root
        
        if root.right is not None:
            root.right.parent = root
        
        new_root.left = root
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        
        return new_root
    
    def _right_rotate(self, root):         
        new_root = root.left
        new_root.parent = root.parent
        
        root.left = new_root.right
        
        root.parent = new_root
        if root.left is not None:
            root.left.parent = root
        
        new_root.right = root        
        
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1
        
        return new_root
    
    def _pre_order(self, root, nodes):
        if root is None:
            return
        
        nodes.append(root.key) 
        self._pre_order(root.left, nodes)
        self._pre_order(root.right, nodes)


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 5 * level + '->', node.key)
            self.printTree(node.left, level + 1)


def test():
    tree = AVLTree() 
    values = [10, 20, 30, 40, 50, 25]

    for value in values:
        tree.insert(value)
        
    nodes = []
    tree._pre_order(tree.root, nodes)
    assert nodes == [30, 20, 10, 25, 40, 50]
    
    # tree.printTree(tree.root)
    
    for value in values + [15, 0, 45, 25]:
        assert tree.exists(value) == (value in values)
        
    for val, next_ in [(10, 20), (20, 25), (25, 30), (40, 50), (50, None), (15, 20), (22, 25)]:
        assert tree.next(val) == next_
    
    for val, prev in [(10, None), (20, 10), (25, 20), (30, 25), (40, 30), (50, 40), (15, 10), (32, 30), (45, 40)]:
        assert tree.prev(val) == prev
        
    
def main():
    tree = AVLTree()
    
    for operation in sys.stdin:
        operation, x = operation.split()
        x = int(x)
        
        # print("--" * 8)
        # print(operation, x)
        
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
            

        # tree.printTree(tree.root) 
        # print()   
        

if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    # main_test()
    # test()