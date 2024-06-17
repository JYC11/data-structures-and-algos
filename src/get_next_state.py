# Function to count live neighbors
def count_live_neighbors(row_num: int, col_num: int, max_rows: int, max_cols: int) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for row_increment, col_increment in directions:
        new_row, new_col = row_num + row_increment, col_num + col_increment
        if 0 <= new_row < max_rows and 0 <= new_col < max_cols:
            count += graph[new_row][new_col]
    return count


def next_state(graph: list[list[int]]) -> list[list[int]]:
    # Get the dimensions of the graph
    num_rows = len(graph)
    num_cols = len(graph[0])

    # Create a copy of the graph to store the next state
    next_graph = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    # Iterate over each cell in the graph, skipping the edges
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            live_neighbors = count_live_neighbors(r, c, num_rows, num_cols)
            if graph[r][c] == 1:  # Checks live nodes
                if live_neighbors < 2 or live_neighbors > 3:
                    next_graph[r][c] = 0  # Dies due to underpopulation or overpopulation
                else:
                    next_graph[r][c] = 1  # Survives
            else:  # Checks dead nodes
                if live_neighbors == 3:
                    next_graph[r][c] = 1  # Revives due to having enough neighbors
                else:
                    next_graph[r][c] = 0  # Stays dead

    return next_graph


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

next_graph = next_state(graph)
for row in next_graph:
    print(row)
