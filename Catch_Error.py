import sys

def Hours(minute):
    H = minute // 60
    M = minute % 60
    print('{} H,{} M'.format(H, M))


if __name__ == '__main__':
    a = int(sys.argv[1])
    try:
        if a < 0:
            raise ValueError
        Hours(a)
    except ValueError:
        print('Parameter Error')

