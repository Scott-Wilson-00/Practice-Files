import linked_list as link


class SearchableLinkedList(link.LinkedList):
    """A link list that can be searched and have any of its nodes data accessed"""
    def __init__(self, head=None):
        super(SearchableLinkedList, self).__init__(head)

    def search_list(self, value):
        """Checks whether the given value exists in the list"""
        n = self.head
        while n:
            if n.data == value: return True
            n = n.pointer
        return False

    def get_data(self, pos):
        """Returns the data of the node at the specified position"""
        if type(pos) != int:
            print('Position must be an integer')
            return False
        if pos < 1 or pos > self.get_length():
            print('Position out of range')
            return False

        n = self.head
        for i in range(1, pos):
            n = n.pointer
        return n.data


# Driver program
if __name__ == '__main__':
    lst = SearchableLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.append('d')
    lst.append('e')

    print('List: ', end='')
    lst.print_list()             # a, b, c, d, e
    print(lst.search_list('a'))  # True
    print(lst.search_list('e'))  # True
    print(lst.search_list(97))   # False

    # b, a, e, d, c
    print(', '.join([lst.get_data(2), lst.get_data(1), lst.get_data(5), lst.get_data(4), lst.get_data(3)]))