def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [-2, 45, 6, 7, 9, 10]
print("Array before Bubble Sort:", arr)
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Loop through the array
        swapped = False
        for j in range(n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Swap if the element is greater than the next one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps happened, the array is already sorted
            break

arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print("Sorted array:", arr)
