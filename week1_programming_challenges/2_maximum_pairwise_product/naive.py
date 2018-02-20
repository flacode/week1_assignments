'''Naive implementation which is slower'''
import sys
def MAXPAIRWISEPRODUCTNATIVE(A):
    product = 0
    n=len(A)
    for i in range(n):
        for j in range(n):
            if (i != j):
                if product < A[i]*A[j]:
                    product = A[i]*A[j]
    return product

if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    print(MAXPAIRWISEPRODUCTNATIVE(A))