my_list = [1, 2, 3, 4, 5]
n =int(input('enter number of times to rotate'))
rotated_list = my_list[-n:] + my_list[:-n]
print(f"Right rotated: {rotated_list}")