from collections import deque

def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return completed == numCourses

numCourses = int(input("Enter the no. of courses: "))

m = int(input("Enter no of prerequisite pairs: "))

prerequisites = []
for i in range(m):
    course, prereq = map(int, input(f"Enter pair {i+1}: ").split())
    prerequisites.append([course, prereq])

print(canFinish(numCourses, prerequisites))