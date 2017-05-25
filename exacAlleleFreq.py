#May 24 2017
#Amy Coffin

"""This is a library that will allow matplotlib visualizations to be made from vcf files"""


import vcf
import matplotlib.pyplot as plt
import numpy as np

class Allele(object): #LOOP OVER ALT FIELD AND CREATE TWO ALLELES
    """This object an allele made from a vcf record. A novel feature of this representation is 
    that it allows subpopulation data to be extracted from the record and well organized"""
    def __init__(self, chrom, pos, ref, alt):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.pops = []


class SubPop(object):
    """This object is a subpopulation that contains its name, allele counts, allele numbers, and allele frequency"""
    def __init__(self, popname, ac, an, af):
        self.ac = ac
        self.an = an
        self.af = af
        self.popname = popname


def exacFetch(vcffile, chr, start, end):
    """This will read the record in the Exac vcf according to the chromosome and position entered organizes 
    allele attributes"""
    vcfReader = vcf.Reader(filename=vcffile)
    for rec in vcfReader.fetch(chr, start, end):
        chrom = rec.CHROM
        pos = rec.POS
        ref = rec.REF
        alt = rec.ALT
        info =  rec.INFO
        aleTup = (chrom, pos, ref, alt, info)
    return aleTup

def getCountsAndNums(aleTup): #not sure how to pass info field to this function
    """This function further organizes allele attributes to obtain allele counts and allele numbers"""
    acfields = []
    anfields = []
    acs = []
    ans = []
    popNames = []
    for item in aleTup:
        try:
            keyCheck = item.keys()
            info =  item
        except:
            continue

    for field in info.keys():
        if field[0:3] == 'AC_' and field.isupper() and len(field) < 7:
            acfields.append(field)
        if field[0:3] == 'AN_' and field.isupper() and len(field) < 7:
            anfields.append(field)
    for ac in acfields:
        acValue = info[ac]
        label = ac[3:]
        acs.append(acValue)
        popNames.append(label)
    for an in anfields:
        anValue = info[an]
        ans.append(anValue)
    return (acs, ans, popNames)

def calcFreqs(acs, ans):
    pass

def plotFreqs():
    pass

#exacFetch('testExac.vcf.gz', 13, 32316434, 32316435)
getCountsAndNums(exacFetch('testExac.vcf.gz', 13, 32316434, 32316435))


#have script do the compressing
#write a function that returns a set of populations