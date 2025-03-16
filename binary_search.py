def binary_search(arr, x):
    lb, ub = 0, len(arr) - 1
    while lb <= ub:
        mid = (ub + lb) // 2
        if arr[mid] < x:
            lb = mid + 1
        elif arr[mid] > x:
            ub = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
x = int(input("Enter number to search: "))
result = binary_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the list.")
