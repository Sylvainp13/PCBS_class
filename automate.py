import numpy as np

import matplotlib.pyplot as plt

participant_choice = input("Choisissez un nombre entre 0 et 100 : ")

len_array = int(participant_choice)

matrice = np.zeros((len_array), dtype = np.int16)

center =  matrice.size // 2

matrice[center] = 1

print(matrice)

#plt.imshow(matrice)
#plt.show()
