test = [14, 4, 32, 9, 1, 5, 22, 3, 18, 300, 501, 1032, 1, 394, 12, 392, 31, 567, 3, 45, 35]

def merge(arr1, arr2):
    """ Merges two sorted arrays (ascending order)"""
    i = 0
    j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            merged.append(arr2[j])
            j += 1
        else:
             merged.append(arr1[i])
             merged.append(arr2[j])
             i += 1
             j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    print("Merged", arr1, 'and', arr2, 'into:', merged)
    return merged

def mergeSort(arr):
    """ Sorts an array using a divide and conquer algorithm """
    print('sorting:', arr)
    if len(arr) <= 1:
        return arr
    midPoint = len(arr)//2
    left = mergeSort(arr[:midPoint])
    right = mergeSort(arr[midPoint:])
    return merge(left, right)

mergeSort(test)

