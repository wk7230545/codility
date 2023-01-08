def solution(A, K):
    n = len(A)
    newlist = [0] * n
    for i in range (0, n):
        newlist[(i+K)%n] = A[i]
    return newlist
