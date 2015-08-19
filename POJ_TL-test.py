#!/usr/bin/env python3

import POJ_TL
from POJ_TL import poj_tl
import unittest
class TestPOJ_TL(unittest.TestCase):
    im = [
        #1
        ['oa óa òa oah ôa ǒa ōa oa̍h ŏa',
         'oa oa2 oa3 oah oa5 oa6 oa7 oah8 oa9',
         'ua ua2 ua3 uah ua5 ua6 ua7 uah8 ua9',
         'ua uá uà uah uâ uǎ uā ua̍h ua̋'],
        #2
        ['oan oán oàn oat oân oǎn oān oa̍t oăn',
         'oan oan2 oan3 oat oan5 oan6 oan7 oat8 oan9',
         'uan uan2 uan3 uat uan5 uan6 uan7 uat8 uan9',
         'uan uán uàn uat uân uǎn uān ua̍t ua̋n'],
        #3
        ['oai oái oài oaih oâi oǎi oāi oa̍ih oăi',
         'oai oai2 oai3 oaih oai5 oai6 oai7 oaih8 oai9',
         'uai uai2 uai3 uaih uai5 uai6 uai7 uaih8 uai9',
         'uai uái uài uaih uâi uǎi uāi ua̍ih ua̋i'],
        #4
        ['oaⁿ óaⁿ òaⁿ oahⁿ ôaⁿ ǒaⁿ ōaⁿ oa̍hⁿ ŏaⁿ',
         'oaN oaN2 oaN3 oahN oaN5 oaN6 oaN7 oahN8 oaN9',
         'uann uann2 uann3 uannh uann5 uann6 uann7 uannh8 uann9',
         'uann uánn uànn uannh uânn uǎnn uānn ua̍nnh ua̋nn'],
        #5
        ['oaiⁿ oáiⁿ oàiⁿ oaihⁿ oâiⁿ oǎiⁿ oāiⁿ oa̍ihⁿ oăiⁿ',
         'oaiN oaiN2 oaiN3 oaihN oaiN5 oaiN6 oaiN7 oaihN8 oaiN9',
         'uainn uainn2 uainn3 uainnh uainn5 uainn6 uainn7 uainnh8 uainn9',
         'uainn uáinn uàinn uainnh uâinn uǎinn uāinn ua̍innh ua̋inn']
    ]

    def test_pojt_pojs_tls_tlt(self):
        for num, imgroup in enumerate(TestPOJ_TL.im):
            print("POJ => TL Testing Group %d:" % (num+1))
            self.assertEqual(poj_tl(imgroup[0]).pojt_pojs(),
                             imgroup[1],
                             'POJ調號 => POJ數字 Err')
            self.assertEqual(poj_tl(imgroup[1]).pojs_tls(),
                             imgroup[2],
                             'POJ數字 => TL數字 Err')
            self.assertEqual(poj_tl(imgroup[2]).tls_tlt(),
                             imgroup[3],
                             'TL數字 => TL調號 Err')
            self.assertEqual(poj_tl(imgroup[0]).pojt_tlt(),
                             imgroup[3],
                             'POJ調號 => TL調號 Err')
    def test_tlt_tls_pojs_pojt(self):
        for num, imgroup in enumerate(TestPOJ_TL.im):
            print("TL => POJ Testing Group %d:" % (num+1))
            self.assertEqual(poj_tl(imgroup[3]).tlt_tls(),
                             imgroup[2],
                             'TL調號 => TL數字 Err')
            self.assertEqual(poj_tl(imgroup[2]).tls_pojs(),
                             imgroup[1],
                             'TL數字 => POJ數字 Err')
            self.assertEqual(poj_tl(imgroup[1]).pojs_pojt(),
                             imgroup[0],
                             'POJ數字 => POJ調號 Err')
            self.assertEqual(poj_tl(imgroup[3]).tlt_pojt(),
                             imgroup[0],
                             'TL調號 => POJ調號 Err')


if __name__ == '__main__':
    unittest.main()
