def two_sum(nums, target):
    lookup = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in lookup:
            return [lookup[needed], i]
        lookup[nums[i]] = i
    return []       

coordinates = [2, 7, 11, 15]
target = 9

print(two_sum(coordinates, target))