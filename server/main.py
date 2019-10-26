import sys
from api import api
from plotting import plotter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == '-p':
            plotter.plot_csv('dataset.csv')
            sys.exit()

    api.run_api()
