def intersection_list(lst1, lst2):
    lst1Map = {}
    for x in lst1:
        lst1Map[x] = None
    ans = []
    for x in lst2:
        if x in lst1Map:
            ans.append(x)
    return ans

def test():
    lst1 = [3,6,1,2,7,8]
    lst2 = [0,9,6,2,7,54]
    print(intersection_list(lst1,lst2))

