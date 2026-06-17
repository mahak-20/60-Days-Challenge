import heapq

emergency_room = []
heapq.heappush(emergency_room, (-5, "Alice"))
heapq.heappush(emergency_room, (-9, "Bob"))
heapq.heappush(emergency_room, (-3, "Charlie"))
heapq.heappush(emergency_room, (-10, "David"))

print("Treatment Order: ")

while emergency_room:
    severity, name = heapq.heappop(emergency_room)
    print(f"Treating {name} (severity {-severity})")
    