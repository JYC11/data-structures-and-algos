def my_solution():  # fails due to stackoverflow
    for test_case in range(1, 11):
        char_box = [input() for i in range(100)]

        def expand_from_middle(s, left, right):
            if s is None or left > right:
                return 0
            while (left > 0 and right < len(s)) and (s[left] and s[right]):
                left -= 1
                right += 1
            return right - left - 1

        def get_longest_palindrome(matrix):
            max_length = 0
            for i in range(100):
                string = matrix[i]
                for i in range(100):
                    length = expand_from_middle(string, i, i + 1)
                    if len(length) > max_length:
                        max_length = length
            return max_length

        row = get_longest_palindrome(char_box)
        transposed = []
        for i in range(100):
            new_string = ""
            for j in range(100):
                new_string += char_box[j][i]
            transposed.append(new_string)

        col = get_longest_palindrome(transposed)

        print(f"#{test_case} {max(row,col)}")


T = 10


def call_me(M, N):
    # 가로에서 확인되면 세로는 안하게
    count = 0
    # 가로 확인
    tx_list = []
    for j in range(N):
        for k in range(N - M + 1):
            cnt = 0
            for t in range(M):
                if tx_list[j][t + k] == tx_list[j][M + k - t - 1]:
                    cnt += 1

            if cnt == M:
                result = M
                count += 1
                return result
    if count == 0:
        # 세로 확인
        for j in range(N):
            for k in range(N - M + 1):
                cnt = 0
                for t in range(M):
                    if tx_list[t + k][j] == tx_list[M + k - t - 1][j]:
                        cnt += 1

                if cnt == M:
                    for i in range(M):
                        result = M
                        return result


def actually_works():
    for tc in range(1, T + 1):
        _ = input()
        # array 형식 변환
        tx_list = []
        N = 100
        for i in range(N):
            N_str_list = list(map(str, input().split()))
            tx_list += N_str_list

        for M in range(100):
            try:
                temp = call_me(M, N)
                result = 0
                if temp is not None:
                    if temp >= 0:
                        result = call_me(M, N)
            except Exception:
                continue
        print("#{} {}".format(tc, result), end=" ")
        print()
