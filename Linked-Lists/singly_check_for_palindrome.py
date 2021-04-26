import linked_list as link


def check_for_palindrome(lst):
    """
    Determines whether the data stored in a linked list's nodes is a palindrome

    :param lst: the linked list to be checked
    :return: whether or not the list is a palindrome
    """
    length = lst.get_length()

    # Check if list is empty
    if length == 0:
        print('List is empty')
        return False

    half_len = length//2

    n = lst.head
    first_half = ''
    second_half = ''

    # Adds node data to the first or second half of the comparison
    for i in range(length):
        if i < half_len:
            first_half += str(n.data)
        else:
            second_half += str(n.data)
        n = n.pointer

    # Disregards the middle element if there are an odd number of nodes
    if length % 2 == 1:
        second_half = second_half[1:]

    return first_half == second_half[::-1]


# Driver program
if __name__ == '__main__':
    lst = link.LinkedList(link.Node('r'))
    lst.append('a')
    lst.append('c')
    lst.append('e')
    lst.append('c')
    lst.append('a')
    lst.append('r')
    # lst = r, a, c, e, c, a, r
    print(check_for_palindrome(lst))  # True
    lst.append('s')
    # lst = r, a, c, e, c, a, r, s
    print(check_for_palindrome(lst))  # False
