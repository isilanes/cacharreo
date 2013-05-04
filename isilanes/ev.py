# Input:
fn = "test.dat"

# Leemos el fichero
try:
    f = open(fn, 'r')
except:
    print ('File not present: ' + fn )

# Leemos las coordenadas x:
linea = f.readline()
linea = linea.split('x')[1].strip()
elemento = linea.split()
x = []
for k in range(len(elemento)):
    x.append(float(elemento[k]))

print(len(x))

# Leemos las coordenadas y:
linea = f.readline()
linea = linea.split('y')[1].strip()
elemento = linea.split()
y = []
for k in range(len(elemento)):
    y.append(float(elemento[k]))

print(len(y))

# Leemos las coordenadas z:
linea = f.readline()
linea = linea.split('z')[1].strip()
elemento = linea.split()
z = []
for k in range(len(elemento)):
    z.append(float(elemento[k]))

print(len(z))

# Read useless line:
f.readline()

t = []
vel = []
# Leemos el tiempo y el valor de la presion en ese instante para todos los puntos.
for linea in f:
    dato = linea.split('(')
    t.append(dato[0].strip())

    for k in dato[1:]:
        vel.append(k.split(')')[0].strip())

'''
# Separamos los datos por sensores, y cada sensor lo guardamos en un fichero
for k in range(nx):
    print('Sensor ' + str(k+1) + ' de ' + str(nx) + '.')

    ficheroGuardar = 'sensorVel_' + str(k+1) + '.dat'
    fileW = open(os.path.join(savePath,ficheroGuardar), 'w')

    string = str(x[k]) + '  ' + str(y[k]) + '  ' + str(z[k]) + '  0.0'
    fileW.write(string + '\n')

    for tt in range(nt):
        string = str(t[tt]) + '  ' + vel[tt*nx+k]
        fileW.write(string + '\n')

    fileW.close()

print('Terminado!')
'''
