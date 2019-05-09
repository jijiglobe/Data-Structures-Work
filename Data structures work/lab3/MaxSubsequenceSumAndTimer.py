import time

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

'''
Linear maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0
    
    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0

    return maxSum, seqStart, seqEnd


'''
Quadratic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


'''
Cubic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd
