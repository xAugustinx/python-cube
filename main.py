import math
import time
import os

class p3:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z


cube = [ p3(-1,-1,-1), p3(1,-1,-1), p3(1,1,-1), p3(-1,1,-1),p3(-1,-1, 1), p3(1,-1, 1), p3(1,1, 1), p3(-1,1, 1) ];

edges = [[0,1], [1,2], [2,3], [3,0], [4,5], [5,6], [6,7], [7,4], [0,4], [1,5], [2,6], [3,7]]

yDisplay = 30
xDisplay = 100

def spriningCube():
	global cube
	for i in range(8):
		pz = cube[i].z
		cube[i].z = cube[i].z * math.cos(0.05) - cube[i].x * math.sin(0.05)
		cube[i].x = pz * math.sin(0.05)+cube[i].x * math.cos(0.05)
		pz = cube[i].y
		cube[i].y=cube[i].y * math.cos(0.05) - cube[i].x * math.sin(0.05)
		cube[i].x=pz * math.sin(0.05)+cube[i].x * math.cos(0.05)

def projection(p):
	return p3(xDisplay/2 + (p.x * 60) / p.z,yDisplay/2 + (p.y * 40 / p.z),0) 


def drawnLine(p1,p2):
	tab = []
	if p1.x < p2.x:
		tab.append(p1)
		tab.append(p2)
	else:
		tab.append(p2)
		tab.append(p1)

	dlugoscX = tab[1].x - tab[0].x
	dlugoscY = tab[1].y - tab[0].y

	if dlugoscX == 0:
		dlugoscX = 1;

	stepY = dlugoscY/dlugoscX

	yCounter =  tab[0].y
	
	for x in range(int(dlugoscX)):
		mat[int(yCounter)][int(tab[0].x) + int(x)] = '#'

		p = 1
		if stepY < 0:
			p=-1

		for i in range(int(math.fabs(stepY))):
			mat[int(yCounter) + i*p ][int(tab[0].x) + int(x)] = '#'

		yCounter = yCounter + stepY
		


while True:
	mat = [[' ' for x in range(xDisplay)] for y in range (yDisplay) ]

	

	for i in range(12):

		new = p3(cube[edges[i][0]].x,cube[edges[i][0]].y,cube[edges[i][0]].z+5)
		
		p1 = projection(p3(cube[edges[i][0]].x,cube[edges[i][0]].y,cube[edges[i][0]].z+5))
		p2 = projection(p3(cube[edges[i][1]].x,cube[edges[i][1]].y,cube[edges[i][1]].z+5))

		if (p1.x >= 0 and p1.y >=0 and p1.y < yDisplay and p1.x < xDisplay):
			mat[int(p1.y)][int(p1.x)] = '#'
			drawnLine(p1,p2)

	spriningCube()

	for y in range(yDisplay):
		for x in range(xDisplay):
			print(mat[y][x],end="")
		print("")
		
	mat.clear()
	time.sleep(0.03)
	os.system('cls')	

