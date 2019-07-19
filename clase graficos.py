import matplotlib.pyplot as plt

import numpy as np
import pandas as pd 
# import seaborn as sn
%matplotlib inline
#columna es una variable fila es una muestra

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df= pd.DataFrame(np.random.randn(1000,4), index=ts.index, columns=list('ABCD')).cumsum()

ax1=df.plot.area(stacked=False)
plt.title('valores')
plt.ylabel('cantidad')
plt.xlabel('fecha')
plt.savefig('valores.png')
ax1.set_xlabel('l__________________________c') 

ax2=df.plot.line()
plt.title('valores')
plt.ylabel('cantidad')
plt.xlabel('fecha')
plt.savefig('valores.png')
ax2.figure.savefig('linea')

grafico = plt.subplot()
df.plot.area(stacked=False, ax=grafico)
df.plot.line(ax=grafico)
figura, grafico = plt.subplots(1,2, figsize=(15,5))


df.plot.area(stacked=False, ax=grafico[0])
df.plot.line(ax=grafico[1])

plt.subplot?
type(ax1)
ax1
ax1.set_xlabel('l__________________________c') 