from unionFind import WeightedUnionFind #import unionFind class
#class for Percolation

			
class Percolation:
	def __init__(self, grid):
		self.rows=len(grid)#number of rows in grid
		self.cols=len(grid[0])#number of columns in grid
		self.grid_size=self.rows*self.cols#number of cells in the entire grid
		self.top=self.grid_size #virtual node to represent top
		self.bottom=self.grid_size+1 #virtual node to represent bottom
		self.grid=grid
		"""Mark cells in a virtual grid with numbers from 0 to gridsize-1""" 
		v=0
		self.vgrid=[]
		for i in range(self.rows):
			self.vgrid.append([])
			for j in range(self.cols):
				self.vgrid[i].append(v)
				v=v+1
		self.uf=WeightedUnionFind(self.grid_size+2) # 2 for the two extra nodes for top and bottom


	"""If cell is valid and it is open, check if any of its neighbors are open and connect the two cells"""
	def check_neighbors(self, i, j):
		if i==0:#if the cell is in the top row, connect it to the virtual top 
			self.uf.union(self.vgrid[i][j], self.top)
		if i==self.rows-1:#if cell is in the last row, connect it to the virtual bottom
			self.uf.union(self.vgrid[i][j], self.bottom)
		if i-1>=0 and self.grid[i-1][j]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i-1][j])
		if i+1< self.rows and self.grid[i+1][j]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i+1][j])
		if j-1 >=0 and self.grid[i][j-1]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i][j-1])
		if j+1 < self.cols and self.grid[i][j+1]=='1':
			self.uf.union(self.vgrid[i][j], self.vgrid[i][j-1])

	"""Check the grid for open cells and connect them to their neighbors"""	
	def discover(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.grid[i][j]=='1':
					self.check_neighbors(i, j)
					
	"""Check if the virtual top is connected to the virtual bottom"""
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
			

		

