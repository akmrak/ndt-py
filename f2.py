__author__ = 'maddoxx'
import numpy as np
import scipy as sp
import scipy.io as io
import pylab as p1
import matplotlib.image as mpimg

mat=io.loadmat('/home/maddoxx/cfrp_16_holes_DFM001to01_100s.mat')
a=mat['imgseq']
b=a[1][1][0:a.shape[2]]
c=np.correlate(b, b, mode='full', old_behavior=False)
d=range(0,2*a.shape[2]-1)
e= range(0,a.shape[2])


z = np.polyfit(e, b, 2)
f=np.poly1d(z)
x=e
y=b
x_new=e
y_new=f(x_new)
p1.plot(e,b)
p1.plot(x_new,y_new)
y_normalized=np.subtract(y_new,y)
x_normalized=x_new
#p1.plot(x_normalized,y_normalized)
y_correlated=np.correlate(y_normalized,y_normalized, mode='full', old_behavior=False)
x_correlated=range(0,2*a.shape[2]-1)
p1.show()
