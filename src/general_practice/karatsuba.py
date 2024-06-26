def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    else:
        n = max(len(str(x)), len(str(y)))
        n2 = n // 2

        a = num1 // (10**n2)
        b = x % (10**n2)
        c = y // (10**n2)
        d = y % (10**n2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        prod = ac * 10 ** (2 * n2) + (ad_plus_bc * 10**n2) + bd
        return prod


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
karatsuba(x, y)
