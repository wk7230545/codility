'''
BinaryGap
Find longest sequence of zeros in binary representation of an integer.

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''
'''
Solution Algorithm
10001001000001
- read the sequence
- increment a counter variable for each zero digit
- reset counter every time when '1' is reached
- compare zero counter with the current maximum value
'''

N = int(input('Please input a number: '))
binrep = bin(N)[2:]

def solution(N): 
    counter = 0
    maxcounter = 0
    for k in binrep:
        if int(k) == 0:
            counter += 1
        elif int(k) == 1:
            maxcounter = max(counter, maxcounter)
            counter = 0
    return maxcounter


print(f'The binary representation of {N} is {binrep}')
print(f'The binary gap is {solution(N)}')
