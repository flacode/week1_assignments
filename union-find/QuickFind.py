"""This algorithm is flat, but it is expensive to keep trees flat in union. N^2 array accesses
   Change all objects whise id equals to id[p] to id[q]
"""

class QuickFindUF:
	def __init__(self, N):
		self.count=N #initial number of components
		self.id=list(range(N)) #list of components

	def no_of_components(self):
		return self.count

	def connected(self, p, q):#can also be called find
		return self.id[p] == self.id[q]

	def union(self, p, q):
		pId=self.id[p]
		qId=self.id[q]
		for i in range(len(self.id)):
			if self.id[i]==pId:
				self.id[i]=qId
		self.count=self.count-1 #has to be outside the loop because only two components merged to make 1
	
if __name__=='__main__':
	files=['tinyUF.txt', 'mediumUF.txt', 'largeUF.txt']
	for file_name in files:
		with open(file_name, 'r') as f:
			n=f.readline()
			uf=QuickFindUF(int(n))
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
