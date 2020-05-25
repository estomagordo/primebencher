import os
import pathlib
import matplotlib.pyplot as plt

def main():
    currdir = pathlib.Path(__file__).parent.absolute()
    plotdir = os.path.join(currdir, 'plotput')

    plt.xscale("log")
    plt.yscale("log")

    for _, _, files in os.walk(plotdir):
        for filename in files:
            with open(os.path.join(plotdir, filename)) as f:
                xs = list(map(int, f.readline().split()))
                ys = list(map(float, f.readline().split()))
            
            plt.plot(xs, ys, label=filename)

    plt.legend()            
    plt.show()

if __name__ == '__main__':
    main()