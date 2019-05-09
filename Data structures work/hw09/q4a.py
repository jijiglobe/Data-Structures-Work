def intersection_list(lst1, lst2):
    lst1.sort()
    lst2.sort()
    ans = []
    pointer1 = pointer2 = 0
    while pointer1 < len(lst1) and pointer2 < len(lst2):
        if lst1[pointer1] == lst2[pointer2]:
            ans.append(lst1[pointer1])
            pointer1+=1
            pointer2+=1

        elif lst1[pointer1] < lst2[pointer2]:
            pointer1+=1
        elif lst2[pointer2] < lst1[pointer1]:
            pointer2+=1
    return ans
def test():
    lst1 = [3,6,1,2,7,8]
    lst2 = [0,9,6,2,7,54]
    print(intersection_list(lst1,lst2))

