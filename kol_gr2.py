#!/usr/bin/env python2.6


class Matrix(object):
        def __init__(self, val1,val2, val3, val4):
                self.a1 = val1
                self.a2 = val2
                self.b1 = val3
                self.b2 = val4

        def add(self, matrix):
                tem1 = self.a1 + matrix.a1
                tem2 = self.a2 + matrix.a2
                tem3 = self.b1 + matrix.b1
                tem4 = self.b2 + matrix.b2
                return Matrix(tem1, tem2, tem3, tem4)
        
        def __add__(self, matrix):
                if isinstance(matrix,Matrix):
                        tem1 = self.a1 + matrix.a1
                        tem2 = self.a2 + matrix.a2
                        tem3 = self.b1 + matrix.b1
                        tem4 = self.b2 + matrix.b2
                        return Matrix(tem1, tem2, tem3, tem4)
                else:
                        raise TypeError

        def __str__(self):
                a = (self.a1, self.a2, self.b1, self.b2)
                return '%.f %.f\n%.f %.f\n' % a

matrix_1 = Matrix(4, 5, 6, 7)
print(matrix_1)
matrix_2 = Matrix(2, 2, 2, 1)
print(matrix_2)
matrix_3 = matrix_2.add(matrix_1)
print(matrix_3)
print(matrix_1 + matrix_2)
#print(matrix_1 + 1)

if __name__ == '__main__':
        print("Program Główny")
else:
        print("Importowano")
