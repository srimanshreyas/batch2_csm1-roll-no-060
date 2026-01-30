import heapq

def water_jug_a_star(cap_a, cap_b, goal):
    h = lambda s: min(abs(goal - s[0]), abs(goal - s[1]))

    def neighbors(a, b):
        return {
            (cap_a, b), (a, cap_b), (0, b), (a, 0),
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),
            (a + min(b, cap_a - a), b - min(b, cap_a - a))
        }

    pq = [(h((0, 0)), 0, (0, 0), [])]
    visited = set()

    while pq:
        f, g, (a, b), path = heapq.heappop(pq)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal or b == goal:
            return path

        for n in neighbors(a, b):
            if n not in visited:
                heapq.heappush(pq, (g + 1 + h(n), g + 1, n, path))

    return None
print(water_jug_a_star(4, 3, 2))
