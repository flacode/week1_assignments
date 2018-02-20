# Uses python3
n = int(input())
A = [int(x) for x in input().split()]
assert(len(A) == n)

result = 0
index = 0
for i in range(1, n):
    if A[i] > A[index]:
        index = i
A[index], A[n-1] = A[n-1], A[index]

index=0
for j in range(1, n-1):
    if A[j] > A[index]:
        index = j
A[index], A[n-2] = A[n-2], A[index]
result = A[n-2]*A[n-1]

print(result)

