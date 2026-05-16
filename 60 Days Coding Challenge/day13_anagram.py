s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("Not Anagram")

else:
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq:
            print("Not Anagram")
            break
        freq[ch] -= 1
        if freq[ch] < 0:
            print("Not Anagram")
            break
    else:
        print("Anagram")