__author__ = 'maddoxx'
import numpy as np
import scipy as sp
import scipy.io as io
import pylab as p1
import matplotlib.image as mpimg

#load the mat into matlab memory
mat=io.loadmat('/home/maddoxx/cfrp_16_holes_DFM001to01_100s.mat')
a=mat['imgseq']                #save the mat file into python array
vid_data=np.array(a)           #save the mat file into numpy python array


#calculate reference pixel correlation
b=a[1][1][0:a.shape[2]]        #reference pixel with which we corelate later
d=range(0,2*a.shape[2]-1)
e= range(0,a.shape[2])
z = np.polyfit(e,b , 2)        #calculate the polynomial coefficients for the intensity of the reference pixel across samples
f=np.poly1d(z)                 #construct the polynomial
x=e
y=b
x_new=e
y_new=f(x_new)                 #calculate the curve fitting curve
y_normalized_11=np.subtract(y_new,y)  #calculate the subtracted pixel intensity
x_normalized=x_new


new_data=np.zeros((320,256,5599))
x=22
y=24
z = np.polyfit(e,vid_data[x,y ,:],2)            #calculate the curve fitting polynomial coefficients
f=np.poly1d(z)
x_new=e
y_new=f(x_new)                                  #calculate the curve fitting polynomial
y_normalized=np.subtract(y_new,vid_data[x,y ,:])
x_normalized=x_new
y_correlated=np.correlate(y_normalized,y_normalized_11, mode='full', old_behavior=False)
x_correlated=range(0,2*a.shape[2]-1)
max1=np.amax(y_correlated)
y_correlated /=max1
new_data[x,y,:]=y_correlated
print  'The value of x is ', x , ', and y is ' ,y, '...'



p1.plot(x_correlated,y_correlated)
p1.show()
print 'end'