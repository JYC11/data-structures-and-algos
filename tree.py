class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if len(self.children) > 0 and self.get_level() < level:
            for child in self.children:
                child.print_tree(level)
            

class TreeNodeND: #ND = Name and Designation
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,type):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if type == "both":
            print(prefix+f"{self.data[0]} ({self.data[1]})")
        if type == "name":
            print(prefix+self.data[0])
        if type == "designation":
            print(prefix+self.data[1])
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(type)

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data: #if less than data in node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else: #if more than data in node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        
        #visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()
        #visit base node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
        return elements

    def calculate_sum(self):
        elements = self.in_order_traversal()
        return sum(elements)

    def search(self,val):
        if search.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

            # max_value = self.left.find_max()
            # self.data = max_value
            # self.left = self.left.delete(max_value)

        return self
            

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

# numbers = [17,4,1,20,9,23,34]
# numbers_tree = build_tree(numbers)
# print(numbers_tree.in_order_traversal())