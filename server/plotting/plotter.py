import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)

    data_frame['Age'].plot()
    plt.title('Row No')
    plt.ylabel('count')
    plt.xlabel('')

    plt.show()


def plot_gender(file_path):
    data_frame = pd.read_csv(file_path)

    males = 0
    males_interviewed = 0
    females = 0
    females_interviewed = 0

    for index, row in data_frame.iterrows():
        if row['Gender'] == 'M':
            males += 1
            if row['Interviewed']:
                males_interviewed += 1
        elif row['Gender'] == 'F':
            females += 1
            if row['Interviewed']:
                females_interviewed += 1

    n_groups = 2
    male_stats = (males, males_interviewed)
    female_stats = (females, females_interviewed)

    plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, male_stats, bar_width,
            alpha=opacity,
            color='b',
            label='Male')

    plt.bar(index + bar_width, female_stats, bar_width,
            alpha=opacity,
            color='r',
            label='Female')

    plt.title('Sex vs Interviewed')
    plt.xticks(index + bar_width, ('Total applicants', 'No. Interviewed'))
    plt.legend()

    plt.tight_layout()
    plt.show()
