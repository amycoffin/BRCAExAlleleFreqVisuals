import exacVcfLibrary
import matplotlib.pyplot as plt
import numpy as np

"""Given a list of ExAC alleles, a bar chart of allele frequencies is plotted, with 
subpopulations on the x axis and frequencies on the y axis"""


def plotAlleles(alleleList):
    """Given an alleleList, will produce 2 bar charts rendering allele freq
    data"""
    figureNum = 0 #will allow "figure 1" and "figure 2" to be made
    for allele in alleleList: #allele is an object with attributes
        figureNum += 1
        plotExacAllele(allele, figureNum)


def plotExacAllele(allele, figureNum):
    """given an allele, will create a bar chart for its allele frequencies"""
    labels, AFs = makeFrequencyVectors(allele)
    # labels, AFs = vectorTup[0]
    # AFs = vectorTup[1]
    sigLine = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
    xAlign = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.bar(xAlign, AFs, color='salmon')
    ax.plot(xAlign, sigLine, color = 'black')
    ax.set_ylabel('Allele Frequencies')
    ax.set_xticks(xAlign) #this is the line that made a difference for label alignment
    ax.set_xticklabels(labels)
    #ax.set_ylim((0,1))
    plt.show()

def makeFrequencyVectors(allele):
    """given an allele, will return a labels and an allele frequencies vector"""
    labels = []
    AFs = []
    subpopTups = []
    for sp in sorted(allele.pops, key=lambda p: (p.namepop,)): #FIX THIS, YOU DONT NEED subpopTups #keys, given one element in the list, returns value youa re supposed to sort on
        labels.append(sp.namepop)
        AFs.append(sp.af)
    return labels, AFs

def calcAF(subpop):
    """Given a subpop, will generate a tuple of (Name, AF)"""
    ac = float(subpop.ac)
    an = float(subpop.an)
    af = (ac/an)
    spTup = (subpop.namepop, af)
    print spTup
    return spTup


