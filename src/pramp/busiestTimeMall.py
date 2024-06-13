def find_busiest_period(data):
    current_visitors = 0
    maximum = 0
    max_time = 0

    for i in range(0, len(data)):
        if data[i][2] == 1:
            current_visitors += data[i][1]
        elif data[i][2] == 0:
            current_visitors -= data[i][1]

        if i < len(data) - 1 and data[i][0] == data[i + 1][0]:
            continue

        if current_visitors > maximum:
            maximum = current_visitors
            max_time = data[i][0]

    return max_time


data = [
    [1487799425, 14, 1],
    [1487799425, 4, 0],
    [1487799425, 2, 0],
    [1487800378, 10, 1],
    [1487801478, 18, 0],
    [1487801478, 18, 1],
    [1487901013, 1, 0],
    [1487901211, 7, 1],
    [1487901211, 7, 0],
]

print(find_busiest_period(data))
