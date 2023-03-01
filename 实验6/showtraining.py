import matplotlib
import os
import numpy as np
from matplotlib import pyplot as plt
import argparse
import sys

# file_loss_path = sys.path[0] + "\\train_loss.txt"
file_loss_path = './train_loss.txt'

lst_loss = list()
with open(file_loss_path) as file_object:
    for line in file_object:
        if "e" in line:
            lst_loss.append(eval(line))
        else:
            lst_loss.append(float(line[:-2]))
    file_object.close()

plt.plot([i+1 for i in range(12)],lst_loss)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()
