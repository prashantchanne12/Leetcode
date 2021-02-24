def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i+1]


print(find_corrupt_numbers([3, 1, 2, 5, 2]))
