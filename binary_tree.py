#Binary tree data structure for semester project
#Code is based on homework assignment we had previously

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeSet():
    def __init__(self):
        self.root = None
        self.size_of_tree = 0

    def depth(self):
        def _depth(node):
            if node is None:
                return 0
            left_depth = _depth(node.left)
            right_depth = _depth(node.right)
            return 1 + max(left_depth, right_depth)

        return _depth(self.root)
    
    def contains(self, x):
        n = self.root
        while n is not None:
            if x < n.value:
                n = n.left
            elif x > n.value:
                n = n.right
            else:
                return True
        return False
    
    def add(self, x):
        n = self.root
        if n == None:
            self.root = Node(x)
            self.size_of_tree += 1
            return
        
        while True:
            if x == n.value:
                return         
            elif x < n.value:
                if n.left == None:
                    n.left = Node(x)
                    self.size_of_tree += 1
                    return
                else:
                    n = n.left
            else: 
                if n.right == None:
                    n.right = Node(x)
                    self.size_of_tree += 1
                    return
                else:
                    n = n.right

    def count(self, lo, hi):
        def count(node, lo, hi):
            if node is None:
                return 0
            elif lo <= node.value <= hi:
                return 1 + count(node.left, lo, hi) + count(node.right, lo, hi)
            elif lo > node.value:
                return count(node.right, lo, hi)
            else:
                return count(node.left, lo, hi)

        return count(self.root, lo, hi)
    
    def size(self):
        return self.size_of_tree
    
    def remove(self, x):
        n = self.root
        parent = None
        
        if self.contains(x) == False: return
        
        def replace(self, parent, n, p):
            if parent == None:    
                self.root = p
            elif parent.left == n: 
                parent.left = p
            elif parent.right == n:
                parent.right = p
            else:
                assert False, 'not a child'
                
        while n.value != x:
            if x < n.value:
                parent = n
                n = n.left
            else:
                parent = n
                n = n.right
                
        if n is None:
            return
                
        if n.left is None and n.right is None:
            replace(self, parent, n, None)
            self.size_of_tree -= 1
        elif n.left is None and n.right is not None:
            replace(self, parent, n, n.right)
            self.size_of_tree -= 1
        elif n.right is None and n.left is not None:
            replace(self, parent, n, n.left)
            self.size_of_tree -= 1
        else:
            k = n.right
            while k.left is not None:
                k = k.left
                
            l = k.value
            self.remove(k.value)
            n.value = l

    def avg_tree_depth(self):
        if self.root is None:
            return 0 

        def calculate_depths(node, current_depth):
            if node is None:
                return 0, 0  

            left_sum, left_count = calculate_depths(node.left, current_depth + 1)
            right_sum, right_count = calculate_depths(node.right, current_depth + 1)

            total_sum = left_sum + right_sum + current_depth
            total_count = left_count + right_count + 1
            return total_sum, total_count

        # Calculate total depth sum and total number of nodes
        total_sum, total_count = calculate_depths(self.root, 0)
        return round(total_sum / total_count, 3)

    
    def clear(self):
        self.root = None
        self.size_of_tree = 0