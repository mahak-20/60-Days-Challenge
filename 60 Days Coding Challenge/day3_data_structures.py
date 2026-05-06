numbers = list(map(int, input("Enter the list of numbers:").split()))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.reverse()
print(numbers)
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) +1
print(freq)