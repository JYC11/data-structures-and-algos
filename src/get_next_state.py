graph = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
]


def get_neighboring_coordinates(i: int, j: int):
    top_row = i - 1
    bottom_row = i + 1
    left_column = j - 1
    right_column = j + 1
    north = (top_row, j)
    south = (bottom_row, j)
    east = (i, left_column)
    west = (i, right_column)
    north_east = (top_row, left_column)
    north_west = (top_row, right_column)
    south_east = (bottom_row, left_column)
    south_west = (bottom_row, right_column)
    return north, south, east, west, north_east, north_west, south_east, south_west


def solution(graph: list[list[int]]) -> list[list[int]]:
    num_rows = len(graph)
    num_cols = len(graph[0])
    _next_graph = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            # is this a graph edge?
            if i != 0 or i != num_rows - 1 or j != 0 or j != num_cols - 1:
                if graph[i][j] == 1:
                    north, south, east, west, north_east, north_west, south_east, south_west = (
                        get_neighboring_coordinates(i, j)
                    )
                if graph[i][j] == 0:
                    ...
    return graph
