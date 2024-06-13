class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def print_forward(self):
        if self.start_node is None:
            print("Linked list is empty")
            return
        node = self.start_node
        llstr = ""
        while node:
            llstr += str(node.data) + " ==> "
            node = node.next
        print(llstr)

    def print_backward(self):
        if self.start_node is None:
            print("Linked list is empty")
            return

        node = self.last_node()
        llstr = ""
        while node:
            llstr += str(node.data)
            node = node.prev
        print(llstr)

    def last_node(self):
        if self.start_node is None:
            return

        node = self.start_node
        while node:
            node = node.next

        return node

    def get_length(self):
        count = 0
        node = self.start_node
        while node:
            count += 1
            node = node.next
        return count

    def insert_at_beginning(self, data):
        if self.start_node is None:
            node = Node(data, self.start_node, None)
            self.start_node = node
        else:
            node = Node(data, self.start_node, None)
            self.start_node.prev = node
            self.start_node = node

    def insert_at_end(self, data):
        if self.start_node is None:
            self.start_node = Node(data, None)
            return

        node = self.start_node

        while node.next:
            node = node.next

        node.next = Node(data, None, node)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        node = self.start_node
        while node:
            if count == index - 1:
                node = Node(data, node.next, node)
                if node.next:
                    node.next.prev = node
                node.next = node
                break
            node = node.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.start_node is None:
            return

        if self.start_node.data == data_after:
            self.start_node.next = Node(data_to_insert, self.start_node.next)

        node = self.start_node
        while node:
            if node.data == data_after:
                node = Node(data_to_insert, node.next, node)
                if node.next:
                    node.next.prev = node
                node.next = node
                break
            node = node.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.start_node = self.start_node.next
            return

        count = 0
        node = self.start_node
        while node:
            if count == index:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                break
            node = node.next
            count += 1

    def remove_by_value(self, data):
        if self.start_node is None:
            return

        if self.start_node.data == data:
            self.start_node = self.start_node.next
            return

        node = self.start_node
        while node:
            if node.data == data:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                break
            node = node.next

    def insert_values(self, data_list):
        self.start_node = None
        for data in data_list:
            self.insert_at_end(data)
