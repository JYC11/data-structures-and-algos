# def fizzbuzz():
#     for num in range(1,101):
#         if num%5 == 0 and num%3 == 0:
#             print("FizzBuzz")
#         elif num%5 == 0:
#             print("Buzz")
#         elif num%3 == 0:
#             print("Fizz")
#         else:
#             print(num)

"""
0,1,1,2,3,5,....
"""


def fibonacciRecursion(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2)


"""
fibonacci(2) => fibonacci(1) + fibonacci(0) = 1

"""
for i in range(1, 11):
    print(fibonacciRecursion(i))


def fibonacciDynamic(n):
    return


"""
naive:
selected bar = odd one out or it could be the not heavier one

odd one out
when we compare one by one
the scale is going to tip to the heavier one

the normal one
as we check one by one
one of them is going to tip over to the comparing bar

compare 7 times at max to get the solution


the smarter solution:
4, 4 comparison 1, see which one tips over to the other side
take the side that is heavier

4 bars to compare

2,2 comparison 2, see which one tips over to the other side
take the side is heavier

2 bars compare

1,1 comparison 3, see which one tips over to the other side
take the side is heavier

this is the odd one out

compare 3 times to get the solution


"""
