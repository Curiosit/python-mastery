import sys
import random

chars = '\|/'

def draw(rows, columns):
    for x in range(0, rows):
        print(''.join(random.choice(chars) for _ in range(0,columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))