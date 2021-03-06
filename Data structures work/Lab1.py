from random import randint
def add_binary(num_str, num_str2):
    ans = ""
    longer = num_str
    shorter = num_str2
    if len(num_str) < len(num_str2):
        longer = num_str2
        shorter = num_str
    for i in range(len(longer)-len(shorter)):
        shorter = "0" + shorter
    carried = False
    #print("adding: " + shorter + " " + longer)
    index = 1
    while index <= len(longer):
        sumDigits = int(shorter[index * -1]) + int(longer[index * -1])
        if sumDigits == 0:
            if carried:
                ans = "1" + ans
            else:
                ans = "0" + ans
            carried = False
        if sumDigits == 1:
            if carried:
                ans = "0" + ans
            else:
                ans = "1" + ans
        if sumDigits == 2:
            if carried:
                ans = "1" + ans
            else:
                ans = "0" + ans
                carried = True
        index += 1
        #print("current: " + ans)
    if carried:
        ans = "1" + ans
    #ans = longer[0: -1 * len(shorter) + 1] + ans
    return ans

def testBinary():
    print(add_binary("111","111"))
    print(add_binary("11","1"))
    print(add_binary("1001","1"))

def can_construct(ransom_note, magazine):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if ransom_note.count(letter) > magazine.count(letter):
            return False
    return True

def test_construct():
    print(can_construct("aa", "ab"))
    print(can_construct("aa", "aba"))
    print(can_construct("aabbcc", "ababccccc"))
    print(can_construct("aabbcc", "ababc"))
    print(can_construct("aabbbbcccc", "abcdefgabcdefgabcdefgabcdefg"))

def create_permutation(n):
    ans = []
    for x in range(n):
        ans.insert(randint(0,len(ans)),x)
    return ans

def testPerm():
    for x in range(10):
        print(create_permutation(x))
        print(create_permutation(x))
        print(create_permutation(x))

def scramble_word(word):
    ans = ""
    perm = create_permutation(len(word))
    for x in range(len(perm)):
        ans += word[perm[x]]
    return ans

def testScram():
    print(scramble_word("pokemon"))
    print(scramble_word("pokemon"))
    print(scramble_word("pokemon"))
    print(scramble_word("pokemon"))
    print(scramble_word("pokemon"))
    print(scramble_word("pokemon"))

#testScram()
#testPerm()
#testBinary()
#test_construct()
