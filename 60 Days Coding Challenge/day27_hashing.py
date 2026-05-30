def detect_duplicate(posts, k):
    seen = {}
    for i in range(len(posts)):
        if posts[i] in seen:
            distance = i - seen[posts[i]]
            if distance <= k:
                return True
        seen[posts[i]] = i
    return False

events = ["post1", "post2", "post3", "post1", "post4"]
k = 3

result = detect_duplicate(events, k)

if result:
    print("Suspicious repeated activity detected")

else:
    print("No suspicious activity detected")