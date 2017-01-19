"""Here, the trees can get too tall, therefore find is expensive. In union, the change is applied only when there is need.
   Keep track of the size of the tree, such that the tree can be balanced by adding the small tree to the root of the bigger tree
"""
import time
class QuickUnionUF:
	def __init__(self, N):
		self.count=N
		self.id=list(range(self.count))#list of trees(forest)
		self.sz=[1]*N#number of sites in each tree
	
	#find the root of a site
	def find(self, i):
		while i != self.id[i]:
			i=self.id[i]
		return i

	def connected(self, p, q):
		return self.find(p)==self.find(q) # compare the roots of the two sites

	def union(self, p, q):
		Rp=self.find(p)
		Rq=self.find(q)
		if Rp == Rq:
			return
		if self.sz[Rp]<self.sz[Rq]:
			self.id[Rp]=Rq
			self.sz[Rq]=self.sz[Rq]+self.sz[Rp]
		else:
			self.id[Rq]=Rp
			self.sz[Rp]=self.sz[Rp]+self.sz[Rq]
		self.count=self.count-1

	def no_of_components(self):
		return self.count



if __name__=="__main__":
	files=['tinyUF.txt', 'mediumUF.txt', 'largeUF.txt']
	for file_name in files:
		start_time=time.time()
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
		end_time=time.time()
		print ("The number of components is %d" %(uf.no_of_components()))
		print ("The elapsed time for %s is %s" %(file_name, (end_time-start_time)))
	
