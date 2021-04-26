
class Node:
    """Represents a node in a doubly linked list"""
    def __init__(self, data, pointer=None, prev=None):
        self.data = data
        self.pointer = pointer
        self.prev = prev


class DoublyLinkedList:
    """A doubly linked list"""
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        """Traverses the list, printing the data of each node"""
        if not self.head:
            return False

        n = self.head
        while n:
            print(n.data, end=', ') if n.pointer else print(n.data)
            n = n.pointer

    def print_reversed_list(self):
        """Prints the list in reverse order"""
        if not self.head:
            return False

        n = self.head
        while n.pointer:
            n = n.pointer

        while n.prev:
            print(n.data, end=', ')
            n = n.prev

        print(n.data)

    def get_length(self):
        """Returns the number of nodes in the list"""
        length = 0
        if self.head:
            length += 1
            n = self.head
            while n.pointer:
                n = n.pointer
                length += 1
        return length

    def push(self, new_data):
        """Pushes a node containing the new data to the front of the list"""
        node = Node(new_data, self.head)
        if self.head:
            self.head.prev = node

        self.head = node

    def append(self, new_data):
        """Appends a node containing the new data to the end of the list"""
        if not self.head:
            self.push(new_data)
            return

        n = self.head
        while n.pointer:
            n = n.pointer

        node = Node(new_data, None, n)
        n.pointer = node

    def insert_node(self, new_data, pos):
        """Inserts a node containing the new data to the specified position (1-n)"""
        # Pushes data
        if pos == 1:
            self.push(new_data)
            return True

        # Position not an integer value
        elif type(pos) != int:
            print('Position must be an integer value')
            return False

        # No nodes to insert behind
        elif not self.head:
            print('No nodes in list')
            return False

        # Appends data
        elif self.get_length() + 1 == pos:
            self.append(new_data)
            return True

        # Inserts data in between two nodes
        elif 1 < pos <= self.get_length():
            n = self.head
            for i in range(1, pos-1):
                n = n.pointer
            node = Node(new_data, n.pointer, n)
            n.pointer = node
            node.pointer.prev = node
            return True

        # Intended position of node exceeds the length of the list + 1
        # Eg: Node at position 3 cannot point to node at position 5
        print('No node at previous position')
        return False

    def remove_node(self, pos):
        """Removes the node found at the specified position"""
        if not self.head:
            print('List is already empty')
            return False

        # Position not an integer value
        elif type(pos) != int:
            print('Position must be an integer value')
            return False

        # Removes the head node
        elif pos == 1:
            data = self.head.data
            self.head = self.head.pointer
            self.head.prev.pointer = None
            self.head.prev = None
            return data

        # Removes the last node
        elif pos == self.get_length():
            n = self.head
            while n.pointer:
                n = n.pointer

            n.prev.pointer = None
            n.prev = None
            return n.data

        # Removes a node in between the head and last
        elif 1 < pos < self.get_length():
            n = self.head
            for i in range(1, pos):
                n = n.pointer

            n.prev.pointer = n.pointer
            n.pointer.prev = n.prev
            n.pointer = n.prev = None
            return n.data

        print('There is no node at this index')
        return False


# Driver program
if __name__ == '__main__':
    lst = DoublyLinkedList()

    lst.push('c')              # c
    lst.append('d')            # c, d
    lst.push('a')              # a, c, d
    lst.insert_node('b', 2)    # a, b, c, d
    lst.remove_node(3)         # a, b, d
    lst.insert_node('x', 3)    # a, b, x, d
    lst.remove_node(4)         # a, b, x
    lst.append('y')            # a, b, x, y
    lst.remove_node(1)         # b, x, y

    lst.print_list()           # b, x, y
    lst.print_reversed_list()  # y, x, b
