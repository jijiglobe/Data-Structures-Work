def factors(n):
    for x in range(int(n/2)):
        if n % (x+1) == 0:
            yield x+1
    yield n
