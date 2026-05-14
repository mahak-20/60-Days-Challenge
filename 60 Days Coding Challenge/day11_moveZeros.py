arr = list(map(int, input("Enter the elements: ").split()))

j=0

for i in range(len(arr)):
    
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j+=1
        
print("Array after moving zeroes to the end:", arr)