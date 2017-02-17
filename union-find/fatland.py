"""Fatland is a town that started with N distinct empires, namely empires 1, 2, ..., N. But over time, the armies of some of these empires have taken over other ones. Each takeover occurred when the army of empire i invaded empire j. After each invasion, all of empire j became part of empire i, and empire j was renamed as empire i.

Empire Huang, leader of Badland, wants to invade Fatland. To do this, he needs to calculate how many distinct empires still remain in Fatland after all the takeovers. Help him with this task.

Input:

The first line contains an integer N, the number of empires that were originally in Fatland.

The second line contains an integer K, denoting the number of takeovers that took place.

Each of the next K lines contains 2 space-separated integers i, j, representing that the army of empire i took over that of empire j. As a result, empire j does not exist anymore and is now renamed as empire i. It is guaranteed that empire i still exists.

Output: Output one integer, the number of empires that exist in Fatland.

Constraints:

1 <= N <= 105

1 <= K <= 105

https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-flood-1/

Solution.
1.using weighted union find with path compression, print the number of connected components

"""
class Fatland:
    def __init__(self, N):
        self.count=N #variable used to keep track of the number of empires in fatland. 
        self.empires=list(range(N))
        self.sz=[1]*N
        
    def root(self, p):
        while p != self.empires[p]:
            self.empires[p]=self.empires[self.empires[p]]#path compression
            p=self.empires[p]
        return p
        
    def union(self, p, q):
        Rp=self.root(p)
        Rq=self.root(q)
        if Rp==Rq:
            return
        if self.sz[Rp]<self.sz[Rq]:
            self.empires[Rp]=Rq
            self.sz[Rq]=self.sz[Rq]+self.sz[Rp]
        else:
            self.empires[Rq]=Rp
            self.sz[Rp]=self.sz[Rp]+self.sz[Rq]
        self.count=self.count-1 #after each connection, we subtract one from the number of connected components
        
    def no_of_empires(self):
        return self.count
        
        
if __name__=="__main__":
    N=int(input())
    k=int(input())
    town=Fatland(N)
    for i in range(k):
        army=input().strip().split(' ')
        town.union(int(army[0])-1, int(army[1])-1)
    print (town.no_of_empires())
            
    
            
