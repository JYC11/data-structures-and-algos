from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)

    while True:
        popped = q.popleft()
        location -= 1
        maximum = 0 if len(q) == 0 else max(q)
        if location != -1 and popped >= maximum:
            answer += 1
        elif location != -1 and popped < maximum:
            q.append(popped)
        elif location == -1 and popped >= maximum:
            answer += 1
            break
        elif location == -1 and popped < maximum:
            q.append(popped)
            location = len(q)-1

    return answer


# print(solution([2,1,3,2],2))
# print(solution([1, 1, 9, 1, 1, 1],5))

q = deque([])
print(max(q))

"""
[2,1,3,2]
l = 2
answer = 0

[1,3,2]
l = 1 (2-1)
popped = 2
answer = 0
max(q) > popped
q.append(popped) = [1,3,2,2]

[3,2,2]
l = 0 (1-0)
popped = 1
answer = 0
max(q) > popped
q.append(popped) = [3,2,2,1]

[2,2,1]
1 = -1
popped = 3
answer = 0
max(q) > popped = False
answer += 1
---------------------------------------
[2,1,3,4]
l = 2
answer = 0

[1,3,4]
l = 1
answer = 0
popped = 2
max(q) > popped: q.append(popped) = [1,3,4,2]

[3,4,2]
l = 0
answer = 0
popped = 1
max(q) > popped: q.append(popped) = [3,4,2,1]

[4,2,1]
l = -1
answer = 0
popped = 3
max(q) > popped: q.append(popped) = [4,2,1,3]
l = 3 (len(q)-1)

[2,1,3]
l = 3
answer = 0
popped = 4
max(q) < popped: answer += 1


"""
