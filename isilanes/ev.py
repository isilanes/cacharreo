import sys

# Leemos el fichero
try:
    fn = sys.argv[1]
    f = open(fn, 'r')
except:
    print ('File not present: ' + fn )
    exit()

# Leemos las coordenadas x:
linea = f.readline()
linea = linea.split('x')[1].strip()
elemento = linea.split()
x = []
for k in range(len(elemento)):
    x.append(float(elemento[k]))

# Leemos las coordenadas y:
linea = f.readline()
linea = linea.split('y')[1].strip()
elemento = linea.split()
y = []
for k in range(len(elemento)):
    y.append(float(elemento[k]))

# Leemos las coordenadas z:
linea = f.readline()
linea = linea.split('z')[1].strip()
elemento = linea.split()
z = []
for k in range(len(elemento)):
    z.append(float(elemento[k]))

# Read useless line:
f.readline()

# Open all output files, and initialize with XYZ:
nx = len(x)
for i in range(nx):
    outfn = 'out_isc/ev_{0:04d}.out'.format(i+1)
    with open(outfn, 'w') as g:
        string = '{0}  {1}  {2}  0.0\n'.format(x[i], y[i], z[i])
        g.write(string)

t = []
vel = []
# Read values line by line:
for line in f:
    line = line.replace('(','')
    line = line.replace(')','')
    aline = line.split()
    for i in range(nx):
        outfn = 'out_isc/ev_{0:04d}.out'.format(i)
        slice = aline[3*i+1:3*i+4]
        string = '{0[0]}  {1[0]} {1[1]} {1[2]}\n'.format(aline, slice)
        with open(outfn, 'a') as g:
            g.write(string)
