import sys

fname = sys.argv[0]
x = int(sys.argv[1])
y = int(sys.argv[2])

print(x+y, x-y, x*y, int(x/y), x%y, sep = '\n')

