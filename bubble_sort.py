def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [-2, 45, 6, 7, 9, 10]
print("Array before Bubble Sort:", arr)
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)
