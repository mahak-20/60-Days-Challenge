arr = list(map(int, input("Enter the elements: ").split()))

max_sum = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        current_sum = sum(arr[i:j+1])
        if current_sum > max_sum:
            max_sum = current_sum
            
print("Max subarray sum is:", max_sum)