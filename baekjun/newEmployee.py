import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = []
    for i in range(N):
        scores = list(map(int, sys.stdin.readline().split()))
        applicants.append(scores)

    applicants.sort()
    count = 1

    min_interview_score = applicants[0][1]

    for i in range(1,N):
        if applicants[i][1] < min_interview_score:
            min_interview_score = applicants[i][1]
            count += 1

    print(count)