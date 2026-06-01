from collections import Counter
def top_k_sort(hashtags, k):
    freq = Counter(hashtags)

    sorted_tags = sorted(
        freq.items(), 
        key = lambda x: x[1],
        reverse = True
        )
    return [tag for tag, count in sorted_tags[:k]]
hashtags = [
"#AI",
"#music",
"#AI",
"#travel",
"#music",
"#AI"
]

k = 2

print(top_k_sort(hashtags, k))

