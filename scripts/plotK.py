from reactions import Reaction
import matplotlib.pyplot as plt
import numpy as np

def plotKElementary(r,Tmin,Tmax):
    if(r.isPressureLog==False and r.isLindemann==False and r.isTroe==False):
        A=r.lnA
        b=r.beta
        eOverR=r.eOverR
        T=np.arange(Tmin,Tmax,1)
        k=A*(T**b)*np.exp(-eOverR/T)
        plt.plot(1/T,k)
        plt.yscale('log')
        plt.xlabel('Temperature')
        plt.ylabel('Forward reaction rate')
        plt.show()
    else:
        print('The reaction is not Elementary or ThreeBody')

