s = list(input("Enter the string: ")   )
start = 0
end = len(s) -1

while start < end :
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1

print("Reversed string is: ","".join(s))


