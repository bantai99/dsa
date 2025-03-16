def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 17, 19, 20, 36, 1]
print("Array before insertion sort:", arr)
print("Sorted array using Insertion Sort:", insertion_sort(arr))
