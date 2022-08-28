# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


class DFT():
    
    def __init__(self):
        
        pass


    def bands(self,file):
        
    
        data=np.loadtxt(str(file) +".out")
        k = np.unique(data[:,0])
    
        bands = np.reshape(data[:,1],(-1,len(k)))

        ##################################################################
        figure = plt.figure()
        Ef=-4.015

        for band in range(len(bands)):
            plt.plot(k,bands[band,:]-Ef, '-', color='black')
    
        plt.xlabel(r'k-path',fontsize=11)
        plt.ylabel(r'Energy (eV)', fontsize=11)
        plt.xlim(min(k),max(k))
        plt.ylim([-1.4,1.4])

        G_0= data[:,0].min() #GAMMA POINT
        M=0.096924
        K=0.152883
        G_1= data[:,0].max() #GAMMA POINT

        plt.axhline(G_0,linestyle=(0,(5,5)),linewidth=0.75,color='k',alpha=0.5)
        plt.axvline(M,linewidth=0.75,color='k',alpha=0.5)
        plt.axvline(K,linewidth=0.75,color='k',alpha=0.5)
        plt.axvline(G_1,linewidth=0.75,color='k',alpha=0.5)
        plt.xticks(ticks = [G_0,M,K,G_1], labels =[r'$\mathsf{\Gamma}$', r'M', r'K', r'$\mathsf{\Gamma}$'])

        figure.set_size_inches(3.375, 3.375)
        figure.savefig(str(file)+'.pdf', dpi=300, bbox_inches="tight")
        
plot=DFT()
plot.bands("Graphene_pristine")      
        
