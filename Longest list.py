# Sample nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

# Assume first sublist is largest initially
largest_list = nested_list[0]

# Loop through each sublist
for sublist in nested_list:
    if len(sublist) > len(largest_list):
        largest_list = sublist

# Print result
print("The largest list is:", largest_list)
print("Length of largest list:", len(largest_list))
