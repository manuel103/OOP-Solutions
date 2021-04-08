# Linked List

class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
        
    def __str__(self):
        return ('(' + str(self.data) + ')')
        
class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
        
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next
        print('None')
        
linked_list = LinkedList()
linked_list.add(89)
linked_list.add(90)
linked_list.add(45)
linked_list.add(76)
linked_list.print_list()