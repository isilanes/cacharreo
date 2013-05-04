#!/usr/bin/python3

# Script hecho para extraer las velocidades de los sensores puestos en runtime.
# Hecho por Jose A Armesto, armestoja@unican.es
# Para hacer este script he usado de base el script post_sensVoF.py hecho por Pablo Higuera
# y el script extrae2.py hecho por Iñaki Silanes y Jose A Armesto.
# Copyright de IH Cantabria, 29 de Enero de 2013

# Se leen los sensores obtenidos de IH-FOAM en runtime que estan almacenados en la carpeta
# "probesVel/0/" y se llama "U". Los resultados se almacenan en la carpeta "sensoresVel",
# un fichero por cada sensor. La primera linea tiene las coordenadas del punto (x,y,z) y un 0
# para que todas las filas tengan el mismo numero de elementos. Las lineas posteriores tienen
# el instante temporal y el valor de las velocidades (t,U,V,W)

import os
import glob

pathname = os.path.abspath('.')
savePath =os.path.join(pathname,'sensorVel')
if not os.path.isdir(savePath):
    os.makedirs(savePath)
# Nombre del fichero generado por IH-FOAM
name = "U"

# Nombre del directorio donde se guarda el fichero
directorio = "probesVel/0/"

## Leemos el fichero
fichero = os.path.join(pathname,directorio,name)
#try:
#    fileR = open(fichero, 'r')
#except:
#    print ('File not present: ' + fichero )
#else:
#    # Guardamos las filas del fichero 
#    data = fileR.read()
#    fileR.close()
#    data = data.split('\n')

cont = 0

with open(fichero) as myfile:

    for line in myfile:

        if (cont == 0): 
            # Leemos las coordenadas x
            linea = line.rstrip('\n')

#            linea = data[0]
            linea = linea.split('x')[1].strip()
            elemento = linea.split()
            x = []
            for k in range(len(elemento)):
                x.append(float(elemento[k]))

            nx = len(x)
            
        elif(cont == 1):

            # Leemos las coordenadas y
            linea = line.rstrip('\n')
 
            linea = linea.split('y')[1].strip()
            elemento = linea.split()
            y = []
            for k in range(len(elemento)):
                y.append(float(elemento[k]))

        elif(cont == 2):

            # Leemos las coordenadas z
            linea = line.rstrip('\n')
 
            linea = linea.split('z')[1].strip()
            elemento = linea.split()
            z = []
            for k in range(len(elemento)):
                z.append(float(elemento[k]))

        elif(cont == 3):
            it = 0
            t = []
            vel = []

        elif(cont > 3):
            # Leemos el tiempo y el valor de la presion en ese instante para todos los puntos.
            linea = line.rstrip('\n')
            dato = linea.split('(')
            t.append(dato[0].strip())

            for k in dato[1:]:
                it = it+1
                vel.append(k.split(')')[0].strip())

        cont += 1 

    nvel = len(vel)
    nt = min(len(t),int(nvel/nx))

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

