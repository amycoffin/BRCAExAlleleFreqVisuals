#May 24 2017


import unittest
import exacAlleleFreq


class TestVcfFetch(unittest.TestCase):
    def test_fetch(self):
        exacAlleleFreq.exacFetch('testExac.vcf.gz', 13, 32316434, 32316435)
    #def test_get(self):
        #exacAlleleFreq.getCountsNums(info)


if __name__ == '__main__':
    unittest.main()