def solution(num):
    maximum = num

    for i in range(len(str(num))):
        temp = str(num)

        if temp[i] == "9":
            temp = temp[:i]+"6"+temp[i+1:]
        else:
            temp = temp[:i]+"9"+temp[i+1:]

        new = int(temp)

        if new > maximum:
            maximum = new

    return maximum

solution(9669)