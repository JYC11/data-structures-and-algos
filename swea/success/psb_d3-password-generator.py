for i in range(10):
    test_num = input()
    seed_numbers = list(map(int,input().split()))
    to_subtract = {
        0:1,
        1:2,
        2:3,
        3:4,
        4:5
    }
    keep_subtracting = 1
    while keep_subtracting == 1:
        first_five = seed_numbers[:5]
        subtracted = [seed_numbers[i] - to_subtract[i] for i in range(5)]
        subtracted = [0 if i < 0 else i for i in subtracted]
        if 0 not in subtracted:
            seed_numbers = seed_numbers[5:] + subtracted
        else:
            first_zero_index = subtracted.index(0,0)
            first_zero = subtracted[:first_zero_index+1]
            final = seed_numbers[first_zero_index+1:] + first_zero
            final = [str(i) for i in final]
            keep_subtracting = 0

    print(f'#{test_num} {" ".join(final)}')