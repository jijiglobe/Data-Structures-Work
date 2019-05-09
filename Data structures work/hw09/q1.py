def hash(input):
    return ((125*input+342) % 1009)

def cheat(lst,size):
    ans = []
    for x in range(size):
        ans.append([])
    print(ans)
    for x in lst:
        ans[hash(x) % size].append(x)
    for x in ans:
        print(x)
#lst = [12,56,22,106,36,72,902,86,96,62,42]
#cheat(lst,10)
for x in [59,39,135,91,46,132,169,277]:
    print (x,x%11)
