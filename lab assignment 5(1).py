nums = tuple(map(int, input("Enter integers separated by space: ").split()))

print("Total items:", len(nums))
print("Last item:", nums[-1])
print("Reverse order:", nums[::-1])

if 3 in nums:
    print("Yes")
else:
    print("No")

if len(nums) > 2:
    new_tuple = nums[1:-1]
    sorted_tuple = tuple(sorted(new_tuple))
    print("After removing first and last and sorting:", sorted_tuple)
else:
    print("Not enough elements")
