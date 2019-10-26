import pandas as pd
import matplotlib.pyplot as plt


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)

    data_frame['Age'].plot()
    plt.title('Row No')
    plt.ylabel('count')
    plt.xlabel('')

    plt.show()
