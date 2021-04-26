import linked_list as link


def find_middle_position(lst):
    """
    Odd: Finds the position of the middle element of a linked list
    Even: Finds the position of the second middle element of a linked list

    1 -> 2 -> 3 -> 4 -> 5 (3 is middle element)
    1 -> 2 -> 3 -> 4 -> 5 -> 6 (4 is middle element)

    :param lst: the linked list to find the middle of
    :return: the position of the middle element
    """
    return lst.get_length()//2 + 1 if lst.get_length() > 0 else None


def remove_middle_element(lst):
    """
    Removes the node in the middle of a linked list

    :param lst: the linked list which the node will be removed from
    :return: the data stored in the node
    """
    return lst.remove_node(find_middle_position(lst))


# Driver program
if __name__ == '__main__':
    lst = link.LinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.append('d')
    lst.append('e')
    lst.append('f')

    print('Data of node removed:', remove_middle_element(lst), '\n')               # d

    print('Current list:')
    lst.print_list()                                                                # a, b, c, e, f

    print('\nPosition of middle node in current list:', find_middle_position(lst))  # 3
