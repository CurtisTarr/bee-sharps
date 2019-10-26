import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)
    plot_graph(data_frame, 'Age', 'Age Breakdown of Applicants', 'Number of Applicants', 'Age', False)
    plot_graph(data_frame, 'Race', 'Racial Breakdown of Applicants', 'Number of Applicants', 'Race', True)
    plot_gender(data_frame)


def plot_graph(data_frame, column, title, ylabel, xlabel, shouldUseHist):
    if shouldUseHist:
        data_frame[column].hist()
    else:
        data_frame[column].plot()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    plt.show()


def plot_gender(data_frame):
    males = 0
    males_interviewed = 0
    females = 0
    females_interviewed = 0

    for index, row in data_frame.iterrows():
        if row['Gender'] == 'M':
            males += 1
            males_interviewed += row.Interviewed
        elif row['Gender'] == 'F':
            females += 1
            females_interviewed += row.Interviewed

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


def convert_interview_bool(data_frame):
    for index, row in data_frame.iterrows():
        if row.Interviewed:
            data_frame.loc['Interviewed'] = 1
        elif not row.Interviewed:
            data_frame.loc['Interviewed'] = 0
        else:
            data_frame.drop(index)

    return data_frame
