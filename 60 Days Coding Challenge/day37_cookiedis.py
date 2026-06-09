def findContentChildren(g, s):
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child<len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    return child

g = list(map(int, input("Enter the greed factors: ").split()))
s = list(map(int, input("Enter the cookie sizes: ").split()))

print(findContentChildren(g,s))
