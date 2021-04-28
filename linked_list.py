class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_linked_list(self):
        linked_list_string = ""
        node = self.head
        if node is None:
            print(Node)
        while node:
            linked_list_string += f" {str(node.data)} ->"
            node = node.next_node

        linked_list_string += " None"
        print(linked_list_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def append_to_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self_last_node = self.last_node.next_node

    def get_user_by_id(self, user_id: int) -> None:
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
