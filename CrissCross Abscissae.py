import numpy as np
import PredictionCorrection
import matplotlib.pyplot as plt
import math

#Algo Criss-Cross pour l'abscisse du pseudospectre (sup Re z, z dans le pseudospectre)

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def svmin(A, n, x, y):
    S = np.linalg.svd(np.identity(n)*(x + 1j*y) - A, compute_uv=False)
    return S[n-1]

def rightmostVap(A):
    vaps = np.linalg.eig(A)[0]
    rmVap = max(vaps, key = lambda x: x.real)
    return rmVap 

def ValeurSinguliereHorizontale(A, n, y, epsilon, tol):
    matAugmentee = np.block([
        [-y * np.identity(n) + 1j*A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), 1j*A + y * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    maxvap = max([x.imag for x in vaps if np.abs(x.real) < tol])
    return maxvap

def ValeurSinguliereVerticale(A, n, x, epsilon, tol):
    Y = np.array([], dtype=np.float64)
    matAugmentee = np.block([
        [x * np.identity(n) - A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), A - x * np.identity(n)]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    for vap in vaps:
        if np.abs(vap.real) < tol:
            if np.abs(svmin(A, n, x, vap.imag) - epsilon) < tol:
                Y = np.append(Y, vap.imag)
    return Y


def CrissCrossAbscisse(n, A, epsilon, tol):
    z1 = rightmostVap(A)
    #etape 2
    x = z1.imag
    i = 0 
    midpoints = np.array([x], dtype=np.float64)
    X = np.array([], dtype=np.float64)
    Y = np.array([z1.imag], dtype=np.float64)

    while i < 10: 
        X = np.array([], dtype=np.float64)
        for x in midpoints:
            X = np.append(X, ValeurSinguliereHorizontale(A, n, x, epsilon, tol))
        
        nvx = X[0]
        nvy = Y[0]
        for j in range(len(X)):
            if X[j] > nvx:
                nvx = X[j]
                nvy = Y[j]

        z1 = nvx + 1j*nvy.imag
        zk = z1

        #etape 3: intersections verticales basses
        
        Y = np.append([] , ValeurSinguliereVerticale(A, n, zk.real, epsilon, tol))
        Y.sort()
        zk = z1

        l = len(Y)
        midpoints = np.array([], dtype = np.float64)
        k = 0
        while(2*k+1 < l):
            midpoints = np.append(midpoints, (Y[2*k] + Y[2*k + 1]) / 2)
            k+=1
        i += 1
        if (l == 1):
            return nvx
    return X[0]
            
