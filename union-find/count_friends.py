"""Attempting hackerearth practice problem https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/count-friends/"""



"""Find the friend on top of the chain"""
def root(roots, a):
    while a != roots[a]:
            roots[a]=roots[roots[a]]
            a=roots[a]
    return a
    
    
"""Make 2 students friends"""  
def make_friends(roots, size, a, b):
    root_a=root(roots, a)
    root_b=root(roots, b)
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            roots[root_a]=root_b
            size[root_b]=size[root_a]+size[root_b]
        else:
            roots[root_b]=root_a
            size[root_a]=size[root_b]+size[root_a]
"""Find the number of friends in each root relationship"""   
def no_of_friends(roots, size):
    friends=[0]*len(roots)
    for i in range(len(roots)):
        root_i=root(roots, i)
        friends[i]=size[root_i]-1
    return friends
    
if __name__=="__main__":
    A=input()
    A=A.strip().split(' ')
    N=int(A[0])
    M=int(A[1])
    roots=list(range(N)) #the student is a friend of himself or herself
    size=[1]*N #size of each student's circle of friends initially
    for i in range(M):
        uv=input()
        uv=uv.strip().split(' ')
        u=int(uv[0])-1
        v=int(uv[1])-1
        make_friends(roots, size, u, v)
    no_of_friends=map(str, no_of_friends(roots, size))
    print (' '.join(no_of_friends))
        
            
