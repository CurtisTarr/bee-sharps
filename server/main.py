from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt #graphing
import numpy as np

app = Flask(__name__)

dataFrame = pd.read_csv('dataset.csv')

dataFrame['Age'].plot()
plt.title('Row No')
plt.ylabel('count')
plt.xlabel('')


plt.show()


