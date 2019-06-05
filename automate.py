import numpy as np

import matplotlib.pyplot as plt

rule_choice = input("Choisissez l'une de ces fameuses règles [28 | 50 | 60 | 90 | 110 | 146] : ")

row_number = input("Choisissez un nombre de générations entre 0 et 1000 : ")

col_number = input("Largeur : choisissez un nombre entre 0 et 1000 : ")

#if int(rule_choice) != 28 or 50 or 60 or 90 or 110 or 146:
#    rule_choice = input("Veuillez choisir l'un de ces nombres [28 | 50 | 60 | 90 | 110 | 146] : ")
#if int(row_number) > 1000:
#    row_number = input("Veuillez ne pas choisir un nombre supérieur à 1000 : ")
#if int(col_number) > 1000:
#    col_number = input("Veuillez ne pas choisir un nombre supérieur à 1000 : ")

width = int(row_number)

lenght = int(row_number)

Rule = int(rule_choice)

pop = np.zeros((lenght), dtype = np.int32)

center =  pop.size // 2

pop[center] = 1

new_population = np.zeros((lenght), dtype = np.int32)

def Rule_maker(pop):
    if Rule == 28:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 1 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 1 and pop[i + 1] == 0:
                new_population[i] = 1
            else:
                new_population[i] = 0
        return new_population
    if Rule == 110:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 1 and pop[i + 1] == 1:
                new_population[i] = 0
            elif pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 0
            elif pop[i - 1] == 0 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 0
            else:
                new_population[i] = 1
        return new_population
    if Rule == 50:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 0 and pop[i + 1] == 1:
                new_population[i] = 1
            else:
                new_population[i] = 0
        return new_population
    if Rule == 60:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 1 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 1 and pop[i + 1] == 0:
                new_population[i] = 1
            else:
                new_population[i] = 0
        return new_population
    if Rule == 90:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 1 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 1 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 0 and pop[i + 1] == 1:
                new_population[i] = 1
            else:
                new_population[i] = 0
        return new_population
    if Rule == 146:
        new_population = np.zeros((len(pop)), dtype = np.int32)
        for i in range(1, len(pop)-1):
            if pop[i - 1] == 1 and pop[i] == 1 and pop[i + 1] == 1:
                new_population[i] = 1
            elif pop[i - 1] == 1 and pop[i] == 0 and pop[i + 1] == 0:
                new_population[i] = 1
            elif pop[i - 1] == 0 and pop[i] == 0 and pop[i + 1] == 1:
                new_population[i] = 1
            else:
                new_population[i] = 0
        return new_population

def create_board(n_rows, n_cols):
    start = np.zeros(n_cols, dtype = np.int32)
    start[n_cols // 2] = 1
    board = np.zeros((n_rows, n_cols), dtype = np.int32)
    board[0,:] = start
    for i in range(n_rows - 1):
        current_pop = board[i , :]
        board[i + 1, :] = Rule_maker(current_pop)
    return board

automate = create_board(width, lenght)

plt.imshow(automate, cmap = "hot")
plt.show()
plt.imsave('Rule_110.png', automate, dpi = 200)
