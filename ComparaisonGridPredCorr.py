import PredictionCorrection
import GRID
import time
import matplotlib.pyplot as plt

def mesure_temps_executionGRID(n, A):
    debut = time.time()
    GRID.affichage(n, A, 0.1, 500)
    fin = time.time()
    return fin - debut

def mesure_temps_executionPredCorr(n, A):
    debut = time.time()
    PredictionCorrection.PredCorr(A, n, 0.1, 0.01, 0.05)
    fin = time.time()
    return fin - debut

def comparer_temps_execution(n_min, n_max):
    tailles = list(range(n_min, n_max + 1))
    temps1 = []
    temps2 = []

    for n in tailles:
        A = GRID.creerMat(n)
        temps1.append(mesure_temps_executionGRID(n, A))
        temps2.append(mesure_temps_executionPredCorr(n, A))
        print(n)

    return tailles, temps1, temps2

def afficher_graphe(tailles, temps1, temps2):
    plt.plot(tailles, temps1, label='GRID')
    plt.plot(tailles, temps2, label='Prediction Correction')
    plt.xlabel('Taille n')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des temps d\'exécution')
    plt.legend()
    plt.show()

n_min = 5
n_max = 35

tailles, temps1, temps2 = comparer_temps_execution(n_min, n_max)
afficher_graphe(tailles, temps1, temps2)
