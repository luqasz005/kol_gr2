#!/usr/bin/env python2.6

class Matrix:
	def __init__(self,a,b,c,d):
		self.a1 = a
		self.a2 = b
		self.b1 = c
		self.b2 = d
	
	def add(self,matrix):
		#return Matrix(self.a1 + matrix.a1,self.a2 + matrix.a2,self.b1 + matrix.b1,self.b2 + matrix.b2)
		self.a1 += matrix.a1
		self.a2 += matrix.a2
		self.b1 += matrix.b1
		self.b2 += matrix.b2		

	def __print__(self):
		print(self.a1,self.a2)
		print('\n')
		print(self.b1,self.b2)

def printM(mat):
	print(mat.a1,mat.a2)
	print(mat.b1,mat.b2)

matrix_1 = Matrix(4,5,6,7)
printM(matrix_1)
matrix_2 = Matrix(2,2,2,1)
printM(matrix_2)

matrix_3 = matrix_2.add(matrix_1)			
#printM(matrix_3)		

	
	
