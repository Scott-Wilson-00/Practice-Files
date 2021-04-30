# Selection sorting algorithm
# Best Case Time Complexity: O(n^2)
# Worst Case Time Complexity: O(n^2)

unsorted = [66, 33, 11, 88, 99, 77, 55, 22, 44]
unsorted2 = ['o', 'f', 'y', 'p', 'l', 'p']


def selection_sort(arr):
    """Sorts the given array using the selection sort algorithm"""

    for i in range(len(arr) - 1):
        min_value = min(arr[i:])
        min_index = arr.index(min_value, i)

        if min_index == i:
            continue
        else:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort(unsorted))
print(selection_sort(unsorted2))