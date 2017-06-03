#May 24 2017


import unittest
import exacVcfLibrary
import renderExacVcfAlleles


#sampleAlleles = [{'pops': [{'ac': 0, 'popname': 'FIN', 'an': 6594}, {'ac': 0, 'popname': 'SAS', 'an': 16366}, {'ac': 0, 'popname': 'AMR', 'an': 11150}, {'ac': 0, 'popname': 'AFR', 'an': 7890}, {'ac': 0, 'popname': 'OTH', 'an': 680}, {'ac': 0, 'popname': 'EAS', 'an': 7754}, {'ac': 1, 'popname': 'NFE', 'an': 52798}], 'chrom': '13', 'alt': 'G', 'ref': 'GA', 'pos': 32319059}]
#might not work bc object with attributes is diff than this....

class Test1KGFetch(unittest.TestCase):
    def test_1kGFetch(self):
        alleleList = exacVcfLibrary.vcfFetchAlleles('1kGSample.vcf.gz', 13, 32316852, 32316853)
        for allele in alleleList:
            print vars(allele)
            for subpop in allele.pops:
                print type(subpop)
        renderExacVcfAlleles.plotAlleles(alleleList)

class TestExacFetch(unittest.TestCase):
    def test_ExacFetch(self):
        alleleList = exacVcfLibrary.vcfFetchAlleles('testExac.vcf.gz', 13, 32319058, 32319059)
        for allele in alleleList:
            print vars(allele)
            for subpop in allele.pops:
                print vars(subpop)
        renderExacVcfAlleles.plotAlleles(alleleList)



if __name__ == '__main__':
    unittest.main()