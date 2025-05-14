import heapq

min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print(heapq.heappop(min_heap))  # Smallest
