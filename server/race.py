from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt #graphing

app = Flask(__name__)

dataFrame = pd.read_csv('dataset.csv')
dataFrame.Race.hist()

plt.title('Racial Breakdown of Applicants')
plt.ylabel('Number of Applicants')
plt.xlabel('Race')

plt.show()
