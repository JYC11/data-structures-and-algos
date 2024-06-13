from heapq import heappop, heappush

# def kWeakestRows(mat,k):
#     counts = [sum(row) for row in mat]
#     rows_dict = {}
#     for i in range(len(counts)):
#         if rows_dict.get(counts[i],None) is None:
#             rows_dict[counts[i]] = [i]
#         else:
#             rows_dict[counts[i]] = rows_dict[counts[i]] + [i]
#     sorted_keys = sorted(rows_dict.keys())
#     final = []
#     for key in sorted_keys:
#         final = final + rows_dict[key]

#     return final[:k]


def kWeakestRows(mat, k):
    cols = len(mat[0])
    h = []
    for r, row in enumerate(mat):
        if row[-1] == 0:
            heappush(h, (row.index(0), r))
        else:
            heappush(h, (cols, r))
    ans = [0] * k
    for i in range(k):
        _, ans[i] = heappop(h)
    return ans


kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3)

"""
A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.


- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5

2
0
3
1
4

"""
