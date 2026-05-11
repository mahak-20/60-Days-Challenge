arr = list(map(int,input("Enter the elements:").split()))

count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1
print("Number of even elements:", count)