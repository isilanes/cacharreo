import sys
import subprocess as sp

#------------------------------------------------------------------------------#

def mk_buffer(n):
    '''
    Returns an initialized buffer of n elements (each one being an empty string).
    '''
    buff = []

    for i in range(n):
        buff.append('')

    return buff

#------------------------------------------------------------------------------#

# Read input file:
try:
    fn = sys.argv[1]
    f = open(fn, 'r')
except:
    print ('Error reading file, or no file name given')
    sys.exit()

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
    #outfn = 'out_isc/ev_{0:04d}.out'.format(i+1)
    outfn = 'out_isc/ev_{0}.out'.format(i+1)
    with open(outfn, 'w') as g:
        string = '{0}  {1}  {2}  0.0\n'.format(x[i], y[i], z[i])
        g.write(string)

cmnd  = "grep -v '#' {0} | ".format(fn)
cmnd += "sed -e 's/(//g;s/)//g' | "
cmnd += "awk '{ for (i = 0; i < 5151; i++) { print $1, $(3*i+2), $(3*i+3), $(3*i+4) "
cmnd += " >> \"out_isc/ev_\"i\".out\" } }'"

s = sp.Popen(cmnd, shell=True)
s.communicate()
