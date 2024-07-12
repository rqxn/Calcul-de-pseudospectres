import numpy as np
import PredictionCorrection
import matplotlib.pyplot as plt
import scipy
import math

#Algo Criss-Cross pour l'abscisse du pseudospectre (sup Re z, z dans le pseudospectre)

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A


def rayonmax(A):
    vaps = np.linalg.eig(A)[0]
    maxi = vaps[0]
    for v in vaps:
        if np.abs(v) > np.abs(maxi):
            maxi = v
    return maxi


def ValeurSinguliereMax(A, n, theta, epsilon, tol):
    matAugmentee = np.block([
        [1j*np.exp(1j*theta)*A.conjugate().T, -epsilon * np.identity(n)],
        [epsilon * np.identity(n), 1j*np.exp(-1j*theta)*A]
    ])
    vaps = np.linalg.eig(matAugmentee)[0]
    maxvap = max([x.imag for x in vaps if np.abs(x.real) < tol])
    print(maxvap)
    return maxvap



def CrissCrossRadius(A, n, epsilon, tol):
    z1 = rayonmax(A)
    theta = np.angle(z1)

    r = ValeurSinguliereMax(A, n, theta, epsilon, tol)

    i = 0
    while i < 10:
        rayons = np.array([r], dtype=np.float64)
        C = np.block([
            [-epsilon * np.identity(n), A],
            [r * np.identity(n), np.zeros((n,n))]
        ])
        B = np.block([
            [np.zeros((n,n)), r * np.identity(n)],
            [A.conjugate().T, -epsilon * np.identity(n)]
        ])

        eigs = scipy.linalg.eig(C, B)[0]

        k = 0
        l = len(eigs)
        midpoints = np.array([], dtype=np.float64)
        print(l)
        while 2*k+1 < l:
            thetamid = np.angle(eigs[2*k] * eigs[2*k+1])/2
            k += 1
            midpoints = np.append(midpoints, thetamid)

        for m in midpoints:
            print("test")
            rayons = np.append(rayons, ValeurSinguliereMax(A, n, m, epsilon, tol))
        r = max(rayons)
        i += 1
    return r

    


   
    
            
A = creerMat(10)
fig, ax = plt.subplots()
print(CrissCrossRadius(A, 10, 0.01, 0.0005))

PredictionCorrection.PredCorr(ax, A, 10, 0.01, 0.0001, 0.005)

        