import numpy as np

import matplotlib.pyplot as plt

participant_choice = input("Choisissez un nombre entre 0 et 100 : ")

size_array = int(participant_choice)

line = np.zeros((size_array), dtype = np.int16)

center =  line.size // 2

line[center] = 1

new_line = np.zeros((size_array), dtype = np.int16)

print(line)

iteration = 0

while iteration < 5:
    for i in range(1, len(line)- 1):
        if line[i - 1] == 1 and line[i] == 1 and line[i + 1] == 0:
            new_line[i] = 1
        elif line[i - 1] == 1 and line[i] == 0 and line[i + 1] == 1:
            new_line[i] = 1
        elif line[i - 1] == 0 and line[i] == 1 and line[i + 1] == 1:
            new_line[i] = 1
        elif line[i - 1] == 0 and line[i] == 1 and line[i + 1] == 0:
            new_line[i] = 1
        elif line[i - 1] == 0 and line[i] == 0 and line[i + 1] == 1:
            new_line[i] = 1
    print(new_line)
    iteration =+ 1
    line = new_line

#plt.imshow(matrice)
#plt.show()
