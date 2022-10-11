
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def at_begining(self, newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node

    # Function to insert node
    def insert_node(self, middle_node, newdata):
        if middle_node is None:
            return 
        
        new_node = Node(newdata)
        new_node.nextval = middle_node.nextval
        middle_node.nextval = new_node

    # Function to add node at the end
    def at_end(self, newdata):
        new_node = Node(newdata)
        if self.headval is None:
            self.headval = newdata
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = new_node

    def remove_node(self, remove_key):
        head = self.headval
        prev = None
        if head is not None:
            if head.dataval == remove_key:
                self.headval = head.nextval
                head = None
                return
        while head is not None:
            if head.dataval == remove_key:
                break
            prev = head
            head = head.nextval

        if head is None:
            return

        prev.nextval = head.nextval
        head = None

linked_list = LinkedList()
linked_list.headval = Node("1")
node2 = Node("3")
node3 = Node("4")
linked_list.headval.nextval = node2
node2.nextval = node3
linked_list.at_begining("0")
linked_list.insert_node(linked_list.headval.nextval, "2")
linked_list.at_end("5")
linked_list.remove_node("3")
linked_list.print_list()
