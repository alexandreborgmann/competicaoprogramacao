import heapq

h = [1, 5, 10, -1, 200, 3]
print(h)
heapq.heapify(h)
print(h)
while h:
    print(heapq.heappop(h))
