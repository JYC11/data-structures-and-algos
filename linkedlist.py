class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def print(self):
        if self.start_node is None:
            print("Linked list is empty")
            return
        node = self.start_node
        llstr = ''
        while node:
            llstr += str(node.data) + ' ==> ' if node.next else str(node.data)
            node = node.next
        print(llstr)
    
    def get_length(self):
        count = 0
        node = self.start_node
        while node:
            count += 1
            node = node.next
        print(count)
        return count

    def insert_at_beginning(self,data):
        node = Node(data, self.start_node)
        self.start_node = node
    
    def insert_at_end(self,data):
        if self.start_node is None:
            self.start_node = Node(data,None)
            return

        node = self.start_node

        while node.next:
            node = node.next
        
        node.next = Node(data,None)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self. insert_at_beginning(data)
            return
        
        count = 0
        node = self.start_node
        while node:
            if count == index - 1:
                node = Node(data,node.next)
                node.next = node
                break
            node = node.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.start_node is None:
            return
        
        if self.start_node.data == data.after:
            self.start_node.next = Node(data_to_insert,self.start_node.next)

        node = self.start_node
        while node:
            if node.data == data_after:
                node = Node(data_to_insert, node.next)
                node.next = node
                break
            node = node.next

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.start_node = self.start_node.next
            return
        
        count = 0
        node = self.start_node
        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            node = node.next
            count += 1
    
    def remove_by_value(self,data):
        if self.start_node is None:
            return
        
        if self.start_node.data == data:
            self.start_node = self.start_node.next
            return

        node = self.start_node
        while node:
            if node.data == data:
                node.next = node.next.next
                break
            node = node.next


    def insert_values(self, data_list):
        self.start_node = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["a","b","c","d"])
    ll.get_length()
    # ll.insert_at(1,"x")
    # ll.remove_at(2)
    # ll.print()