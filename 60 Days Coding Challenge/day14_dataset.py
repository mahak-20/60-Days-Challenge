sales = [100, 250, 150, 100, 250, 550, 400, 350]

freq = {}

for i in sales:
    freq[i] = freq.get(i, 0) + 1

print("frequency count: ", freq)
print("Maximum sale: ", max(freq))
print("Minimum sale: ", min(freq))
print("Average sale: ", sum(sales)/len(sales))