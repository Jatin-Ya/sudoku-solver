#sudoku solving program


#block = [[8,2,7,1,5,4,3,9,6],[9,6,5,3,2,7,1,4,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]]

block = [[0,2,7,1,5,4,3,9,0],[0,6,5,3,2,7,1,0,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]]
#block=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

#block = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
#block = [[8,2,7,1,5,4,3,9,6],
#	[9,6,5,3,2,7,1,4,8],
#	[3,4,1,6,8,9,7,5,2],
#	[5,9,3,4,6,8,2,7,1],
#	[4,7,2,5,1,3,6,8,9],
#	[6,1,8,9,7,2,4,3,5],
#	[7,8,6,2,3,5,9,1,4],
#	[1,5,4,7,9,6,8,2,3],
#	[2,3,9,8,4,1,5,6,7]]


def next_empty(block):
	"""input : block   --finds next empty box that is to be filled""" 
	for m in range (0,9):
		for l in range (0,9):
			if block[m][l]==0:
				return (m,l)
def check(block,i,j,k):
	"""checks if k is filled in the block at position i,j then will there be a conflict"""
	for m in range (0,9):
		if block[m][j]==k:
			return False 
	for m in range (0,9):
		if block[i][m]==k:
			return False
	sector_x=3*(i//3)
	sector_y=3*(j//3)
	for m in range (sector_x,sector_x+3):
		for l in range (sector_y,sector_y+3):
			if block[m][l]==k:
				 return False
	return True
def complete(block):
	"""checks if the block is filled completely"""
	for c in block:
		if 0 in c:
			return False
	return True


def main(block,m,n):
	i,j=0,0
	if not complete(block):
		i,j=next_empty(block)
	if complete(block):
		
		return block
	for k in range (1,10):
		if check(block,i,j,k):
			block[i][j]=k
			m,n=i,j
			block=main(block,m,n)
			if complete(block):
				break
	else:
		block[m][n]=0
		return block			
	if complete(block):
		
		return block
		
result=main(block,0,0)
for i in result:
	print(i)	
				
