def find_duplicates(lst):
    found = {}
    ans = []
    for x in lst:
        if x in found:
            if found[x] == 1:
                ans.append(x)
                found[x]+=1
        else:
            found[x] = 1
    return ans

def test_duplicates():
    test=[2,4,4,1,2]
    print(find_duplicates(test))
    test=[]
    print(find_duplicates(test))
    test=[1,2,4,4,1,2]
    print(find_duplicates(test))
    test=[2,32,2,2,3,4,4,56,6,6,6,4,4,1,2]
    print(find_duplicates(test))
    test=[2]
    print(find_duplicates(test))
    test=[2,2,2,2]
    print(find_duplicates(test))
