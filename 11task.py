# Define a list
my_list = [10, 20, 30, 40, 50]
print("simple list:" ,my_list)

# 1. Append an element to the list
my_list.append(60)
print("After append:", my_list)

# 2. Extend the list with another list
my_list.extend([70, 80])
print("After extend:", my_list)

# 3. Insert an element at a specific position
my_list.insert(2, 25)
print("After insert:", my_list)

# 4. Remove an element from the list
my_list.remove(40)
print("After remove:", my_list)

# 5. Pop an element from the list (default last element)
popped_element = my_list.pop()
print("After pop:", my_list, "| Popped element:", popped_element)

# 6. Pop an element from a specific position
popped_element = my_list.pop(2)
print("After pop at index 2:", my_list, "| Popped element:", popped_element)

# 7. Get the index of an element
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# 8. Count the occurrences of an element
count_of_20 = my_list.count(20)
print("Count of 20:", count_of_20)

# 9. Sort the list
my_list.sort()
print("After sort:", my_list)

# 10. Reverse the list
my_list.reverse()
print("After reverse:", my_list)

# 11. Clear the list
my_list.clear()
print("After clear:", my_list)

# Reinitialize the list for further operations
my_list = [10, 20, 30, 40, 50]

# 12. Copy the list
my_list_copy = my_list.copy()
print("Original list:", my_list, "| Copied list:", my_list_copy)

# 13. Demonstrate list comprehension
squared_list = [x**2 for x in my_list]
print("Squared list:", squared_list)

# 14. Demonstrate filtering using list comprehension
filtered_list = [x for x in my_list if x > 25]
print("Filtered list (elements > 25):", filtered_list)

# 15. Demonstrate mapping using list comprehension
mapped_list = [str(x) + '!' for x in my_list]
print("Mapped list:", mapped_list)
