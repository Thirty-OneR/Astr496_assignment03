import numpy as np
import matplotlib.pyplot as plt
from Rate import generate_k
from rhs import rhs
import scipy.integrate as sint

# This is the code cell for inputing all necessary initial condition
HII_frac=0.6 # Hydro
HeII_frac=0.2
HeIII_frac=0.1
HM_frac=0.1
int_method=None
T=10000
n_total=100000 #density
final_t=10**5

# some constant
k=1.38*10**(-23) # boltzmann constant
gamma=1.5 
mh=1.6737236*10**(-27) # hydrogen mass

# following codes calculate the number density taking in consideration of electron
total=HII_frac*2+HeII_frac+3*HeIII_frac+HM_frac

HII_frac=HII_frac/total
HeII_frac=HeII_frac/total
HeIII_frac=HeIII_frac/total
HM_frac=HM_frac/total
e_frac=1-HII_frac-HeII_frac-HeIII_frac-HM_frac

# setting initial temprature
T0=T
e=T0/((gamma-1)*(n_total*HII_frac*1+4*n_total*HeII_frac+4*n_total*HeIII_frac+1*n_total*HM_frac)/(n_total)*mh)

# setting safety number for simulation
safety=1000

# set the initial element for the simulation
final_t = final_t#*365*24*3600
n_HII_initial = n_total * HII_frac
n_HeII_initial = n_total * HeII_frac
n_HeIII_initial=n_total*HeIII_frac
n_HM_initial = n_total * HM_frac
n_e_initial = n_total * e_frac


# create the integrator
integrator = sint.ode(rhs)

#set the integration method if there is any
if int_method!=None:
    integrator.set_integrator(int_method)

state_vector_values = []
ts = []
state_vector = np.array([0,n_HII_initial , n_e_initial, 0, n_HeII_initial, n_HeIII_initial, 0,  n_HM_initial, 0, T0,n_total,e*((gamma-1)*mh),0,safety])
initial_d=rhs(0,state_vector)
candidate=[]
for ind,num_den in enumerate(state_vector[:9]):
    if num_den!=0 and initial_d[ind] != 0:
        candidate.append(abs(num_den/initial_d[ind])*safety)
dt=min(candidate)
print(dt)

state_vector = np.array([0,n_HII_initial , n_e_initial, 0, n_HeII_initial, n_HeIII_initial, 0,  n_HM_initial, 0, T0,n_total,e*((gamma-1)*mh),dt,safety])
integrator.set_initial_value(state_vector, t=0)
ts.append(integrator.t)

state_vector_values.append(integrator.y)
while integrator.t < final_t:
    integrator.integrate(integrator.t+dt)
    ts.append(integrator.t)
    state_vector_values.append(integrator.y)
    dt=integrator.y[-2]
    print(integrator.t,dt)

state_vector_values = np.array(state_vector_values)
ts = np.array(ts)

# plotting
plt.clf()
plt.loglog(ts, state_vector_values[:,0], label='HI')
plt.loglog(ts, state_vector_values[:,1], label='HII')
plt.loglog(ts, state_vector_values[:,2], label='e')
plt.loglog(ts, state_vector_values[:,3], label='HeI')
plt.loglog(ts, state_vector_values[:,4], label='HeII')
plt.loglog(ts, state_vector_values[:,5], label='HeIII')
plt.loglog(ts, state_vector_values[:,6], label='HM')
plt.loglog(ts, state_vector_values[:,7], label='H2I')
plt.loglog(ts, state_vector_values[:,8], label='H2II')
plt.loglog(ts, state_vector_values[:,10], label='total')

plt.ylim(10**(-10),10**10)

plt.xlabel("Time [s]")
plt.ylabel("n")
plt.title('Number density versus time')
plt.legend()
plt.savefig('Number Density Plot')