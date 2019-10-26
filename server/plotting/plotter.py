import pandas as pd
import matplotlib.pyplot as plt


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)
    plot_graph(data_frame, 'Age', 'Age Breakdown of Applicants', 'Number of Applicants', 'Age', False)
    plot_graph(data_frame, 'Race', 'Racial Breakdown of Applicants', 'Number of Applicants', 'Race', True)


def plot_graph(data_frame, column, title, ylabel, xlabel, shouldUseHist):
    if shouldUseHist:
        data_frame[column].hist()
    else:
        data_frame[column].plot()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    plt.show()


def convert_interview_bool(dataset):

    for index, row in dataset.iterrows():
        if row.Interviewed:
            dataset.loc['Interviewed'] = 1
        elif not row.Interviewed:
            dataset.loc['Interviewed'] = 0
        else:
            dataset.drop(index)

    return dataset