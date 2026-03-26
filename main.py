import threading
import math
import time
import os

class p3:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z



camPos = p3(0,0,0)
angleA = 6
angleB = 0


cube = [ p3(-1,-1,-1), p3(1,-1,-1), p3(1,1,-1), p3(-1,1,-1),p3(-1,-1, 1), p3(1,-1, 1), p3(1,1, 1), p3(-1,1, 1) ];
edges = [[0,1], [1,2], [2,3], [3,0], [4,5], [5,6], [6,7], [7,4], [0,4], [1,5], [2,6], [3,7]]

yDisplay = 30
xDisplay = 100



mat = [[' ' for x in range(xDisplay)] for y in range (yDisplay) ]

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

	m = p3(p.x - camPos.x, p.y - camPos.y, p.z - camPos.z)


	n1 = m
	n1.x = m.x * math.cos(angleA) - m.z * math.sin(angleA)
	n1.z = m.x * math.sin(angleA) + m.z * math.cos(angleA)

	n2 = p3(0,0,0)

	n2.x = n1.x
	
	n2.z = n1.z * math.cos(angleB) + n1.y * math.sin(angleB) 
	n2.y = n1.y*math.cos(angleB) - n1.z * math.sin(angleB)

	n = n2

	if (n.z < 0):
		return p3(-1,-1,-1)
	return p3(xDisplay/2 + (n.x * 60) / n.z,yDisplay/2 + (n.y * 40 / n.z),0)


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

	if dlugoscX < 1:
		dlugoscX = 1;

	stepY = dlugoscY/dlugoscX

	yCounter =  tab[0].y

	for x in range(int(dlugoscX)):
		if ((int(yCounter) >= 0 and int(tab[0].x) + int(x) >=0 and int(yCounter) < yDisplay and int(tab[0].x) + int(x) < xDisplay) ):
			mat[int(yCounter)][int(tab[0].x) + int(x)] = '#'

		p = 1
		if stepY < 0:
			p=-1

		for i in range(int(math.fabs(stepY))):
			if (int(tab[0].x) + int(x) >= 0 and int(yCounter) + i*p >=0 and int(yCounter) + i*p < yDisplay and int(tab[0].x) + int(x) < xDisplay):
				mat[int(yCounter) + i*p ][int(tab[0].x) + int(x)] = '#'

		yCounter+=stepY

def main():
	global angleA
	global angleB
	while True:
		#angleB+=0.02
		#angleA+=0.02

		for i in range(12):
			p1 = projection(p3(cube[edges[i][0]].x,cube[edges[i][0]].y,cube[edges[i][0]].z+6))
			p2 = projection(p3(cube[edges[i][1]].x,cube[edges[i][1]].y,cube[edges[i][1]].z+6))


			if (False == (p1.z < 0 or p2.z < 0)):
				drawnLine(p1,p2)

		spriningCube()

		for y in range(yDisplay):
			for x in range(xDisplay):
				print(mat[y][x],end="")
				mat[y][x] = ' '
			print("")

		print("Kat A ",angleA,".Kat B ",angleB,".")
		print("x: ", camPos.x, "y: ", camPos.y, "z: ", camPos.z)
		time.sleep(0.03)
		os.system('cls')


main()

