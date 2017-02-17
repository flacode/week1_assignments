"""Returning the largest element from a component containing p
   Successor with delete. Given a set of N integers S={0,1,...,N−1}
and a sequence of requests of the following form:
• Remove x from S
• Find the successor of x: the smallest y in S such that y ≥ x.
Design a data type so that all operations (except construction) should take
logarithmic time or better.

O(MlogN).
Solution.
1.using weighted union-find algorithm with path compression, with an list ie large to keep track of the largest elements
2.for each union, update the value of largest element in that component.
3.Add a method to return largest element in a component


"""
class LargestItemComponent:
	def __init__(self, N):
		self.count=N
		self.id=list(range(N))#initial list of connevted components
		self.sz=[1]*N#initially each component has only one element, itself
		self.large=list(range(N))#list to keep track of the largest element in each connected component.


	def root(self, p):
		while p != self.id[p]:
			self.id[p]=self.id[self.id[p]]
			p=self.id[p]

		return p

	def union(self, p, q):
		Rp=self.root(p)
		Rq=self.root(q)	
		if Rp == Rq:
			return
		if self.sz[Rp]<self.sz[Rq]:
			self.id[Rp]=Rq
			self.sz[Rq]=self.sz[Rq]+self.sz[Rp]
			self.large[Rq]=max(self.large[Rq], self.large[Rp])

		else:
			self.id[Rq]=Rp
			self.sz[Rp]=self.sz[Rp]+self.sz[Rq]
			self.large[Rp]=max(self.large[Rq], self.large[Rp])
		self.count=self.count-1

	def connected(self, p, q):
		return self.root(p)==self.root(q)

	def count_comp(self):
		return self.count

	"""Returns the largest element in the component, where it looks for the value of the root of p in the list large"""
	def largest(self, p):
		return self.large[self.root(p)]



if __name__=="__main__":
	files=['tinyUF.txt']
	print ("\tCount  largestP  largestQ")
	for file_name in files:
		with open(file_name, 'r') as f:
			n=f.readline()
			uf=LargestItemComponent(int(n))
			while n:
				n=f.readline()
				c=n.strip().split(' ')
				if c != ['']:
					p=int(c[0])
					q=int(c[1])
					print ("Before",  end='\t'),
					print (uf.count_comp(),  end='\t')
					print (uf.largest(p),  end='\t')
					print (uf.largest(q))
					if not uf.connected(p, q):
						uf.union(p, q)
					print ("After",  end='\t'),
					print (uf.count_comp(),  end='\t')
					print (uf.largest(p),  end='\t')
					print (uf.largest(q))						
		f.close()
