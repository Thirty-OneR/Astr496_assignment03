import numpy as np

def generate_k(T,rate=None):
    T_eV=T/11605.
    log_T_eV=np.log(T_eV)
    log_T=np.log(T)

    if rate=='reaction':
        print('k1: HI + e -> HII + 2e')
        print('k2: HII + e -> HI + p')
        print('k3: HeI + e -> HeII + 2e')
        print('k4: HeII + e -> HeI + p')
        print('k5: HeII + e -> HeIII + 2e')
        print('k6: HeIII + e -> HeII + p')
        print('k7: HI + e -> HM + p')
        print('k8: HM + HI -> H2I + e')
        print('k9: HI + HII -> H2II + p')
        print('k10: H2II + HI -> H2I* + HII')
        print('k11: H2I + HII -> H2II + HI')
        print('k12: H2I + e -> 2HI + e')
        print('k13: H2I + HI -> 3HI')
        print('k14: HM + e -> HI + 2e')
        print('k15: HM + HI -> 2HI + e')
        print('k16: HM + HII -> 2HI')
        print('k17: HM + HII -> H2II + e')
        print('k18: H2II + e -> 2HI')
        print('k19: H2II + HM -> HI + H2I')

    if rate==None:
    		print('You need to work with me here')
	
    if rate=='k1':
        k = np.exp(-32.71396786375
          + 13.53655609057*log_T_eV
          - 5.739328757388*log_T_eV**2 
          + 1.563154982022*log_T_eV**3
          - 0.2877056004391*log_T_eV**4
          + 0.03482559773736999*log_T_eV**5
          - 0.00263197617559*log_T_eV**6
          + 0.0001119543953861*log_T_eV**7
          - 2.039149852002e-6*log_T_eV**8)
    
    if rate=='k2':
        k = 4.881357e-6*T**(-1.5)* (1.+1.14813e2 * T**(-0.407))**(-2.242)
        
    if rate=='k3':
        k = np.exp(-44.09864886561001
              + 23.91596563469*log_T_eV
              - 10.75323019821*log_T_eV**2
              + 3.058038757198*log_T_eV**3
              - 0.5685118909884001*log_T_eV**4
              + 0.06795391233790001*log_T_eV**5
              - 0.005009056101857001*log_T_eV**6
              + 0.0002067236157507*log_T_eV**7
              - 3.649161410833e-6*log_T_eV**8)
        
    if rate=='k4':
        k = (1.54e-9*(1.+0.3 / 
              np.exp(8.099328789667/T_eV))
              / (np.exp(40.49664394833662/T_eV)*T_eV**1.5)
              + 3.92e-13/T_eV**0.6353)
            
    if rate=='k5':
        k = np.exp(-68.71040990212001
              + 43.93347632635*log_T_eV
              - 18.48066993568*log_T_eV**2
              + 4.701626486759002*log_T_eV**3
              - 0.7692466334492*log_T_eV**4
              + 0.08113042097303*log_T_eV**5
              - 0.005324020628287001*log_T_eV**6
              + 0.0001975705312221*log_T_eV**7
              - 3.165581065665e-6*log_T_eV**8)
        
    if rate=='k6':
        k = 7.8155e-5*T**(-1.5) * (1.+2.0189e2* T**(-0.407))**(-2.242)
                 
    if rate=='k7':
        k = 3.0e-16 * (T/(3.0e2))**0.95 * np.exp(-T/9.32e3)
         
    if rate=='k8':
        k = 1.35e-9*(T**9.8493e-2 + 3.2852e-1
         * T**5.5610e-1 + 2.771e-7 * T**2.1826)/ (1. + 6.191e-3 * T**1.0461
         + 8.9712e-11 * T**3.0424
         + 3.2576e-14 * T**3.7741)
         
    if rate=='k9':
        if (T < 30.0):
            k = 2.10e-20 * (T/30.0)**(-0.15)
        else:
            if (T > 3.2e4):
                tk9 = 3.2e4
            else:
                tk9 = T

            k = 10**(-18.20  - 3.194 * np.log10(tk9)
                + 1.786  * np.log10(tk9)**2
                - 0.2072 * np.log10(tk9)**3 ) 
    if rate=='k10':
        k=6.0e-10
        
    if rate=='k11':
        k = (np.exp(-21237.15) * 
             (- 3.3232183e-07
              + 3.3735382e-07 * log_T
              - 1.4491368e-07 * log_T**2
              + 3.4172805e-08 * log_T**3
              - 4.7813720e-09 * log_T**4
              + 3.9731542e-10 * log_T**5
              - 1.8171411e-11 * log_T**6
              + 3.5311932e-13 * log_T**7))
    if rate=='k12':
        k = 4.4886e-9*T**0.109127*np.exp(-101858./T)
    
    if rate=='k13':
        k = 1.0670825e-10*T_eV**2.012/(np.exp(4.463/T_eV)*(1.+0.2472* T_eV)**3.512)
              
    if rate=='k14':
        k = np.exp(-18.01849334273
              + 2.360852208681*log_T_eV
              - 0.2827443061704*log_T_eV**2
              + 0.01623316639567*log_T_eV**3
              - 0.03365012031362999*log_T_eV**4
              + 0.01178329782711*log_T_eV**5
              - 0.001656194699504*log_T_eV**6
              + 0.0001068275202678*log_T_eV**7
              - 2.631285809207e-6*log_T_eV**8)
    
    if rate=='k15':
        if (T_eV > 0.1):
            k = np.exp(-20.37260896533324
              + 1.139449335841631*log_T_eV
              - 0.1421013521554148*log_T_eV**2
              + 0.00846445538663*log_T_eV**3
              - 0.0014327641212992*log_T_eV**4
              + 0.0002012250284791*log_T_eV**5
              + 0.0000866396324309*log_T_eV**6
              - 0.00002585009680264*log_T_eV**7
              + 2.4555011970392e-6*log_T_eV**8
              - 8.06838246118e-8*log_T_eV**9)
        else:
            k = 2.56e-9*T_eV**1.78186
            
    if rate=='k16':
        k = 2.4e-6*(1.+T/2e4)/np.sqrt(T)
        
    if rate=='k17':
        k = 1.0e-8*T**(-0.4)
        if (T > 1.0e4):
            k=4.0e-4*T**(-1.4)*np.exp(-15100.0/T)
    
    if rate=='k18':
        k = 1.0e-8
        if (T > 617.):
            k = 1.32e-6 * T**(-0.76) 
    
    if rate=='k19':
        k = 5.0e-7*np.sqrt(100.0/T)
        
    return k
        
