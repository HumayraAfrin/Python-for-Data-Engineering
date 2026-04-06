import time
import multiprocessing

def mySleep(n):
    print(f'Sleeping for {n}')
    time.sleep(n)


def main():
    l = {1, 2, 4, 5, 2, 1, 3}

    pool = multiprocessing.Pool(3)
    pool.map(mySleep, l)


if __name__ == '__main__':
    main()
