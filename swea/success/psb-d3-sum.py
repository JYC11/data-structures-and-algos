for test_case in range(1,11):
    t = int(input())
    matrix = [list(map(int,input().split())) for i in range(100)]
            
    row_sums = []
    col_sums = []
    dr = []
    dl = []
    for i in range(100):
        #diagonal right
        dr.append(matrix[i][i])
        #diagonal left
        dl.append(matrix[i][99-i])
        row_sums.append(sum(matrix[i]))
        col_sum = 0
        for j in range(100):
            col_sum += matrix[j][i]
        col_sums.append(col_sum)
    
    nums = [max(row_sums),max(col_sums),sum(dr),sum(dl)]
    
    print(f"#{test_case} {max(nums)}")



print(dr)
print(dl)
print(row_sums)
print(col_sums)
        
