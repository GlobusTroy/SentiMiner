import matplotlib.pyplot as plt
import csv
import re

x = []
y = []

with open('data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    print plots
    print type(plots)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

