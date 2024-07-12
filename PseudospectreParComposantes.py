import numpy as np
import matplotlib.pyplot as plt
import math
import GRID as g
def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def rayspec(A):
  return max(np.absolute(np.linalg.eigvals(A)))

def f(x, y, A, n, E):
    X = np.linalg.inv(A - (x+1j*y)*np.identity(n))
    X = np.absolute(X)
    Y = np.matmul(X, E)
    r = rayspec(Y)
    return r

def affichage(ax, n, A, epsilon, nbPoints):

    R = [math.sqrt(n)*epsilon + np.sum(np.abs(A[i, :])) for i in range(n)]
    centers = np.diag(A)
    E = np.absolute(A)
    x = np.array([])
    y = np.array([])
    seen = set()
    for i in range(n):
        re = centers[i].real
        im = centers[i].imag
        leftbound = re - R[i]
        rightbound = re + R[i]
        upperbound = im + R[i]
        lowerbound = im - R[i]
        arrx = np.linspace(leftbound, rightbound, nbPoints)
        arry = np.linspace(lowerbound, upperbound, nbPoints)
        X, Y = np.meshgrid(arrx, arry)
        Z = np.empty_like(X, dtype=float)
        
        for k in range(nbPoints):
            for j in range(nbPoints):
                if (k, j) not in seen:
                    Z[j, k] = f(X[j, k], Y[j, k], A, n, E)
                    seen.add((k,j))
                else:
                    Z[j, k] = 0
               

        C = 1/epsilon
        ax.contour(X, Y, Z, levels=[C], colors=['green'])
        ax.set_xlabel('Reels')
        ax.set_ylabel('Imaginaires')
        ax.set_title('Contour du pseudo-spectre par composantes')
        ax.grid(True)