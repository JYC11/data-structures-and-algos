for test_case in range(1,11):
    pal_count = 0
    pal_length = int(input())
    char_box = [list(input()) for i in range(8)]
    for i in range(8):
        row = char_box[i]
        index = 0
        while index+pal_length <= len(row):
            string = ''.join(row[index:index+pal_length])
            if string == string[::-1]:
                pal_count += 1
            index+=1
        col = []
        for j in range(8):
            col.append(char_box[j][i])
        index = 0
        while index+pal_length <= len(col):
            string = ''.join(col[index:index+pal_length])
            if string == string[::-1]:
                pal_count += 1
            index+=1

    print(f"#{test_case} {pal_count}")