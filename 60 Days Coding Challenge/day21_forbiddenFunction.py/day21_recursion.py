def recursive_sum(arr, index):
    if index == len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index + 1)

arr = list(map(int, input("Enter numbers: ").split()))
result = recursive_sum(arr, 0)
print("Sum:", result)
