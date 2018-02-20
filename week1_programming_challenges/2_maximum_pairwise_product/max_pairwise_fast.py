def MAXPAIRWISEFAST(A):
    index_1 = 0
    n = len(A)
    for i in range(1, n):
        if A[i]>A[index_1]:
            index_1 = i
    if index_1 == 0: index_2 = 1
    else: index_2 = 0
    for i in range(1, n):
        if (A[i]>A[index_2]) and (i != index_1):
            index_2 = i
    return A[index_1]*A[index_2]

if __name__ == '__main__':
    # n = input()
    A = [int(x) for x in input().split()]
    # assert (len(A) == n)

    print(MAXPAIRWISEFAST(A)) 