def generate_subsets(gems, current, index):

    print(current)

    for i in range(index, len(gems)):
        current.append(gems[i])
        generate_subsets(gems, current, i+1)
        current.pop()

gems = input("Enter the gems: ").split()

print("All possible combinations of gems: ")
generate_subsets(gems, [], 0)