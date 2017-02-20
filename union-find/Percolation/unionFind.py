#class for weighted union find
class WeightedUnionFind:
	def __init__(self, N):
		self.count=N
		self.id=list(range(N))
		self.sz=[1]*N

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
		if self.sz[Rp] < self.sz[Rq]:
			self.id[Rp]=Rq
			self.sz[Rq]=self.sz[Rq]+self.sz[Rp]
		else:
			self.id[Rq]=Rp
			self.sz[Rp]=self.sz[Rp]+self.sz[Rq]
		self.count=self.count-1

	def connected(self, p,q):
		return self.root(p)==self.root(q)

