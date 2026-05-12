arr = list(map(int, input("Enter the elements: ").split()))

for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i-1]

print("Prefix sum array: ", arr)