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
        plotAllele(allele, figureNum)


def plotAllele(allele, figureNum):
    """given an allele, will create a bar chart for its allele frequencies"""
    vectorTup = makePlottingVectors(allele)
    labels = vectorTup[0]
    AFs = vectorTup[1]
    print AFs
    xAlign = np.arange(len(labels))
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    ax1.bar(xAlign, AFs, label= 'Bars1', color='salmon')
    plt.show()

def makePlottingVectors(allele):
    """given an allele, will return a labels and an allele frequencies vector"""
    labels = []
    AFs = []
    subpopTups = []
    for sp in allele.pops:
        spTup = calcAFs(sp)
        subpopTups.append(spTup)
    subpopTups.sort()
    for tup in subpopTups:
        labels.append(tup[0])
        AFs.append(tup[1])
    subpopTups = []
    return labels, AFs

def calcAFs(subpop):
    """Given a subpop, will generate a tuple of (Name, AF)"""
    ac = float(subpop.ac)
    print ac
    an = float(subpop.an)
    print an
    af = (ac/an)
    spTup = (subpop.popname, af)
    print spTup
    return spTup


chrom = 13
start = 32316434
end = 32316435
#exacVcfLibrary.vcfFetchAlleles('testExac.vcf.gz', chrom, start, end)

