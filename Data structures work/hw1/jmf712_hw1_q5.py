def fibs(n):
    first = 1
    second = 1
    index = 0
    while index<n:
        if(index == 0 or index == 1):
            yield 1
        else:
            yield first + second
            first, second = second, first + second
        index +=1
