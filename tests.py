#May 24 2017


import unittest
import exacVcfLibrary



class TestVcfFetch(unittest.TestCase):
    def test_fetch(self):
        alleleList = exacVcfLibrary.vcfFetchAlleles('testExac.vcf.gz', 13, 32319058, 32319059)
        for allele in alleleList:
            print vars(allele)
            for subpop in allele.pops:
                print vars(subpop)
    #def test_get(self):
        #exacAlleleFreq.getCountsNums(info)


if __name__ == '__main__':
    unittest.main()