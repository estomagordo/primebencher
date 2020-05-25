from time import time
import os
import pathlib
import primes


def main(repeats=3):
    currdir = pathlib.Path(__file__).parent.absolute()
    plotdir = os.path.join(currdir, 'plotput')

    if not os.path.exists(plotdir):
        os.mkdir(plotdir)

    functions = [f for _, f in primes.__dict__.items() if callable(f)]

    for function in functions:
        filename = os.path.join(currdir, 'plotput', function.__name__ + '.dat')

        if os.path.exists(filename):
            continue

        xs = []
        ys = []
        
        for exp in range(1, 9):
            n = 10**exp
            cumtime = 0.0

            for _ in range(repeats):
                now = time()
                function(n)
                cumtime += time() - now

            xs.append(n)
            ys.append(cumtime / repeats)

        with open(filename, 'w') as f:
            f.write(' '.join(str(x) for x in xs))
            f.write('\n')
            f.write(' '.join(str(y) for y in ys))

if __name__ == '__main__':
    main()