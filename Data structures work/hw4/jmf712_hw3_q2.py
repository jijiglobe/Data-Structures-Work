import copy
def permutations(lst,low,high):
    if low>= high:
        return [[lst[low]]]
    ans = []
    perms = permutations(lst,low+1,high)
    for perm in perms:
        for index in range(len(perm)+1):
            permCopy = copy.copy(perm)
            permCopy.insert(index,lst[low])
            ans.append(permCopy)
    return ans

