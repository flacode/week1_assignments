"""Returning the largest element from a component"""
class LargestItemComponent:
	def __init__(self, N):
		self.count=N
		self.id=list(range(N))
		self.sz=[1]*N
		self.large=list(range(N))


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
