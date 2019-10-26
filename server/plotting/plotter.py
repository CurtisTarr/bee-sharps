import pandas as pd
import matplotlib.pyplot as plt


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)

    data_frame['Age'].plot()
    plt.title('Row No')
    plt.ylabel('count')
    plt.xlabel('')

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