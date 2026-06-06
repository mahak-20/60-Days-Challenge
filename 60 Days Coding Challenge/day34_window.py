def max_average(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum/k

nums = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter the value of k: "))

print(max_average(nums, k))