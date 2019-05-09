import os
def is_palindrome(input_str, low= 0, high = -1):
    if high == -1:
        high = len(input_str)-1
    if low == high:
        return True
    if input_str[low] == input_str[high]:
        if low-high == 1:
            return True
        else:
            return is_palindrome(input_str, low+1, high-1)
    return False

def test_palindrome():
    case = "kayak"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))
    case = "aabbccbbaa"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))
    case = "aba"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))
    case = "a"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))
    case = "python"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))
    case = "java"
    print(("testing:2 %s\nresult:  %s\n")% (case, is_palindrome(case)))

def binary_search(srt_lst, val, low = 0, high = -1):
    if high == -1:
        high = len(srt_lst)-1
    if low == high:
        return None
    index = int((low + high) / 2)
    if srt_lst[index] == val:
        return index
    if srt_lst[index] < val:
        return binary_search(srt_lst,val,index,high)
    else:
        return binary_search(srt_lst,val,low,index)

def test_search():
    print("testing search...\n")
    case = [1,2,3,4,5,6,7,8,9,10]
    for x in range (10,20):
        case.append(x)
        print(("seaching %s for %s\nresult:  %s\n")% (case,x-5, binary_search(case,x-5)))

def decimal_to_binary(input_int):
    if input_int == 0:
        return "0"
    if input_int == 1:
        return "1"
    return decimal_to_binary(int(input_int / 2)) + str(input_int % 2)

def binaryHelper():
    print("testing Binary...\n")
    for x in range(30):
        print("Decimal: %d\n binary: %s" % (x, decimal_to_binary(x)))

def move(frm, to):
    print("move disk from %s to %s" % (frm,to))

def solve_hanoi(n, frm, to, extra):
    #The Flaw in the stated method is that it will eventually cause mis-stacked disks
    if n==1:
        move(frm,to)
    else:
        solve_hanoi(n-1,frm,extra,to)
        move(frm,to)
        solve_hanoi(n-1,extra,to,frm)

def test_hanoi():
    solve_hanoi(3,"A","C","B")

def disk_usage(path):
    if os.path.isdir(path):
        size =  os.path.getsize(path)
        for subpath in os.listdir(path):
            size += disk_usage(os.path.join(path,subpath))
        return size
    return os.path.getsize(path)

def subDirs(path):
    print(path)
    if os.path.isdir(path):
        size =  os.path.getsize(path)
        for subpath in os.listdir(path):
            size += subDirs(os.path.join(path,subpath))
        return size
    return os.path.getsize(path)

def test_usage():
    print("testing usage...\n")
    print("size of Data Structures Directory %s" % (disk_usage("/Users/jionfairchild/Data-Structures")))

def test_subpath():
    print("testing subpath...\n")
    print("subpaths of Data Structures Directory...")
    subDirs('/Users/jionfairchild/Blizzard')
test_usage()
test_subpath()
