from random import randint
def split_by_sign(lst, low, high):
    if low >= high:
        return lst
    if lst[low] < 0 and lst[high] >=0:
        return split_by_sign(lst,low+1,high-1)
    if lst[low] >= 0 and lst[high] < 0:
        lst[low], lst[high] = lst[high], lst[low]
        return split_by_sign(lst,low+1,high-1)
    if lst[low] < 0 and lst[high] <0:
        return split_by_sign(lst,low+1,high)
    if lst[low] >=0 and lst[high] >= 0:
        return split_by_sign(lst,low,high-1)

def test_split():
    #I can just leave these in right?
    test_passed = True
    for x in range(100):
        test = []
        for y in range(randint(0,200)):
            test.append(randint(-1000,1000))
        split_by_sign(test,0,len(test)-1)
        for y in range(1,len(test)):
            if test[y-1] >=0 and test[y] < 0:
                test_passed = False
    if test_passed:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
