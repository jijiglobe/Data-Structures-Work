from random import randint
def count_lowercase(lst, low=0, high=-1):
    if(len(lst) < 1):
        return 0
    if high == -1:
        high = len(lst)-1
    if low == high:
        if lst[low].islower():
            return 1
        return 0
    else:
        return count_lowercase(lst,low,int((low+high)/2)) + count_lowercase(lst,int((low+high)/2)+1,high)

def is_number_of_lowercase_even(lst, low=0, high=-1):
    if(len(lst) < 1):
        return True
    if high == -1:
        high = len(lst)-1
    if low == high:
        if lst[low].islower():
            return False
        return True
    else:
        return is_number_of_lowercase_even(lst,low,int((low+high)/2)) == is_number_of_lowercase_even(lst,int((low+high)/2)+1,high)

