import numpy as np
import matplotlib.pyplot as plt
import math

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def svmin(x, y, A, n):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def affichage(ax, n, A, epsilon, nbPoints):

    R = [math.sqrt(n)*epsilon + np.sum(np.abs(A[i, :])) for i in range(n)]
    centers = np.diag(A)

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
                    Z[j, k] = svmin(X[j, k], Y[j, k], A, n)
                    seen.add((k,j))
                else:
                    Z[j, k] = 1000

        C = epsilon
        ax.contour(X, Y, Z, levels=[C], colors=['red'])
        ax.set_xlabel('Reels')
        ax.set_ylabel('Imaginaires')
        ax.set_title('Contour du pseudo-spectre')
        ax.grid(True)

