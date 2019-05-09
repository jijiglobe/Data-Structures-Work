def appearances(strink, low=0, high=-1):
    if high <= 0:
        high = len(strink)-1
    if low >= high:
        return {strink[low]: 1}
    recurse = appearances(strink,low+1,high)
    
    if strink[low] in recurse:
        recurse[strink[low]]+=1
    else:
        recurse[strink[low]] = 1
    return recurse
print(appearances("Hello world"))
