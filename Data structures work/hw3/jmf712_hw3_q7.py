def flat_list(lst,low=0,high=-1):
    if high == -1:
        high = len(lst)
    ans = []
    for index in range(low,high):
        if(isinstance(lst[index],list)):
            ans+=flat_list(lst[index])
        else:
            ans.append(lst[index])
    return ans
test = [[1, 2], 3, [4, [5, 6, [7], 8]]]
print(test)
print(flat_list(test))
