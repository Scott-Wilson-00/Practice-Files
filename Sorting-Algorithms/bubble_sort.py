# Bubble sorting algorithm
# Best Case Time Complexity: O(n)
# Worst Case Time Complexity: O(n^2)
unsorted = [9, 4, 5, 7, 2, 1]
unsorted2 = ['p', 'o', 'b', 'y', 'i', 's']


def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm"""
    if type(arr) != list: return

    has_made_swap = True

    while has_made_swap:
        has_made_swap = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                has_made_swap = True

    return arr


print(bubble_sort(unsorted))
print(bubble_sort(unsorted2))