import array as arr

array = arr.array('i', [22, 32, 45, 78, 26])
print("Initial Array:", array)

print("First element of the array:", array[0])
print("Last element of the array:", array[-1])

print("Inserting an element (6) at the end of the array:")
array.insert(len(array), 6)
print(array)

print("Deleting element (6) from the array:")
array.remove(6)
print(array)

print("Traversing the array:")
for element in array:
    print(element)
