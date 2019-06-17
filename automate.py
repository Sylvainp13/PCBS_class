""" Implémentation d'un automate cellulaire à une dimension

"""

import numpy as np
import matplotlib.pyplot as plt
import webbrowser as wb

width = 500 # nombre d'éléments contenus dans la population initiale
lenght = 500 # nonbre de générations

wb.open('https://fr.wikipedia.org/wiki/Automate_cellulaire') # ouvre une page wikipédia en lien avec les automates cellulaires

print("Lisez attentivement les informations sur la page qui vient de s'afficher")

rule_choice = int(input("Maintenant que vous en savez plus à propos des automates cellulaires, choisissez le chiffre correspondant à l'une des règles proposée entre crochet -> [Règle n°28 | Règle n°30 | Règle n°50 | Règle n°60 | Règle n°110 | Règle n°146 | Règle n°184] : "))

rule = rule_choice

population = np.zeros((lenght), dtype = np.int32) # définit la 1ère population comme une suite de 0

center =  population.size // 2

population[center] = 1

new_generation = np.zeros((lenght), dtype = np.int32)

def rule_generator(population):
    """ Transforme un array en un nouvel array de même longueur en fonction de la règle appliquée

    Argument :
    population : un array d'une longueur de 500 éléments

    Retourne :
    new_generation : un nouvel array de même longueur résultant de la transformation de la population initiale en fonction de la règle appliquée

    """
    if rule == 28:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 0:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation
    if rule == 30:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation
    if rule == 50:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation
    if rule == 60:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 0:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation
    if rule == 110:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 0
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 0
            elif population[i - 1] == 0 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 0
            else:
                new_generation[i] = 1
        return new_generation
    if rule == 146:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation
    if rule == 184:
        new_generation = np.zeros((len(population)), dtype = np.int32)
        for i in range(1, len(population)-1):
            if population[i - 1] == 1 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 0 and population[i] == 1 and population[i + 1] == 1:
                new_generation[i] = 1
            elif population[i - 1] == 1 and population[i] == 0 and population[i + 1] == 0:
                new_generation[i] = 1
            else:
                new_generation[i] = 0
        return new_generation

def automate_generator(n_rows, n_cols):
    """ Créé une matrice montrant l'évolution de la population en fonction de la règle appliquée

    Argurment :
    n_rows : un entier correspondant au nombre de génération de l'automate
    n_cols : un entier correspondant au nombre d'éléments dans la population initiale

    Retourne :
    board : une matrice montrant l'évolution des conditions initiales en fonction de la règle appliquée
    """
    start = np.zeros(n_cols, dtype = np.int32)
    start[n_cols // 2] = 1
    board = np.zeros((n_rows, n_cols), dtype = np.int32)
    board[0,:] = start
    for i in range(n_rows - 1):
        current_population = board[i , :]
        board[i + 1, :] = rule_generator(current_population)
    return board

wb.open('http://mathworld.wolfram.com/Rule' + str(rule) + '.html')

automate = automate_generator(width, lenght)

plt.imshow(automate)
plt.show()
plt.imsave('rule_' + str(rule) + '.png', automate, dpi = 100, cmap = "hot") # enregistre une image au au format .png
