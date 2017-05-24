#Amy Coffin
#May 10 2017

"""This module will open and parse ExAC's Allele Number and Allele Count data. It will use PyVcf to open the ExAC file. 
The chromosome and position number will be entered into respective attributes of an 'Allele' object; a third attribute of 
the Allele object will be the alternate nuc from the reference, and a fourth attribute will be its 'info' attribute. This 
info attribute will hold only the relevant AC, AN, and perhaps AF fields. These fields will then be retrieved from this 
Allele data structure and made into a histogram in order to represent ACs and ANs for each subpopulation."""

import vcf
import matplotlib.pyplot as plt
import numpy as np


class Allele(object):
    def __init__(self, r):
        self.chrom = r.CHROM
        self.pos = r.POS
        self.ref = r.REF
        self.alt = str(r.ALT)
        self.pops = []

class SubPop(object):
    def __init__(self, r):
        #self.all = [r.INFO['AC']]
        self.afr = (r.INFO['AC_AFR'], r.INFO['AN_AFR'])
        self.amr = (r.INFO['AC_AMR'], r.INFO['AN_AMR'])
        self.eas = (r.INFO['AC_EAS'], r.INFO['AN_EAS'])
        self.fin = (r.INFO['AC_FIN'], r.INFO['AN_FIN'])
        self.nfe = (r.INFO['AC_NFE'], r.INFO['AN_NFE'])
        self.oth = (r.INFO['AC_OTH'], r.INFO['AN_OTH'])
        self.sas = (r.INFO['AC_SAS'], r.INFO['AN_SAS'])

def calculateFreqs(object): #records get passed here
    yAFs = []
    global labels #youre going to have to create another labels list in the next
    for po in rec.pops:
        popDict = vars(po)
        labels = popDict.keys()
        labels.sort()
        for la in labels:
            tup = popDict[la]
            #print tup
            if len(tup[0]) < 2:
                for ac in tup[0]:
                    an = tup[1]
                    af = float(ac)/float(an)
                    yAFs.append(af)
    return yAFs
    #return labels

def plotFreqs(object):
    """This will unpack the records data structure and plot it. You can two other vectors if you wish to """
    yAFs = calculateFreqs(rec)
    print yAFs
    x1 = [0, 1, 2, 3, 4, 5, 6] #this is to position bars on barcharts for ACs
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.bar(xAC, yAFs, label='Bars1', color='salmon')
    ax1.set_xticklabels(labels) #feed this a label list

    plt.xlabel('subpopulations')
    plt.ylabel('ExAC Allele Frequency (Caclulated)')

    plt.show()


vcf_reader = vcf.Reader(open('4testFinalExac.vcf.gz', 'r'))

records = []
for rec in vcf_reader:
    allele = Allele(rec)
    subpop = SubPop(rec)
    allele.pops.append(subpop)
    records.append(allele)

for rec in records:
    plotFreqs(rec)

#calculateFreqs(records) #for rec in records plotStuff(rec)
#plotStuff(records)

    #this creates a janky data structure so that you could do the thing in the other program; allele should have everything you need
    # alDict = vars(allele)
    # newAlDict = {'chrom': alDict['chrom'], 'pos': alDict['pos'], 'ref': alDict['ref'], 'alt':alDict['alt']}
    # #print newAlDict
    # for item in allele.pops: #looking at ACs and ANs for current record
    #     #print item.afr
    #     popDict = {'pops': vars(item)}
    #     newAlDict.update(popDict)
    #     finalAlDict = {(allele.chrom, allele.pos): newAlDict}
    #
    # records.append(finalAlDict)


###############################################################
#THIS IS WHERE PLOTTING BEGINS, COPIED PASTED FROM EXACPLOT.PY#
###############################################################
#ONCE YOU HAVE THIS DONE, YOU NEED TO JUST USE ORIGINAL DATA STRUCTURE RATHER THAN RECORDS
# one challenge you will have with this is using a specific allele, you might want to just generate three figures
#next steps will be thinking about how to use fetch option in conjunction with a command line and ArgParser

# subpops = []
# smallfrac = 0.0001 #to avoid logs of 0
#
# for allele in records:
#     #atts = allele
#     for key, value in allele.iteritems():
#         subPopDict = value['pops']
#         subpops.append(subPopDict)
#
# bestTest = subpops[2] #picks best visualization test with nonzero data
# keyList = bestTest.keys() #makes a list that can be used for labels
# keyList.sort() #sorts for predictability since the list was pulled from a dictionary
#
# #yAC = []
# #yAN = []
#
#
# #REWRITE ALL THIS STUFF TO USE YOUR DATA STRUCTURE
# for k in keyList:
#     popTup = bestTest[k]
#     print popTup
#
#     for i in popTup[0]:
#         #print type(log(i))
#         yAC.append(float(i))
#     yAN.append(float(popTup[1]))
#
# yFrac = []
# for yindex in range(0, 7):
#     yFrac.append(yAC[yindex] / yAN[yindex])
#
# xAC = [0, 1, 2, 3, 4, 5, 6]
# #keyList.append('aaa')
# popNames =  np.append(np.roll(keyList,1), keyList[6])

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))
# ax1.bar(xAC, yFrac, label= 'Bars1', color='salmon')
# ax1.set_xticklabels(popNames)
#
#
# plt.xlabel('subpopulations')
# plt.ylabel('ExAC Allele Frequency (Caclulated)')
#
# plt.show()
#f = open('records.py', 'w')
#f.write('records = ' + str(records) + '\n')
#THESE LINES ARE FOR CREATING A DIFFERENT MODULE WITH THE RECORD LIST IN IT






#plotStuff(thing)


        #print item
    #print allele
    #temp = vars(allele)
    #for v in temp:
    #    print v
    #IT MIGHT BE A GOOD IDEA TO JUST START A NEW FOR LOOP USING RECORDLIST RATHER THAN TRYING TO UNPACK ALLELES IN THIS ONE,
    #EVEN IF IT DOES TAKE UP MORE MEMORY

    #you might want to use fetch to test your barcharts
    #the hard part of making the histograms will be getting the
    #scaling right by using maxs and mins from the data