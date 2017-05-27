import vcf

class Allele(object):
    """This object an allele made from a vcf record. A novel feature of this representation is 
    that it allows subpopulation data to be extracted from the record and well organized"""
    def __init__(self, chrom, pos, ref, alt): #chrom pos ref and alt might be passed here actualyl
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.pops = []

class SubPop(object):
    """This object is a subpopulation that contains its name, allele counts, allele numbers, and allele frequency"""
    def __init__(self, popname, ac, an):
        self.ac = ac
        self.an = an
        #self.af = af
        self.popname = popname

def vcfFetchAlleles(vcffile, chrom, start, end):
    """Converts a range of vcf file records into Allele objects"""
    vcfReader = vcf.Reader(filename=vcffile)
    alleleList = []
    for vcfrec in vcfReader.fetch(chrom, start, end):
        alleleList.extend(vcfRecToAlleles(vcfrec))
    return alleleList

def vcfRecToAlleles(vcfrec):
    """Converts record objects to a list allele objects"""
    alleleList = []
    for altindex in xrange(len(vcfrec.ALT)):
        allele = vcfAltToAllele(vcfrec, altindex)
        alleleList.append(allele)
    return alleleList

def vcfAltToAllele(vcfrec, altindex):
    "Converts a single record to a fully characterized (?) allele object"
    allele = Allele(vcfrec.CHROM, vcfrec.POS, vcfrec.REF, vcfrec.ALT[altindex])
    popList = vcfRecToPopNames(vcfrec)
    print popList
    for popname in popList:
        subpop = vcfToSubpop(vcfrec, altindex, popname)
        allele.pops.append(subpop)
    return allele

def vcfRecToPopNames(vcfrec):
    """Generates a list of population names from the record object"""
    popList = []
    info = vcfrec.INFO
    for field in info.keys():
        if field[0:3] == 'AC_' and field.isupper() and len(field) < 7:
            popList.append(field[3:])
    return popList

def vcfToSubpop(vcfrec, altindex, popname):
    """Returns a subpop object with AC and AN fields from info column of vcf"""
    acs = vcfrec.INFO["AC_" + popname]
    subpop = SubPop(popname, acs[altindex], vcfrec.INFO["AN_" + popname]) #ACs are list type, ANs are int type
    return subpop




