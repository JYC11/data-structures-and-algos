from heapq import heappop, heappush


def inverse(n):
    return n * -1


def lastStoneWeight(stones):  # heap
    heap = []
    for s in stones:
        heappush(heap, inverse(s))

    while len(heap) >= 2:
        y = heappop(heap)
        x = heappop(heap)
        if y == x:
            pass
        else:
            y = y - x
            heappush(heap, y)
    if len(heap) == 0:
        return 0
    elif len(heap) == 1:
        return inverse(heappop(heap))


print(lastStoneWeight([1]))
