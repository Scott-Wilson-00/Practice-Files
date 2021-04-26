
class Node:
    """A node stores data and a pointer to the next node"""
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:
    """A singly linked list"""
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        """Traverses the list, printing the data of each node"""
        if self.head:
            n = self.head
            while n:
                if n.pointer:
                    print(n.data, end=', ')
                else:
                    print(n.data)
                n = n.pointer

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


    def peek(self):
        """Returns the data of the list's head"""
        return self.head.data if self.head else None

    def delete_list(self):
        """Deletes all the contents of the list using garbage collection"""
        self.head = None

    def push(self, new_data):
        """Pushes a node containing the new data to the front of the list"""
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            node.pointer = self.head
            self.head = node

    def append(self, new_data):
        """Appends a node containing the new data to the end of the list"""
        node = Node(new_data)
        if self.head:
            n = self.head
            while n:
                if n.pointer:
                    n = n.pointer
                    continue
                break
            n.pointer = node
        else:
            self.head = node

    def insert_node(self, new_data, pos):
        """Inserts a node containing the new data at the given position (1-n)"""

        # Ensures valid argument
        if type(pos) != int:
            print("Position must be an integer value")
            return False

        # Pushes data
        elif pos == 1:
            self.push(new_data)
            return True

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
            for i in range(1, pos):
                if i == pos - 1:
                    prev = n
                n = n.pointer
            node = Node(new_data, n)
            prev.pointer = node
            return True

        # Intended position of node exceeds the length of the list + 1
        # Eg: Node at position 3 cannot point to node at position 5
        print('No node at previous position')
        return False

    def remove_node(self, pos):
        """Disengages a node from the list and returns it's data"""

        # List is empty
        if not self.head:
            print('List is already empty')
            return False

        # Removing the head of the list
        elif pos == 1:
            prev = self.head
            self.head = self.head.pointer
            prev.pointer = None
            return prev.data

        # Removing the tail of the list
        elif self.get_length() == pos:
            n = self.head
            while n.pointer.pointer:
                n = n.pointer
            data = n.pointer.data
            n.pointer = None
            return data

        # Removing an element between two nodes
        elif 1 < pos < self.get_length():
            n = self.head
            for i in range(1, pos):
                if i == pos - 1:
                    prev = n
                n = n.pointer
            prev.pointer = n.pointer
            n.pointer = None
            return n.data

        print('There is no node at this index')
        return False


# Driver program
if __name__ == '__main__':
    lst = LinkedList()

    print('----------------------')
    print('Before list generation:')
    print('Length of list:', lst.get_length())
    print('Peek:', lst.peek())
    print('----------------------')
    print('During list generation (errors):')

    lst.push('b')                  # b
    lst.remove_node(2)             # b              --> (no node at this position to remove)
    lst.append('d')                # b, d
    lst.insert_node('c', 2)        # b, c, d
    lst.insert_node('y', 5)        # b, c, d        --> (node at position 5 will not link with node at position 3)
    lst.push('a')                  # a, b, c, d
    lst.append('e')                # a, b, c, d, e
    removed = lst.remove_node(4)   # a, b, c, e
    lst.insert_node('z', 3)        # a, b, z, c, e
    lst.remove_node(-9293)         # a, b, z, c, e  --> (no node at this position to remove)

    print('---------------------------')
    print('After list generation:')
    print('List:')
    lst.print_list()
    print('Length of list:', lst.get_length())
    print('Peek:', lst.peek())
    print('Data removed:', removed)
    print('---------------------------')
    lst.delete_list()
    print('List deleted.')
    print('Length of list:', lst.get_length())
    print('Peek:', lst.peek())