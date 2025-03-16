a = [1, 2, 3, 4, 5, 6]
b = int(input("Enter number to search: "))

found = False
for i in a:
    if i == b:
        found = True
        break

if found:
    print("Item found in the list.")
else:
    print("Item not found in the list.")
