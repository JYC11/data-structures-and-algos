def solution(phone_book): #hash map
    phone_book = sorted(phone_book)
    for num1, num2 in zip(phone_book,phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True
    
print(solution(["97674223", "119", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
