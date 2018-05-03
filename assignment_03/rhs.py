from Rate import generate_k
import numpy as np

def rhs(t,state):
    '''
    State should contain a list or array of number density of all particle and temperature.
    in order of:
        HI, HII, e, HeI, HeII, HeIII, HM, H2I, H2II, T
    '''
    from Rate import generate_k
    
    # extract the number density of each element including species and temp and time step and some constants
    HI=state[0]
    HII=state[1]
    e=state[2]
    HeI=state[3]
    HeII=state[4]
    HeIII=state[5]
    HM=state[6]
    H2I=state[7]
    H2II=state[8]
    T0=state[9] # temperature
    n=state[10] # total number density
    e=state[11] # total energy (assume constant during simulation)
    dt=state[12] # time step
    safety=state[13] # safety number 
    
    '''
    1: 
    '''
    
    #  get the reaction rate for convenience
    k1=generate_k(T0,rate='k1')
    k2=generate_k(T0,rate='k2')
    k3=generate_k(T0,rate='k3')
    k4=generate_k(T0,rate='k4')
    k5=generate_k(T0,rate='k5')
    k6=generate_k(T0,rate='k6')
    k7=generate_k(T0,rate='k7')
    k8=generate_k(T0,rate='k8')
    k9=generate_k(T0,rate='k9')
    k10=generate_k(T0,rate='k10')
    k11=generate_k(T0,rate='k11')
    k12=generate_k(T0,rate='k12')
    k13=generate_k(T0,rate='k13')
    k14=generate_k(T0,rate='k14')
    k15=generate_k(T0,rate='k15')
    k16=generate_k(T0,rate='k16')
    k17=generate_k(T0,rate='k17')
    k18=generate_k(T0,rate='k18')
    k19=generate_k(T0,rate='k19')
    
    # calculate the change in number density for each species
    dHIdt=-k1*HI*e-k7*HI*e-k8*HI*HM-k9*HI*HII-k10*H2II*HI-k15*HI*HM-k13*H2I*HI+k2*HII*e+k11*H2I*HII+k12*2*H2I*e\
        +k13*3*H2I*HI+k14*HM*e+k15*2*HM*HI+k16*2*HM*HII+k18*H2II*e+k19*H2II*HM
    dHIIdt=-k2*HII-k9*HI*HII-k11*H2I*HII-k16*HM*HII-k17*HM*HII+k1*HI*e+k10*H2II*HI
    dedt=+k1*HI*e-k2*HII*e+k3*HeI*e-k4*HeII*e+k5*HeII*e-k6*HeIII*e-k7*HI*e+k8*HM*HI+k14*HM*e+k15*HM*HI+k17*HM*HII-k18*H2II*e
    dHeIdt=-k3*HeI*e+k4*HeII*e
    dHeIIdt=-k4*HeII*e-k5*HeII*e+k3*HeI*e+k6*HeIII*e
    dHeIIIdt=-k6*HeIII*e+k5*HeII*e
    dHMdt=-k8*HM*HI-k14*HM*e-k15*HM*HI-k16*HM*HII-k17*HM*HII-k19*H2II*HM+k7*HI*e
    dH2Idt=-k11*H2I*HII-k12*H2I*e-k13*H2I*HI+k8*HM*HI+k10*H2II*HI+k19*H2II*HM
    dH2IIdt=-k10*H2II*HI-k18*H2II*e-k19*H2II*HM+k9*HI*HII+k11*H2I*HII+k17*HM*HII
    
    # calculate the total number density change
    dndt=dHIdt+dHIIdt+dedt+dHeIdt+dHeIIdt+dHeIIIdt+dHMdt+dH2Idt+dH2IIdt
    
    # calculate the new mean molecular weight (in atmo weight)
    mean=(1*(HI+dHIdt+HII+dHIIdt+HM+dHMdt)+2*(H2I+H2II+dH2Idt+dH2IIdt)+4*(HeI+HeII+HeIII+dHeIdt+dHeIIdt+dHeIIIdt))/(n+dndt)
    
    # calculate the change to temp assuming constant energy
    dT0dt=e*mean-T0
    
    # calculate the new time step
    candidate=[]
    d=[dHIdt,dHIIdt,dedt,dHeIdt,dHeIIdt,dHeIIIdt,dHMdt,dH2Idt,dH2IIdt]
    num=[HI+dHIdt,HII+dHIIdt,e+dedt,HeI+dHeIdt,HeII+dHeIIdt,HeIII+dHeIIIdt,HM+dHMdt,H2I+dH2Idt,H2II+dH2IIdt]
    for ind, ni in  enumerate(num):
        if ni !=0 and d[ind]!=0:
            candidate.append(abs(ni/d[ind])*safety)
    
    dt_now=min(candidate)
    dtdt=dt_now-dt
#    dT0dt=0
#    n=n+dndt
    
    return np.array([
            dHIdt,dHIIdt,dedt,dHeIdt,dHeIIdt,dHeIIIdt,dHMdt,dH2Idt,dH2IIdt,dT0dt,dndt,0, dtdt,0
    ])