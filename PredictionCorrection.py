import numpy as np
import matplotlib.pyplot as plt

#recommandation: n = 10, eps = 0.1, tolerance = 0.001, pas = 0.05

def creerMat(n):
    A = np.random.rand(n, n)*10-5
    return A

def g(z, A, n):
    U, S, V = np.linalg.svd(np.identity(n)*z-A)
    V = V.conjugate().T
    return U, S, V

def h(z, theta, A, n, epsilon):
    return g(z + 1j*theta, A, n)[1][n-1] - epsilon

def PredCorr(ax, n, A, epsilon, tolContour, pas):
    Z = np.array([], dtype=np.float64)
    #trouver le premier point z1 par la methode de Newton
    for j in range(n):
        lambda0 = np.linalg.eig(A)[0][j]
        ax.plot(lambda0.real, lambda0.imag, 'xr')
        theta = epsilon
        d = 1j
        z = lambda0 + d*theta
        U, S, V = g(z, A, n)
        while(np.abs((S[n-1] - epsilon))  >  epsilon * 0.00001):
            z = z - (S[n-1] - epsilon)*d / ((-d*np.vdot(V[:, n-1], U[:, n-1])).real)
            U, S, V = g(z, A, n)
            Z = np.append(Z,  z)
            #newton iterate 
        Z = np.append(Z, z)
        
        #on trouve le point suivant
        rk = d*(np.vdot(V[:,n-1], U[:,n-1]) / np.abs(np.vdot(V[:,n-1], U[:,n-1])))
        zkPred = z + pas*rk
        Uk, Sk, Vk = g(zkPred, A, n)
        zk = zkPred - (Sk[n-1] - epsilon)/(np.vdot(Uk[:,n-1], Vk[:,n-1]))
        Z = np.append(Z, zk)
        
        i = 0
        #puis tous les points suivants tant que l'on est pas revenu a z1
        while(np.abs((zk - z)) > tolContour):
            rk = d*(np.vdot(Vk[:,n-1], Uk[:,n-1]) / np.abs(np.vdot(Vk[:,n-1], Uk[:,n-1])))
            zkPred = zk + pas*rk
            Uk, Sk, Vk = g(zkPred, A, n)
            zk = zkPred - (Sk[n-1] - epsilon) / (np.vdot(Uk[:,n-1], Vk[:,n-1]))
            i += 1 
            Z = np.append(Z, zk)
    Z_real = [z.real for z in Z]
    Z_imag = [z.imag for z in Z]
    ax.plot(Z_real, Z_imag, 'b.')  # 'bo' for blue circles
    ax.set_xlabel('Reels')
    ax.set_ylabel('Imaginaires')
    ax.set_title('Contour du pseudo-spectre')
    ax.grid(True)


