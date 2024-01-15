#!/bin/python

from numpy import *
from timeit import *
from numpy.linalg import *
from numpy.random import *


n = 10000

def randomMatrix():
	global A, b, n

	A = random((n, n))
	b = random(n)

print(f"Time to generate a random matrix and vector: {timeit(randomMatrix, number = 1)} seconds")



def solveLinearSystem():
	global  b, x

	x = solve(A, b)

print(f"Time to solve the linear system: {timeit(solveLinearSystem, number = 1)} seconds")



def findEigenValuesAndVectors():
	global A, eig_A, eig_V

	eig_A, eig_V = eig(A)

print(f"Time to find eigenvalues and eigenvectors of the matrix: {timeit(findEigenValuesAndVectors, number = 1)} seconds")




def findSVD():
	global A, svd_A

	svd_A = svd(A)

print(f"Time to find SVD of the matrix: {timeit(findSVD, number = 1)} seconds")
