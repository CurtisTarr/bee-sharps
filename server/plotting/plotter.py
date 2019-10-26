import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_csv(file_path):
    data_frame = pd.read_csv(file_path)
    plot_graph(data_frame, 'Age', 'Age Breakdown of Applicants', 'Number of Applicants', 'Age', False)
    plot_graph(data_frame, 'Race', 'Racial Breakdown of Applicants', 'Number of Applicants', 'Race', True)
    plot_vs_interviewed(data_frame, 'Gender')
    plot_vs_interviewed(data_frame, 'Race')


def plot_graph(data_frame, column: str, title: str, y_label: str, x_label: str, should_use_hist: bool):
    if should_use_hist:
        data_frame[column].hist()
    else:
        data_frame[column].plot()
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)

    plt.show()


def plot_vs_interviewed(data_frame, column: str):
    unique_column_values = data_frame[column].unique()

    plt.subplots()
    index = np.arange(2)
    bar_width = 0.15
    opacity = 0.8

    iteration = 0
    for value in unique_column_values:
        if not isinstance(value, str):
            continue

        data = get_info_for_row(data_frame, column, value)
        plt.bar(index + (bar_width * iteration), data, bar_width,
                alpha=opacity,
                label=value)

        iteration += 1

    plt.title(column + ' vs Interviewed')
    plt.xticks(index + bar_width, ('Total applicants', 'No. Interviewed'))
    plt.legend()
    plt.show()


def get_info_for_row(data_frame, column_label: str, column_value: str) -> (int, int):
    total = 0
    interviewed = 0

    for index, row in data_frame.iterrows():
        if row[column_label] == column_value:
            total += 1
            interviewed += row.Interviewed

    return total, interviewed


def convert_interview_bool(data_frame):
    for index, row in data_frame.iterrows():
        if row.Interviewed:
            data_frame.loc['Interviewed'] = 1
        elif not row.Interviewed:
            data_frame.loc['Interviewed'] = 0
        else:
            data_frame.drop(index)

    return data_frame
