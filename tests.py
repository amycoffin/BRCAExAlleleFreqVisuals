#May 24 2017


import unittest
import exacVcfLibrary
import renderExacVcfAlleles


#sampleAlleles = [{'pops': [{'ac': 0, 'popname': 'FIN', 'an': 6594}, {'ac': 0, 'popname': 'SAS', 'an': 16366}, {'ac': 0, 'popname': 'AMR', 'an': 11150}, {'ac': 0, 'popname': 'AFR', 'an': 7890}, {'ac': 0, 'popname': 'OTH', 'an': 680}, {'ac': 0, 'popname': 'EAS', 'an': 7754}, {'ac': 1, 'popname': 'NFE', 'an': 52798}], 'chrom': '13', 'alt': 'G', 'ref': 'GA', 'pos': 32319059}]
#might not work bc object with attributes is diff than this....

class TestVcfFetch(unittest.TestCase):
    def test_fetch(self):
        alleleList = exacVcfLibrary.vcfFetchAlleles('testExac.vcf.gz', 13, 32316434, 32316435)
        for allele in alleleList:
            print vars(allele)
            for subpop in allele.pops:
                print vars(subpop)
        renderExacVcfAlleles.plotAlleles(alleleList)
    #def test_get(self):
        #exacAlleleFreq.getCountsNums(info)


if __name__ == '__main__':
    unittest.main()