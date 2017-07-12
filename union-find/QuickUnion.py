"""Here, the trees can get too tall, therefore find is expensive. In the union method, the change is applied only when there is need."""
class QuickUnionUF:
	def __init__(self, N):
		self.count=N
		self.id=list(range(self.count))#list of trees
	
	#find the root of a site
	def root(self, i):
		while i != self.id[i]:
			i=self.id[i]
		return i

	def connected(self, p, q):
		return self.root(p)==self.root(q) # compare the roots of the trees of the two sites

	def union(self, p, q):
		Rp=self.root(p)
		Rq=self.root(q)
		self.id[Rp]=Rq
		self.count=self.count-1

	def no_of_components(self):
		return self.count


if __name__=="__main__":
	files=['tinyUF.txt', 'mediumUF.txt', 'largeUF.txt']
	for file_name in files:
		with open(file_name, 'r') as f:
			n=f.readline()
			uf=QuickUnionUF(int(n))
			while n:
				n=f.readline()
				c=n.strip().split(' ')
				if c != ['']:
					p=int(c[0])
					q=int(c[1])
					if not uf.connected(p, q):
						uf.union(p, q)
		f.close()
		print ("The number of connected components is %d" %(uf.no_of_components()))
	
