def sumSquaresLong(n):
    n -= 1
    ans = 0
    while n>0:
        ans += n**2
        n-=1
    return ans
def sumSquaresList(n):
    return sum([x**2 for x in range(n) if x!=0])
def sumSquaresOdd(n):
    ans = 0
    if(n%2 == 0):
        n -=1
    else:
        n -= 2
    while n>0:
        ans += n**2
        n-=2
    return ans
def sumSquaresOddEasy(n):
    return sum([x ** 2 for x in range(n) if x % 2 != 0])
