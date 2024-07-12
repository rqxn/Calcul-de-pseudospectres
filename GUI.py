import tkinter as tk
import ttkbootstrap as ttk
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import GRID 
import PredictionCorrection
import CrissCrossAlg
import Composantes

# fonctions utilisees tout au long du code pour le GUI
def getMat():
    global n
    n = dimension_val.get()
    global A 
    A = GRID.creerMat(n)

def getEps():
    global epsilon
    epsilon = float(imprecision_val.get())

def getNbPoints():
    global nbPoints
    nbPoints = nbPoints_val.get()

def getTolContour():
    global tolContour
    tolContour = float(tolContour_val.get())

def getPas():
    global pas
    pas = float(pas_val.get())

def GridMethod():
    ax1.clear()
    GRID.affichage(ax1, n, A, epsilon, nbPoints)
    canvas1.draw()

def PredCorrMethod():
    ax2.clear()
    PredictionCorrection.PredCorr(ax2, n, A, epsilon, tolContour, pas)
    canvas2.draw()

def PseudoSpectreAbscisse():
    abscisse = CrissCrossAlg.CrissCrossAbscisse(n, A, epsilon, 0.00001)
    psabscisse.config(text=f"L'abscisse du pseudospectre est: {abscisse}")

def ComposantesMethod():
    ax3.clear()
    Composantes.affichage(ax3, n, A, epsilon, nbPoints)
    Composantes.affichage(ax3, n, A, epsilon / ((3+math.sqrt(2))*n), nbPoints)
    canvas3.draw()

def ComparePS():
    ax4.clear()
    GRID.affichage(ax4, n, A, epsilon, nbPoints)
    Composantes.affichage(ax4, n, A, epsilon, nbPoints)
    Composantes.affichage(ax4, n, A, epsilon / ((3+math.sqrt(2))*n), nbPoints)
    canvas4.draw()

def quitApp():
    window.quit()

# fenetre
window = ttk.Window(themename = 'darkly')
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

# attributs de la fenetre 
window.title('Projet LU2IN013')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

window.geometry(f"{window_width}x{window_height}")
# menu & notebook
menu = tk.Menu(window)

file_programme_menu = tk.Menu(menu, tearoff = False)
file_programme_menu.add_command(label = 'Quitter', command = quitApp)
file_interface_menu = tk.Menu(menu, tearoff = False)
file_interface_menu.add_command(label = 'Theme de base', command = lambda: ttk.Style().theme_use('clam'))
file_interface_menu.add_command(label = 'Theme sombre', command = lambda: ttk.Style().theme_use('darkly'))

menu.add_cascade(label = 'Programme', font = ("Arial", 11), menu = file_programme_menu)
menu.add_cascade(label = 'Interface', font = ("Arial", 11), menu = file_interface_menu)

notebook = ttk.Notebook(window)

# textes
title_label = ttk.Label(window, text = "Interface graphique du projet d'Akram et Ron", font = ("Arial", 22))
title_label.pack()

pres_label = ttk.Label(window, text = "Ci-dessous vous sont mises à disposition les différentes méthodes que l'on utilise afin d'étudier le pseudo-spectre, accompagnées d'une interface graphique permettant de visualiser nos approches.", font = ("Arial", 12))
pres_label.pack()

# arguments - Valeurs (fenetre 0)
tab0 = ttk.Frame(notebook)

label00 = ttk.Label(tab0, text = "Entrez les valeurs que vous souhaitez en veillant à cliquer (re-cliquer) sur OK après l'insertion (la modification).", font = ("Arial", 12))
label00.grid(row = 0, column = 0, sticky = tk.W)
nb_width = label00.winfo_reqwidth()

label01 = ttk.Label(tab0, text = 'Entrez la taille souhaitée de la matrice:', font = ("Arial", 12))
label01.grid(row = 1, column = 0, sticky = tk.W)
label01_width = label01.winfo_reqwidth()

dimension_val = tk.IntVar() 
dimension = ttk.Entry(tab0, textvariable = dimension_val)
dimension.grid(row = 1, column = 0, sticky = tk.W, padx = (label01_width, 0))
dimension_width = dimension.winfo_reqwidth()

button01 = ttk.Button(tab0, text='OK', command = getMat)
button01.grid(row = 1, column = 0, sticky = tk.W, padx = (label01_width + dimension_width, 0))

label02 = ttk.Label(tab0, text = "Entrez l'imprécision souhaitée epsilon:", font = ("Arial", 12))
label02.grid(row = 2, column = 0, sticky = tk.W)
label02_width = label02.winfo_reqwidth()

imprecision_val = tk.StringVar() 
imprecision = ttk.Entry(tab0, textvariable = imprecision_val)
imprecision.grid(row = 2, column = 0, sticky = tk.W, padx = (label02_width, 0))
imprecision_width = imprecision.winfo_reqwidth()

button02 = ttk.Button(tab0, text='OK', command = getEps)
button02.grid(row = 2, column = 0, sticky = tk.W, padx = (label02_width + imprecision_width, 0))

label03 = ttk.Label(tab0, text = "(GRID) Entrez le nombre souhaité de points:", font = ("Arial", 12))
label03.grid(row = 3, column = 0, sticky = tk.W)
label03_width = label03.winfo_reqwidth()

nbPoints_val = tk.IntVar() 
nbPoints = ttk.Entry(tab0, textvariable = nbPoints_val)
nbPoints.grid(row = 3, column = 0, sticky = tk.W, padx = (label03_width, 0))
nbPoints_width = nbPoints.winfo_reqwidth()

button03 = ttk.Button(tab0, text = 'OK', command = getNbPoints)
button03.grid(row = 3, column = 0, sticky = tk.W, padx = (label03_width + nbPoints_width, 0))

label04 = ttk.Label(tab0, text = "(Prédiction-correction) Entrez la tolérance de fin souhaitée pour le contour:", font = ("Arial", 12))
label04.grid(row = 4, column = 0, sticky = tk.W)
label04_width = label04.winfo_reqwidth()

tolContour_val = tk.StringVar() 
tolContour = ttk.Entry(tab0, textvariable = tolContour_val)
tolContour.grid(row = 4, column = 0, sticky = tk.W, padx = (label04_width, 0))
tolContour_width = tolContour.winfo_reqwidth()

button04 = ttk.Button(tab0, text = 'OK', command = getTolContour)
button04.grid(row = 4, column = 0, sticky = tk.W, padx = (label04_width + tolContour_width, 0))

label05 = ttk.Label(tab0, text = "(Prédiction-correction) Entrez le pas souhaité pour le contour:", font = ("Arial", 12))
label05.grid(row = 5, column = 0, sticky = tk.W)
label05_width = label05.winfo_reqwidth()

pas_val = tk.StringVar() 
pas = ttk.Entry(tab0, textvariable = pas_val)
pas.grid(row = 5, column = 0, sticky = tk.W, padx = (label05_width, 0))
pas_width = pas.winfo_reqwidth()

button05 = ttk.Button(tab0, text = 'OK', command = getPas)
button05.grid(row = 5, column = 0, sticky = tk.W, padx = (label05_width + pas_width, 0))

button06 = ttk.Button(tab0, text="Afficher l'abscisse du pseudospectre", command=PseudoSpectreAbscisse)
button06.grid(row=6, column=0, sticky=tk.W)
b06_width = button06.winfo_reqwidth()

psabscisse = ttk.Label(tab0, text="")
psabscisse.grid(row=6, column=0, sticky=tk.W, padx=(b06_width, 0))

# arguments - GRID (fenetre 1)
tab1 = ttk.Frame(notebook)

button11 = ttk.Button(tab1, text = 'Afficher', command = GridMethod)
button11.grid(row = 0, column = 0, sticky = tk.W, padx = nb_width)

canvas1 = FigureCanvasTkAgg(fig1, tab1)
canvas1.get_tk_widget().grid(row = 1, column = 0)

toolbar1 = NavigationToolbar2Tk(canvas1, tab1, pack_toolbar = False)
toolbar1.update()
toolbar1.grid(row = 2, column = 0)

# arguments - PredCorr (fenetre 2)
tab2 = ttk.Frame(notebook)

button21 = ttk.Button(tab2, text = 'Afficher', command = PredCorrMethod)
button21.grid(row = 0, column = 0, sticky = tk.W, padx = nb_width)

canvas2 = FigureCanvasTkAgg(fig2, tab2)
canvas2.get_tk_widget().grid(row = 1, column = 0)

toolbar2 = NavigationToolbar2Tk(canvas2, tab2, pack_toolbar = False)
toolbar2.update()
toolbar2.grid(row = 2, column = 0)

# arguments - Pseudospectre par composante (fenetre 3)
tab3 = ttk.Frame(notebook)

button31 = ttk.Button(tab3, text = 'Afficher', command = ComposantesMethod)
button31.grid(row = 0, column = 0, sticky = tk.W, padx = nb_width)

canvas3 = FigureCanvasTkAgg(fig3, tab3)
canvas3.get_tk_widget().grid(row = 1, column = 0)

toolbar3 = NavigationToolbar2Tk(canvas3, tab3, pack_toolbar = False)
toolbar3.update()
toolbar3.grid(row = 2, column = 0)

# arguments - comparaison du pseudospectre et du pseudospectre par composantes (fenetre 4)
tab4 = ttk.Frame(notebook)

button41 = ttk.Button(tab4, text='Afficher', command=ComparePS)
button41.grid(row = 0, column = 0, sticky = tk.W, padx = nb_width)

canvas4 = FigureCanvasTkAgg(fig4, tab4)
canvas4.get_tk_widget().grid(row = 1, column = 0)

toolbar4 = NavigationToolbar2Tk(canvas4, tab4, pack_toolbar = False)
toolbar4.update()
toolbar4.grid(row = 2, column = 0)

# menu & notebook - ajouts des differentes fenetres 
window.configure(menu = menu)

notebook.add(tab0, text = 'Valeurs')
notebook.add(tab1, text = 'GRID')
notebook.add(tab2, text = 'Prédiction-correction')
notebook.add(tab3, text = 'Pseudo-spectre par composantes')
notebook.add(tab4, text = 'Comparaison pseudo-spectre et pseudo-spectre par composantes')
notebook.pack(pady = 15)

# run
window.mainloop()