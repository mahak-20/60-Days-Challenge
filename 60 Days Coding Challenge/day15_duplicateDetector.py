import time

agent_ids = list(map(int, input("Enter agent IDs: ").split()))

start = time.time()

duplicate_found = False

for i in range(len(agent_ids)):
    for j in range(i+1, len(agent_ids)):
        if agent_ids[i] == agent_ids[j]:
            duplicate_found = True
            break

end = time.time()

print("Brute Force Time:", end-start)

start = time.time()
seen = set()

duplicate_found = False

for id in agent_ids:
    if id in seen:
        duplicate_found = True
        break
    seen.add(id)

end = time.time()

print("Optimized Time:", end-start)