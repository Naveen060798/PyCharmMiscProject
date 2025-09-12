def unique_number(*args):
    nums=set(args)
    return list(nums)

print("Enter numbers with space: ")
nums=input("")

numbers=[int(n) for n in nums.split()]
unique=unique_number(*numbers)
print("\nUnique Numbers:")
print(unique)