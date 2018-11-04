import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import csv

v_in=10
v_out=50
st_in=1.03e-4
dlugosc_fali=[]
stezenie=[]

csv_read=csv.reader(open('IPS_Artur.csv','rt'), delimiter=';', lineterminator='\n');
for row in csv_read:
    dlugosc_fali.append(float(row[0]))
    stezenie.append(float(row[1]))

wartosc_obliczona=st_in*v_in/v_out
print("Stężenie obliczone", wartosc_obliczona)

st=[6.01862e-6, 1.20372e-5, 2.40745e-5, 3.61117e-5, 4.8149e-5, 6.01862e-5, 7.22235e-5, 8.42607e-5, 0.000108335]
abso=[0.11, .179, .327, .435, .531, .679, .751, .867, 1.003]

wsp=np.polyfit(st, abso, 1)
print("Stężenie odczytane", (max(stezenie[60:90])-wsp[1])/wsp[0])

step_x=np.arange(0, 0.00011, 0.0000001)
plt.figure()
plt.plot(step_x, wsp[0]*step_x+wsp[1])
plt.xlabel('Stezenie [mol/l]')
plt.ylabel('Absorbcja [A]')
plt.xlim(0,0.0001)
plt.ylim(0, 1.1)

plt.figure()
plt.plot(dlugosc_fali, stezenie)
plt.xlabel('Dlugosc fali [nm]')
plt.ylabel('Absorbcja [A]')
plt.xlim(190,500)

plt.show()