# Insertion sorting algorithm
# Best Case Time Complexity: O(n)
# Worst Case Time Complexity: O(n^2)

unsorted = [900, 400, 500, 700, 200, 100]
unsorted2 = ['l', 'a', 's', 'o', 'm', 't']


def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm"""

    for i in range(len(arr)):
        current = arr[i]
        j = i

        while current < arr[j-1] and j > 0:
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = current

    return arr


print(insertion_sort(unsorted))
print(insertion_sort(unsorted2))

