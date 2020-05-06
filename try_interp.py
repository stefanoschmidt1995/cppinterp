import numpy as np
import matplotlib.pyplot as plt
import time
import cppinterp #importing the package

	#setting up an interpolation problem
N_data = 200
x = np.linspace(0,100,100) 				#old grid
y = np.exp(x/100.)						#function evaluated at the old grid
x_new = np.linspace(-10,110,500000)		#new grid to interpolate at

y = np.repeat(y[None,:],N_data, axis =0) #creating a N dimensional problem
y_np = np.zeros((N_data, len(x_new)))
y_new = np.zeros((N_data, len(x_new)))

time_0 = time.process_time_ns()/1e6 #ms
for i in range(N_data):
	y_np[i,:] = np.interp(x_new, x, y[i,:])
time_1 = time.process_time_ns()/1e6
for i in range(N_data):
	y_new[i,:] = cppinterp.interp(x_new, x, y[i,:]) #sequential interpolation (like np.interp)
time_2 = time.process_time_ns()/1e6
y_new_par = cppinterp.interp_N(x_new, x, y, 0,0) #parallel interpolation (left and right boundaries are zero)
time_3 = time.process_time_ns()/1e6

print("# interpolation: ", N_data, "\nNew grid size: ", len(x_new))
print("Time:\n\tnp\t\t\t{0} ms\n\tcppinterp\t\t{1} ms\n\tcppinter parallel\t{2} ms".format(time_1-time_0, time_2-time_1, time_3-time_2))


plt.plot(x, y[0,:],'-',label = "True", ms =2)
plt.plot(x_new,y_new[0,:], '.:', label = "Interp", ms =2)
plt.plot(x_new,y_new_par[0,:], '-.', label = "Interp", ms =2)
plt.plot(x_new,y_np[0,:], '--', label = "Numpy", ms =2)
plt.legend(loc = "upper left")
plt.show()






