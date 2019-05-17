import numpy as np

import matplotlib.pyplot as plt

row_number = input("Longueur : choisissez un nombre entre 0 et 1000 : ")

col_number = input("Largeur : choisissez un nombre entre 0 et 10000 : ")

width = int(row_number)

lenght = int(row_number)

pop = np.zeros((lenght), dtype = np.int32)

center =  pop.size // 2

pop[center] = 1

new_population = np.zeros((lenght), dtype = np.int32)

def next_generation_110(pop):
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

def create_board(n_rows, n_cols):
    start = np.zeros(n_cols, dtype = np.int32)
    start[n_cols // 2] = 1
    board = np.zeros((n_rows, n_cols), dtype = np.int32)
    board[0,:] = start
    for i in range(n_rows - 1):
        current_pop = board[i , :]
        board[i + 1, :] = next_generation_110(current_pop)
    return board

automate = create_board(width, lenght)

plt.imshow(automate, cmap = "hot")
plt.show()
plt.imsave('Rule_110.png', automate, dpi = 200)
