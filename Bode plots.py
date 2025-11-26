

import math
import matplotlib.pyplot as plt
import numpy as np


def gainlp(omega,RC):
    gain = 1/(1+(RC*omega)**2)
    return gain
    
def phaselp(omega,RC):
    phase = -(np.atan(RC*omega))
    return phase

def gainhp(omega, RC):
    gain = omega/(omega**2+(1/RC)**2)**0.5
    return gain

def phasehp(omega,RC):
    phase = (math.pi/2)-np.atan(RC*omega)
    return phase

def bodeplotlp(RC):
    cutoff = 1/(RC*2*math.pi)
    omega = np.linspace(10**3,10**7,10000)
    frequency = omega/(2*math.pi)
    cutofffrequncy = np.full(len(omega), cutoff)
    gain = gainlp(omega,RC)
    phase = np.rad2deg(phaselp(omega,RC))
    dB = 20*np.log10(gain)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(frequency,dB,label='Lowpass-filter gain')
    ax1.plot(cutofffrequncy,dB,linestyle='dashed')
    ax1.set_xscale('log')
    ax1.set_ylabel('Gain [dB]')
    ax1.set_xticks([1000,24.11*10**3,10**6],['$f_1$','$f_c$','$f_2$'])
    ax1.set_xlim(left=800,right=10**6+10**5)
    ax1.legend()
    ax2.plot(frequency,phase,label='Lowpass-filter phase')
    ax2.plot(cutofffrequncy,phase,linestyle='dashed')
    ax2.set_ylabel('Phase [deg]')
    ax2.set_xlabel('Frequency')
    ax2.set_xscale('log')
    ax2.set_xticks([1000,24.11*10**3,10**6],['$f_1$','$f_c$','$f_2$'])
    ax2.set_xlim(left=800,right=10**6+10**5)
    ax2.legend()
    plt.show

def bodeplothp(RC):
    cutoff = 1/(RC*2*math.pi)
    omega = np.linspace(10,10**7,10000)
    frequency = omega/(2*math.pi)
    cutofffrequncy = np.full(len(omega), cutoff)
    gain = gainhp(omega,RC)
    phase = np.rad2deg(phasehp(omega,RC))
    dB = 20*np.log10(gain)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(frequency,dB,label='Highpass-filter gain',color='red')
    ax1.plot(cutofffrequncy,dB,linestyle='dashed',color='green')
    ax1.set_xscale('log')
    ax1.set_ylabel('Gain [dB]')
    ax1.set_xticks([1000,24.11*10**3,10**6],['$f_1$','$f_c$','$f_2$'])
    ax1.set_xlim(left=800,right=10**6+10**5)
    ax1.legend()
    ax2.plot(frequency,phase,label='Highpass-filter phase',color='red')
    ax2.plot(cutofffrequncy,phase,linestyle='dashed',color='green')
    ax2.set_ylabel('Phase [deg]')
    ax2.set_xlabel('Frequency')
    ax2.set_xscale('log')
    ax2.set_xticks([1000,24.11*10**3,10**6],['$f_1$','$f_c$','$f_2$'])
    ax2.set_xlim(left=800,right=10**6+10**5)
    ax2.legend()
    plt.show

bodeplotlp(0.0000066)
bodeplothp(0.0000066)
    
    




    