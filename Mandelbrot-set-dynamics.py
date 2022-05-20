import numpy 
from numpy import linspace
import cmath,math
import matplotlib.pyplot as plt

nIter = linspace(1,50) #number of iterations
nSpace = linspace(1,500,500) #number of points for which system will be tested

a = linspace(-2.4, 1.2, int(max(nSpace))) #range of a
b = linspace(-1.5, 1.5, int(max(nSpace))) #range of b

Ba = [] #array for which values will be plotted black
Bb = []
Wa = [] #array for which values will be plotted black
Wb = []

for i in nSpace:
    for j in nSpace:
        z0r = 0
        z0i = 0
        z0 = complex(z0r,z0i) #ititial point
        for k in nIter:
            z1 = z0**2 + complex(a[int(i)-1],b[int(j)-1])
            z0 = z1
            mod = math.sqrt(z0.real**2 + z0.imag**2)
            if mod > 4:
                break

        if mod < 4:
            Ba.append(a[int(i)-1])
            Bb.append(b[int(j)-1])
        # elif (k % 2) == 0:
        #     Ba.append(a[int(i)-1])
        #     Bb.append(b[int(j)-1])
        else:
            Wa.append(a[int(i)-1])
            Wb.append(b[int(j)-1])


plt.scatter(Ba,Bb,color = 'black')
plt.scatter(Wa,Wb,color = 'white')
plt.xlim([min(a), max(a)])
plt.ylim([min(b), max(b)])
plt.show()
