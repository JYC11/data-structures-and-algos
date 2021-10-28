from collections import deque

def bfs(graph,node,visited):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        popped = q.popleft()
        # get neigbors
        # check if index is not equal, check if connected
        # check if not visited
        # add to q

def dfs(graph,node,visited):
    # mark as visited
    visited[node] = True
    # get neighbors
    # check if index is not equal, check if connected
    # check if not visited
    # recursively call dfs
    return


def solution(n,computers):
    answer = 0
    # iterate through the computers
    # check if not visited
    # do the search algorithm
    # add 1 to answer
    return answer