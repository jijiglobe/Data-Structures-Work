from random import randint
def list_min(lst, low=0, high=-1):
    if(len(lst) < 1):
        return None
    if high == -1:
        high = len(lst)-1
    if low == high:
        return lst[low]
    else:
        min1 = list_min(lst,low,int((low+high)/2))
        min2 = list_min(lst,int((low+high)/2)+1,high)
        if min1 < min2:
            return min1
        else:
            return min2

def test_min():
    is_good = True
    for x in range(1000):
        ans = []
        for x in range(randint(0,100)):
            ans.append(randint(-1000,1000))
        #sadly the built in min function for python cries when you feed it an empty list
        if(len(ans) != 0 and list_min(ans) != min(ans)):
            is_good = False
    print(is_good)
