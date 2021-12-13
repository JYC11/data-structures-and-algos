import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

def romanToDecimal(roman):
    toDecimal = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900, 
        "M":1000
    }

    result = 0
    i = 0
    while (i < len(roman)):
        first = toDecimal[roman[i]]
        if (i + 1 < len(roman)):
            second = toDecimal[roman[i+1]]
            if(first >= second):
                result = result + first
                i = i + 1
            else:
                result = result + second - first
                i = i + 2
        else:
            result = result + first
            i = i + 1
    return result

def decimalToRoman(decimal):
    toRoman = {
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
    }

    result = ""

    for dec,roman in toRoman.items():
        (n,decimal) = divmod(decimal,dec)
        result += roman * n
    
    return result

answer = romanToDecimal(A)+romanToDecimal(B)
romanAnswer = decimalToRoman(answer)

print(answer)
print(romanAnswer)