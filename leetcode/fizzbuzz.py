def fizzbuzz(n):
    answer = []
    for i in range(1,n+1):
        j = ''
        if i%3==0:
            j += "Fizz"
        if i%5==0:
            j += "Buzz"
        if i%3!=0 and i%5!=0:
            j += str(i)
        answer.append(j)
    return answer
print(fizzbuzz(15))