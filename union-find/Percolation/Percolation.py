#class for weighted union find
#class for Percolation


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

			
class Percolation:
	def __init__(self, grid):
		self.rows=len(grid)
		self.cols=len(grid[0])
		self.grid_size=self.rows*self.cols
		self.top=self.grid_size
		self.bottom=self.grid_size+1
		self.grid=grid
		v=0
		self.vgrid=[]
		for i in range(self.rows):
			self.vgrid.append([])
			for j in range(self.cols):
				self.vgrid[i].append(v)
				v=v+1
		self.uf=WeightedUnionFind(self.grid_size+2) # 2 for the two extra nodes for top and bottom


	"""If cell is valid and it is open"""
	def check_neighbors(self, i, j):
		if i==0:
			self.uf.union(self.vgrid[i][j], self.top)
		if i==self.rows-1:
			self.uf.union(self.vgrid[i][j], self.bottom)
		if i-1>=0 and self.grid[i-1][j]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i-1][j])
		if i+1< self.rows and self.grid[i+1][j]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i+1][j])
		if j-1 >=0 and self.grid[i][j-1]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i][j-1])
		if j+1 < self.cols and self.grid[i][j+1]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i][j-1])

	def discover(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.grid[i][j]=='1':
					self.check_neighbors(i, j)
					

	def percolates(self):
		if self.uf.connected(self.top, self.bottom):
			print ("It Percolates!!!")
		else:
			print ("It does not percolate ;(")
		
		 
def main():
	file_name='test.txt'
	with open(file_name, 'r') as f:
		n=f.readline()
		while n:
			size=n.strip().split(' ')
			row_len=int(size[0])
			col_len=int(size[1])
			grid=[[0 for j in range(col_len)] for i in range(row_len)]
			for i in range(row_len):
				line=f.readline()
				grid[i]=line.strip().split(' ')
			break
				
	f.close()
	land=Percolation(grid)
	land.discover()
	land.percolates()
					
main()
			

		

