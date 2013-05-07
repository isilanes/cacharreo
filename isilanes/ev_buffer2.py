import sys
import itertools as it

#------------------------------------------------------------------------------#

# Variables:
buffer_size = 512

# Read input file:
try:
    fn = sys.argv[1]
    f = open(fn, 'r')
except:
    print ('Error reading file, or no file name given')
    sys.exit()

# Read X, Y and Z coordinates, from first three lines:
x = f.readline().split()[2:]
y = f.readline().split()[2:]
z = f.readline().split()[2:]

# Open all output files, and initialize with XYZ:
nx = len(x)
for i in range(nx):
    outfn = 'out_isc/ev_{0:04d}.out'.format(i+1)
    with open(outfn, 'w') as g:
        string = '{0}  {1}  {2}  0.0\n'.format(x[i], y[i], z[i])
        g.write(string)

# Read useless line:
f.readline()

# Read values line by line:
buffer = True
while buffer:
    strings = [ [] for i in range(nx) ]
    buffer = list(it.islice(f, buffer_size))
    for line in buffer:
        line = line.replace('(','')
        line = line.replace(')','')
        aline = line.split()
        for i in range(nx):
            slice = aline[3*i+1:3*i+4]
            strings[i].append('{0[0]}  {1[0]} {1[1]} {1[2]}\n'.format(aline, slice))

    for i in range(nx):
        outfn = 'out_isc/ev_{0:04d}.out'.format(i)
        with open(outfn, 'a') as g:
            for line in strings[i]:
                g.write(line)
