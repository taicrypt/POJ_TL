#!/usr/bin/env python3
""" 白話字POJ vs. 台羅TL 轉換家私

       POJtiau_2_POJsoo       POJsoo_2_TLsoo      TLsoo_2_TLtiau
POJ調符--------------->POJ數字------------->TL數字------------->TL調符
  |    <--------------        <------------       <------------    |
  |    POJsoo_2_POJtiau       TLsoo_2_POJsoo      TLtiau_2_TLsoo   |
  |                                                                |
  |>----------------->  POJtiau_2_TLtiau  >----------------------->|
  |<-----------------<  TLtiau_2_POJtiau  <-----------------------<|

"""

# The above function names, if not mentioned in `__all__`,
# are not yet implemented.
__all__ = ["POJtiau_2_POJsoo", "POJsoo_2_TLsoo", "TLsoo_2_TLtiau",
           "TLtiau_2_TLsoo", "TLsoo_2_POJsoo", "POJsoo_2_POJtiau"]

__author__ = "潘科元"
__version__ = "0.0.2"
__date__ = "2015-06-18"
__version__ = "0.0.6"
__date__ = "2015-06-21"

import re

#--------POJtiau_2_POJsoo---------------------------------------------------#
def RC(poj):
    return re.compile(poj + r'([aAeEgGhHiIkKmMnNoOpPtTuU]*)')


# POJ調符(Tiauhu)式 -> POJ數字(Sooji)式 mapping
POJ_T2S = [
    (RC(r'á'), r'a\g<1>2'), (RC(r'Á'), r'A\g<1>2'),
    (RC(r'à'), r'a\g<1>3'), (RC(r'À'), r'A\g<1>3'),
    (RC(r'â'), r'a\g<1>5'), (RC(r'Â'), r'A\g<1>5'),
    (RC(r'ǎ'), r'a\g<1>6'), (RC(r'Ǎ'), r'A\g<1>6'),
    (RC(r'ā'), r'a\g<1>7'), (RC(r'Ā'), r'A\g<1>7'),
    (RC(r'a̍'), r'a\g<1>8'), (RC(r'A̍'), r'A\g<1>8'),
    (RC(r'ă'), r'a\g<1>9'), (RC(r'Ă'), r'A\g<1>9'),
    (RC(r'é'), r'e\g<1>2'), (RC(r'É'), r'E\g<1>2'),
    (RC(r'è'), r'e\g<1>3'), (RC(r'È'), r'E\g<1>3'),
    (RC(r'ê'), r'e\g<1>5'), (RC(r'Ê'), r'E\g<1>5'),
    (RC(r'ě'), r'e\g<1>6'), (RC(r'Ě'), r'E\g<1>6'),
    (RC(r'ē'), r'e\g<1>7'), (RC(r'Ē'), r'E\g<1>7'),
    (RC(r'e̍'), r'e\g<1>8'), (RC(r'E̍'), r'E\g<1>8'),
    (RC(r'ĕ'), r'e\g<1>9'), (RC(r'Ĕ'), r'E\g<1>9'),
    (RC(r'í'), r'i\g<1>2'), (RC(r'Í'), r'I\g<1>2'),
    (RC(r'ì'), r'i\g<1>3'), (RC(r'Ì'), r'I\g<1>3'),
    (RC(r'î'), r'i\g<1>5'), (RC(r'Î'), r'I\g<1>5'),
    (RC(r'ǐ'), r'i\g<1>6'), (RC(r'Ǐ'), r'I\g<1>6'),
    (RC(r'ī'), r'i\g<1>7'), (RC(r'Ī'), r'I\g<1>7'),
    (RC(r'i̍'), r'i\g<1>8'), (RC(r'I̍'), r'I\g<1>8'),
    (RC(r'ĭ'), r'i\g<1>9'), (RC(r'Ĭ'), r'I\g<1>9'),
    (RC(r'o͘'), r'ou\g<1>'), (RC(r'O͘'), r'Ou\g<1>'),
    (RC(r'ó͘'), r'ou\g<1>2'), (RC(r'Ó͘'), r'Ou\g<1>2'),
    (RC(r'ò͘'), r'ou\g<1>3'), (RC(r'Ò͘'), r'Ou\g<1>3'),
    (RC(r'ô͘'), r'ou\g<1>5'), (RC(r'Ô͘'), r'Ou\g<1>5'),
    (RC(r'ǒ͘'), r'ou\g<1>6'), (RC(r'Ǒ͘'), r'Ou\g<1>6'),
    (RC(r'ō͘'), r'ou\g<1>7'), (RC(r'Ō͘'), r'Ou\g<1>7'),
    (RC(r'o̍͘'), r'ou\g<1>8'), (RC(r'O̍͘'), r'Ou\g<1>8'),
    (RC(r'ŏ͘'), r'ou\g<1>9'), (RC(r'Ŏ͘'), r'Ou\g<1>9'),
    (RC(r'ó'), r'o\g<1>2'), (RC(r'Ó'), r'O\g<1>2'),
    (RC(r'ò'), r'o\g<1>3'), (RC(r'Ò'), r'O\g<1>3'),
    (RC(r'ô'), r'o\g<1>5'), (RC(r'Ô'), r'O\g<1>5'),
    (RC(r'ǒ'), r'o\g<1>6'), (RC(r'Ǒ'), r'O\g<1>6'),
    (RC(r'ō'), r'o\g<1>7'), (RC(r'Ō'), r'O\g<1>7'),
    (RC(r'o̍'), r'o\g<1>8'), (RC(r'O̍'), r'O\g<1>8'),
    (RC(r'ŏ'), r'o\g<1>9'), (RC(r'Ŏ'), r'O\g<1>9'),
    (RC(r'ú'), r'u\g<1>2'), (RC(r'Ú'), r'U\g<1>2'),
    (RC(r'ù'), r'u\g<1>3'), (RC(r'Ù'), r'U\g<1>3'),
    (RC(r'û'), r'u\g<1>5'), (RC(r'Û'), r'U\g<1>5'),
    (RC(r'ǔ'), r'u\g<1>6'), (RC(r'Ǔ'), r'U\g<1>6'),
    (RC(r'ū'), r'u\g<1>7'), (RC(r'Ū'), r'U\g<1>7'),
    (RC(r'u̍'), r'u\g<1>8'), (RC(r'U̍'), r'U\g<1>8'),
    (RC(r'ŭ'), r'u\g<1>9'), (RC(r'Ŭ'), r'U\g<1>9'),
    (RC(r'ḿ'), r'm\g<1>2'), (RC(r'Ḿ'), r'M\g<1>2'),
    (RC(r'm̀'), r'm\g<1>3'), (RC(r'M̀'), r'M\g<1>3'),
    (RC(r'm̂'), r'm\g<1>5'), (RC(r'M̂'), r'M\g<1>5'),
    (RC(r'm̌'), r'm\g<1>6'), (RC(r'M̌'), r'M\g<1>6'),
    (RC(r'm̄'), r'm\g<1>7'), (RC(r'M̄'), r'M\g<1>7'),
    (RC(r'm̍'), r'm\g<1>8'), (RC(r'M̍'), r'M\g<1>8'),
    (RC(r'm̆'), r'm\g<1>9'), (RC(r'M̆'), r'M\g<1>9'),
    (RC(r'ń'), r'n\g<1>2'), (RC(r'Ń'), r'N\g<1>2'),
    (RC(r'ǹ'), r'n\g<1>3'), (RC(r'Ǹ'), r'N\g<1>3'),
    (RC(r'n̂'), r'n\g<1>5'), (RC(r'N̂'), r'N\g<1>5'),
    (RC(r'ň'), r'n\g<1>6'), (RC(r'Ň'), r'N\g<1>6'),
    (RC(r'n̄'), r'n\g<1>7'), (RC(r'N̄'), r'N\g<1>7'),
    (RC(r'n̍'), r'n\g<1>8'), (RC(r'N̍'), r'N\g<1>8'),
    (RC(r'n̆'), r'n\g<1>9'), (RC(r'N̆'), r'N\g<1>9')
]

def POJtiau_2_POJsoo(poj_tiau, nasal='N'):
    """白話字調符式 => 白話字數字式
       if nasal == 'nn', change POJ nasal N to nn
       elif nasal == 'N', keep POJ nasal N intact
    """
    if not poj_tiau:
        return ''

    poj_sooji = ''
    if nasal == 'nn':
        poj_sooji = re.sub(r'ⁿ', r'nn', poj_tiau)
    else:
        poj_sooji = re.sub(r'ⁿ', r'N', poj_tiau)

    for tiauhusik, soojisik in POJ_T2S:
        poj_sooji = tiauhusik.sub(soojisik, poj_sooji)

    return poj_sooji

#------POJsoo_2_TLsoo-----------------------------------------------------#

def POJsoo_2_TLsoo(poj_soo, nasal='nn'):
    """白話字數字式 => 台羅數字式
       if nasal == 'nn', change POJ nasal N to nn
       elif nasal == 'N', keep POJ nasal N intact
    """
    if not poj_soo:
        return ''

    tailo = poj_soo

    if nasal == 'N':
        tailo = re.sub(r'ou(h?)(?:N|nn)(\d?)', r'oN\1\2', tailo)
        tailo = re.sub(r'(?<=[aeiouAEIOU])(h?)(?:N|nn)(\d?)', r'N\1\2', tailo)
        # non-canonical POJ nasal form: Nh rather than hN
        #tailo = re.sub(r'(?<=[aeiou])(?:N|nn)(h?\d?)', r'N\1', tailo)

    else:  # default `nn` for vowel nasaliztion
        tailo = re.sub(r'ou(h?)(?:N|nn)(\d?)', r'onn\1\2', tailo)
        tailo = re.sub(r'(?<=[aeiouAEIOU])(h?)(?:N|nn)(\d?)', r'nn\1\2', tailo)
        # non-canonical POJ nasal form: Nh rather than hN
        #tailo = re.sub(r'(?<=[aeiou])(?:N|nn)(h?\d?)', r'nn\1', tailo)

    poj2tailo = {
        'ch': 'ts', 'Ch': 'Ts', 
        'ou': 'oo', 'Ou': 'Oo', 'oa': 'ua', 'Oa': 'Ua', 'oe': 'ue', 'Oe': 'Ue',
        'eng': 'ing', 'Eng': 'Ing', 'ek': 'ik', 'Ek': 'Ik',
    }

    for k, v in poj2tailo.items():
        tailo = tailo.replace(k, v)


    return tailo

#--------TLsoo_2_TLtiau-----------------------------------------------------#

# 台羅音節尾
TL_bue = '((?:rm|rng|rn|r|m|ng|n|nnh|nn|ⁿ|N)?)'

# 處理非入聲
def RC1(tailo):
    return re.compile(tailo[:-1] + TL_bue + tailo[-1])

# 用佇 ai[1-9], au[1-9] 因為調號囥佇頭前个雙母音，著愛另外處理
def RC2(tailo):
    return re.compile(tailo[0] + '(u|i)((?:nn|ⁿ|N)?)' + tailo[1])

# 簡單情形
def RC3(tailo):
    return re.compile(tailo)

# 處理第四聲
def RC4(tailo):
    return re.compile(tailo[:-1] + '((?:nn)?h|p|t|k)' + tailo[-1] + '?')

# 處理第八聲
def RC8(tailo):
    return re.compile(tailo[:-1] + r'((?:nn)?h|p|t|k)' + tailo[-1])

# 台羅(TL)數字(Sooji)式 -> 台羅調符(Tiauhu)式 mapping
TL_S2T = [
    # use RC2
    (RC2('a1'), r'a\1\2'), (RC2('A1'), r'A\1\2'),
    (RC2('a2'), r'á\1\2'), (RC2('A2'), r'Á\1\2'),
    (RC2('a3'), r'à\1\2'), (RC2('A3'), r'À\1\2'),
    # use RC3
    (RC3('a(i|u)((?:nn|ⁿ|N)?)h4'), r'a\1\2h'),
    (RC3('A(i|u)((?:nn|ⁿ|N)?)h4'), r'A\1\2h'),
    # use RC2
    (RC2('a5'), r'â\1\2'), (RC2('A5'), r'Â\1\2'),
    (RC2('a6'), r'ǎ\1\2'), (RC2('A6'), r'Ǎ\1\2'),
    (RC2('a7'), r'ā\1\2'), (RC2('A7'), r'Ā\1\2'),
    # use RC3
    (RC3('a(i|u)((?:nn|ⁿ|N)?)h8'), r'a̍\1\2h'),
    (RC3('A(i|u)((?:nn|ⁿ|N)?)h8'), r'A̍\1\2h'),
    # use RC2
    (RC2('a9'), r'a̋\1\2'), (RC2('A9'), r'A̋\1\2'),

    # use RC1
    (RC1('a1'), r'a\1'), (RC1('A1'), r'A\1'),
    (RC1('a2'), r'á\1'), (RC1('A2'), r'Á\1'),
    (RC1('a3'), r'à\1'), (RC1('A3'), r'À\1'),
    (RC4('a4'), r'a\1'), (RC4('A4'), r'A\1'),
    (RC1('a5'), r'â\1'), (RC1('A5'), r'Â\1'),
    (RC1('a6'), r'ǎ\1'), (RC1('A6'), r'Ǎ\1'),
    (RC1('a7'), r'ā\1'), (RC1('A7'), r'Ā\1'),
    (RC8('a8'), r'a̍\1'), (RC8('A8'), r'A̍\1'),
    (RC1('a9'), r'a̋\1'), (RC1('A9'), r'A̋\1'),
    (RC1('e1'), r'e\1'), (RC1('E1'), r'E\1'),
    (RC1('e2'), r'é\1'), (RC1('E2'), r'É\1'),
    (RC1('e3'), r'è\1'), (RC1('E3'), r'È\1'),
    (RC4('e4'), r'e\1'), (RC4('E4'), r'E\1'),
    (RC1('e5'), r'ê\1'), (RC1('E5'), r'Ê\1'),
    (RC1('e6'), r'ě\1'), (RC1('E6'), r'Ě\1'),
    (RC1('e7'), r'ē\1'), (RC1('E7'), r'Ē\1'),
    (RC8('e8'), r'e̍\1'), (RC8('E8'), r'E̍\1'),
    (RC1('e9'), r'e̋\1'), (RC1('E9'), r'E̋\1'),
    (RC1('i1'), r'i\1'), (RC1('I1'), r'I\1'),
    (RC1('i2'), r'í\1'), (RC1('I2'), r'Í\1'),
    (RC1('i3'), r'ì\1'), (RC1('I3'), r'Ì\1'),
    (RC4('i4'), r'i\1'), (RC4('I4'), r'I\1'),
    (RC1('i5'), r'î\1'), (RC1('I5'), r'Î\1'),
    (RC1('i6'), r'ǐ\1'), (RC1('I6'), r'Ǐ\1'),
    (RC1('i7'), r'ī\1'), (RC1('I7'), r'Ī\1'),
    (RC8('i8'), r'i̍\1'), (RC8('I8'), r'I̍\1'),
    (RC1('i9'), r'i̋\1'), (RC1('I9'), r'I̋\1'),
    (RC1('oo1'), r'oo\1'), (RC1('Oo1'), r'Oo\1'),
    (RC1('oo2'), r'óo\1'), (RC1('Oo2'), r'Óo\1'),
    (RC1('oo3'), r'òo\1'), (RC1('Oo3'), r'Òo\1'),
    (RC4('oo4'), r'oo\1'), (RC4('Oo4'), r'Oo\1'),
    (RC1('oo5'), r'ôo\1'), (RC1('Oo5'), r'Ôo\1'),
    (RC1('oo6'), r'ǒo\1'), (RC1('Oo6'), r'Ǒo\1'),
    (RC1('oo7'), r'ōo\1'), (RC1('Oo7'), r'Ōo\1'),
    (RC8('oo8'), r'o̍o\1'), (RC8('Oo8'), r'O̍o\1'),
    (RC1('oo9'), r'őo\1'), (RC1('Oo9'), r'Őo\1'),
    (RC1('o1'), r'o\1'), (RC1('O1'), r'O\1'),
    (RC1('o2'), r'ó\1'), (RC1('O2'), r'Ó\1'),
    (RC1('o3'), r'ò\1'), (RC1('O3'), r'Ò\1'),
    (RC4('o4'), r'o\1'), (RC4('O4'), r'O\1'),
    (RC1('o5'), r'ô\1'), (RC1('O5'), r'Ô\1'),
    (RC1('o6'), r'ǒ\1'), (RC1('O6'), r'Ǒ\1'),
    (RC1('o7'), r'ō\1'), (RC1('O7'), r'Ō\1'),
    (RC8('o8'), r'o̍\1'), (RC8('O8'), r'O̍\1'),
    (RC1('o9'), r'ő\1'), (RC1('O9'), r'Ő\1'),
    (RC1('u1'), r'u\1'), (RC1('U1'), r'U\1'),
    (RC1('u2'), r'ú\1'), (RC1('U2'), r'Ú\1'),
    (RC1('u3'), r'ù\1'), (RC1('U3'), r'Ù\1'),
    (RC4('u4'), r'u\1'), (RC4('U4'), r'U\1'),
    (RC1('u5'), r'û\1'), (RC1('U5'), r'Û\1'),
    (RC1('u6'), r'ǔ\1'), (RC1('U6'), r'Ǔ\1'),
    (RC1('u7'), r'ū\1'), (RC1('U7'), r'Ū\1'),
    (RC8('u8'), r'u̍\1'), (RC8('U8'), r'U̍\1'),
    (RC1('u9'), r'ű\1'), (RC1('U9'), r'Ű\1'),

    # use RC3
    (RC3('m1'), r'm'), (RC3('M1'), r'M'),
    (RC3('m2'), r'ḿ'), (RC3('M2'), r'Ḿ'),
    (RC3('m3'), r'm̀'), (RC3('M3'), r'M̀'),
    (RC3('mh4'), r'mh'), (RC3('Mh4'), r'Mh'),
    (RC3('m5'), r'm̂'), (RC3('M5'), r'M̂'),
    (RC3('m6'), r'm̌'), (RC3('M6'), r'M̌'),
    (RC3('m7'), r'm̄'), (RC3('M7'), r'M̄'),
    (RC3('mh8'), r'm̍h'), (RC3('Mh8'), r'M̍h'),
    (RC3('m9'), r'm̋'), (RC3('M9'), r'M̋'),

    (RC3('ng1'), r'ng'), (RC3('Ng1'), r'Ng'),
    (RC3('ng2'), r'ńg'), (RC3('Ng2'), r'Ńg'),
    (RC3('ng3'), r'ǹg'), (RC3('Ng3'), r'Ǹg'),
    (RC3('ngh4'), r'ngh'), (RC3('Ngh4'), r'Ngh'),
    (RC3('ng5'), r'n̂g'), (RC3('Ng5'), r'N̂g'),
    (RC3('ng6'), r'ňg'), (RC3('Ng6'), r'Ňg'),
    (RC3('ng7'), r'n̄g'), (RC3('Ng7'), r'N̄g'),
    (RC3('ngh8'), r'n̍gh'), (RC3('Ngh8'), r'N̍gh'),
    (RC3('ng9'), r'n̋g'), (RC3('Ng9'), r'N̋g')
]

def TLsoo_2_TLtiau(tl_soo):
    if tl_soo == '':
        return ''
    tl_tiau = tl_soo
    #counter = 0
    for soojisik, tiauhusik in TL_S2T:
        #counter += 1
        tl_tiau = soojisik.sub(tiauhusik, tl_tiau)
        #print('c(%d): %s' % (counter, tl_tiau))

    return tl_tiau
        
#-------TLtiau_2_TLsoo------------------------------------------------------#

# TL調符(Tiauhu)式 -> TL數字(Sooji)式 mapping
TL_T2S = [
    (RC(r'á'), r'a\g<1>2'), (RC(r'Á'), r'A\g<1>2'),
    (RC(r'à'), r'a\g<1>3'), (RC(r'À'), r'A\g<1>3'),
    (RC(r'â'), r'a\g<1>5'), (RC(r'Â'), r'A\g<1>5'),
    (RC(r'ǎ'), r'a\g<1>6'), (RC(r'Ǎ'), r'A\g<1>6'),
    (RC(r'ā'), r'a\g<1>7'), (RC(r'Ā'), r'A\g<1>7'),
    (RC(r'a̍'), r'a\g<1>8'), (RC(r'A̍'), r'A\g<1>8'),
    (RC(r'a̋'), r'a\g<1>9'), (RC(r'A̋'), r'A\g<1>9'),
    (RC(r'é'), r'e\g<1>2'), (RC(r'É'), r'E\g<1>2'),
    (RC(r'è'), r'e\g<1>3'), (RC(r'È'), r'E\g<1>3'),
    (RC(r'ê'), r'e\g<1>5'), (RC(r'Ê'), r'E\g<1>5'),
    (RC(r'ě'), r'e\g<1>6'), (RC(r'Ě'), r'E\g<1>6'),
    (RC(r'ē'), r'e\g<1>7'), (RC(r'Ē'), r'E\g<1>7'),
    (RC(r'e̍'), r'e\g<1>8'), (RC(r'E̍'), r'E\g<1>8'),
    (RC(r'e̋'), r'e\g<1>9'), (RC(r'E̋'), r'E\g<1>9'),
    (RC(r'í'), r'i\g<1>2'), (RC(r'Í'), r'I\g<1>2'),
    (RC(r'ì'), r'i\g<1>3'), (RC(r'Ì'), r'I\g<1>3'),
    (RC(r'î'), r'i\g<1>5'), (RC(r'Î'), r'I\g<1>5'),
    (RC(r'ǐ'), r'i\g<1>6'), (RC(r'Ǐ'), r'I\g<1>6'),
    (RC(r'ī'), r'i\g<1>7'), (RC(r'Ī'), r'I\g<1>7'),
    (RC(r'i̍'), r'i\g<1>8'), (RC(r'I̍'), r'I\g<1>8'),
    (RC(r'i̋'), r'i\g<1>9'), (RC(r'I̋'), r'I\g<1>9'),
    (RC(r'ó͘'), r'oo\g<1>2'), (RC(r'Ó͘'), r'Oo\g<1>2'),
    (RC(r'ò͘'), r'oo\g<1>3'), (RC(r'Ò͘'), r'Oo\g<1>3'),
    (RC(r'ô͘'), r'oo\g<1>5'), (RC(r'Ô͘'), r'Oo\g<1>5'),
    (RC(r'ǒ͘'), r'oo\g<1>6'), (RC(r'Ǒ͘'), r'Oo\g<1>6'),
    (RC(r'ō͘'), r'oo\g<1>7'), (RC(r'Ō͘'), r'Oo\g<1>7'),
    (RC(r'o̍͘'), r'oo\g<1>8'), (RC(r'O̍͘'), r'Oo\g<1>8'),
    (RC(r'ő͘'), r'oo\g<1>9'), (RC(r'Ő͘'), r'Oo\g<1>9'),
    (RC(r'ó'), r'o\g<1>2'), (RC(r'Ó'), r'O\g<1>2'),
    (RC(r'ò'), r'o\g<1>3'), (RC(r'Ò'), r'O\g<1>3'),
    (RC(r'ô'), r'o\g<1>5'), (RC(r'Ô'), r'O\g<1>5'),
    (RC(r'ǒ'), r'o\g<1>6'), (RC(r'Ǒ'), r'O\g<1>6'),
    (RC(r'ō'), r'o\g<1>7'), (RC(r'Ō'), r'O\g<1>7'),
    (RC(r'o̍'), r'o\g<1>8'), (RC(r'O̍'), r'O\g<1>8'),
    (RC(r'ő'), r'o\g<1>9'), (RC(r'Ő'), r'O\g<1>9'),
    (RC(r'ú'), r'u\g<1>2'), (RC(r'Ú'), r'U\g<1>2'),
    (RC(r'ù'), r'u\g<1>3'), (RC(r'Ù'), r'U\g<1>3'),
    (RC(r'û'), r'u\g<1>5'), (RC(r'Û'), r'U\g<1>5'),
    (RC(r'ǔ'), r'u\g<1>6'), (RC(r'Ǔ'), r'U\g<1>6'),
    (RC(r'ū'), r'u\g<1>7'), (RC(r'Ū'), r'U\g<1>7'),
    (RC(r'u̍'), r'u\g<1>8'), (RC(r'U̍'), r'U\g<1>8'),
    (RC(r'ű'), r'u\g<1>9'), (RC(r'Ű'), r'U\g<1>9'),
    (RC(r'ḿ'), r'm\g<1>2'), (RC(r'Ḿ'), r'M\g<1>2'),
    (RC(r'm̀'), r'm\g<1>3'), (RC(r'M̀'), r'M\g<1>3'),
    (RC(r'm̂'), r'm\g<1>5'), (RC(r'M̂'), r'M\g<1>5'),
    (RC(r'm̌'), r'm\g<1>6'), (RC(r'M̌'), r'M\g<1>6'),
    (RC(r'm̄'), r'm\g<1>7'), (RC(r'M̄'), r'M\g<1>7'),
    (RC(r'm̍'), r'm\g<1>8'), (RC(r'M̍'), r'M\g<1>8'),
    (RC(r'm̋'), r'm\g<1>9'), (RC(r'M̋'), r'M\g<1>9'),
    (RC(r'ń'), r'n\g<1>2'), (RC(r'Ń'), r'N\g<1>2'),
    (RC(r'ǹ'), r'n\g<1>3'), (RC(r'Ǹ'), r'N\g<1>3'),
    (RC(r'n̂'), r'n\g<1>5'), (RC(r'N̂'), r'N\g<1>5'),
    (RC(r'ň'), r'n\g<1>6'), (RC(r'N̋'), r'N\g<1>6'),
    (RC(r'n̄'), r'n\g<1>7'), (RC(r'N̄'), r'N\g<1>7'),
    (RC(r'n̍'), r'n\g<1>8'), (RC(r'N̍'), r'N\g<1>8'),
    (RC(r'n̋'), r'n\g<1>9'), (RC(r'N̋'), r'N\g<1>9')
]

def TLtiau_2_TLsoo(tl_tiau, nasal='nn', use14=False):
    """台羅調符式 => 台羅數字式
       if nasal == 'N', change TL nasal nn to N
       else keep TL nasal nn intact
       if use14 == True, append digit 1/4 for tone1/4 syllable
       else keep tone1/4 syllables intact
    """
    if not tl_tiau:
        return ''

    tl_soo = tl_tiau 

    for tiauhusik, soojisik in TL_T2S:
        tl_soo = tiauhusik.sub(soojisik, tl_soo)

    tl_soo = re.sub(r'ⁿ', 'nn', tl_soo)

    if nasal == 'N':
        tl_soo = re.sub('(?<=[aeiouAEIOU])nn', 'N', tl_soo)

    if use14:
        add1 = re.compile(r'(a|A|e|E|i|I|o|O|u|U|m|M|ng|Ng|n)\b', re.A)
        add4 = re.compile(r'(h|p|t|k)\b', re.A)
        tl_soo = add1.sub(r'\g<1>1', tl_soo)
        tl_soo = add4.sub(r'\g<1>4', tl_soo)

    return tl_soo


#--------TLsoo_2_POJsoo---------------------------------------------------#

def TLsoo_2_POJsoo(tailo_soo, keep14=False):
    """ 台羅數字式 => 白話字數字式
        if keep14: keep TLsoo tone1/4 digit    
    """
    if not tailo_soo:
        return ''

    poj_soo = tailo_soo

    if not keep14:
        remove1 = re.compile('([aeiouAEIOU](?:nn|N)?|[aeiouAEIOU](?:ng|n|m)|'
                '(?:p|P|ph|Ph|m|M|b|B|t|T|th|Th|n|N|l|L|k|K|kh|Kh|ng|Ng|g|G|s|S|h|H)?(?:ng|Ng|m|M))1')
        poj_soo = remove1.sub(r'\1', poj_soo)
        remove4 = re.compile('([aeiouAEIOU](?:(?:nn|N)?h|p|t|k)|(?:m|M|ng|Ng)h)4')
        poj_soo = remove4.sub(r'\1', poj_soo)

    # TL has no oonn, just in case sb. uses it
    tailo2poj = [
        ('oonn', 'ouN'), ('Oonn', 'OuN'),
        ('onn', 'ouN'), ('Onn', 'OuN'),
        ('ts', 'ch'), ('Ts', 'Ch'), 
        ('oo', 'ou'), ('Oo', 'Ou'),
        ('ua', 'oa'), ('Ua', 'Oa'), ('ue', 'oe'), ('Ue', 'Oe'),
        ('ing', 'eng'), ('Ing', 'Eng'), ('ik', 'ek'), ('Ik', 'Ek'),
        ('nnh', 'hN'), ('Nh', 'hN'), ('hnn', 'hN')
    ]

    for k, v in tailo2poj:
        poj_soo = poj_soo.replace(k, v)

    nn_2_N = re.compile(r'([aeiouAEIOU])(?:nn|N)(h?\d?)\b', re.A)
    poj_soo = nn_2_N.sub(r'\1N\2', poj_soo)

    return poj_soo


#--------POJsoo_2_POJtiau----------------------------------------------------#

def POJsoo_2_POJtiau(poj_soo):

    # 白話字音節尾. POJ無用著 r，但是來自TL个資料可能會用著
    TL_bue = '((?:rm|rng|rn|r|m|ng|n|hN|N|ⁿ|nn)?)'

    # 處理非入聲
    def RC1(tailo):
        return re.compile(tailo[:-1] + TL_bue + tailo[-1])

    # 用佇 ai|au|ui 因為調號囥佇頭前个雙母音，著愛另外處理
    def RC2(tailo):
        return re.compile(tailo[0] + '(u|i)((?:N|ⁿ|nn)?)' + tailo[1])

    # 簡單情形
    def RC3(tailo):
        return re.compile(tailo, re.A)

    # 處理第四聲
    def RC4(tailo):
        return re.compile(tailo[:-1] + '(h(?:N|ⁿ|nn)?|p|t|k)' + tailo[-1] + '?')

    # 處理第八聲
    def RC8(tailo):
        return re.compile(tailo[:-1] + r'(h(?:N|ⁿ|nn)?|p|t|k)' + tailo[-1])

    # 白話字(TL)數字(Sooji)式 -> 白話字調符(Tiauhu)式 mapping
    POJ_S2T = [
        # use RC2
        (RC2('a1'), r'a\1\2'), (RC2('A1'), r'A\1\2'),
        (RC2('a2'), r'á\1\2'), (RC2('A2'), r'Á\1\2'),
        (RC2('a3'), r'à\1\2'), (RC2('A3'), r'À\1\2'),
        # use RC3
        (RC3('a(i|u)((?:N|ⁿ|nn)?)h4'), r'a\1\2h'),
        (RC3('A(i|u)((?:N|ⁿ|nn)?)h4'), r'A\1\2h'),
        # use RC2
        (RC2('a5'), r'â\1\2'), (RC2('A5'), r'Â\1\2'),
        (RC2('a6'), r'ǎ\1\2'), (RC2('A6'), r'Ǎ\1\2'),
        (RC2('a7'), r'ā\1\2'), (RC2('A7'), r'Ā\1\2'),
        # use RC3
        (RC3('a(i|u)h(?:N|ⁿ|nn)8'), r'a̍\1hⁿ'),
        (RC3('A(i|u)h(?:N|ⁿ|nn)8'), r'A̍\1hⁿ'),
        (RC3('a(i|u)h8'), r'a̍\1h'),
        (RC3('A(i|u)h8'), r'A̍\1h'),
        # use RC2
        (RC2('a9'), r'ă\1\2'), (RC2('A9'), r'Ă\1\2'),

        # use RC2
        (RC2('u1'), r'u\1\2'), (RC2('U1'), r'U\1\2'),
        (RC2('u2'), r'ú\1\2'), (RC2('U2'), r'Ú\1\2'),
        (RC2('u3'), r'ù\1\2'), (RC2('U3'), r'Ù\1\2'),
        # use RC3
        (RC3('uih((?:N|ⁿ|nn)?)4'), r'uih\1'),
        (RC3('Uih((?:N|ⁿ|nn)?)4'), r'Uih\1'),
        # use RC2
        (RC2('u5'), r'û\1\2'), (RC2('U5'), r'Û\1\2'),
        (RC2('u6'), r'ǔ\1\2'), (RC2('U6'), r'Ǔ\1\2'),
        (RC2('u7'), r'ū\1\2'), (RC2('U7'), r'Ū\1\2'),
        # use RC3
        (RC3('uih((?:N|ⁿ|nn)?)8'), r'u̍ih\1'),
        (RC3('Uih((?:N|ⁿ|nn)?)8'), r'U̍ih\1'),
        # use RC2
        (RC2('u9'), r'ŭ\1\2'), (RC2('U9'), r'Ŭ\1\2'),

        # use RC3
        (RC3(r'(o|O)([ae])((?:N|ⁿ|nn)?)1?\b'), r'\1\2\3'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)2\b'), r'ó\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)2\b'), r'Ó\1'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)3\b'), r'ò\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)3\b'), r'Ò\1\2'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)5\b'), r'ô\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)5\b'), r'Ô\1\2'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)6\b'), r'ǒ\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)6\b'), r'Ǒ\1\2'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)7\b'), r'ō\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)7\b'), r'Ō\1\2'),
        (RC3(r'o([ae])((?:N|ⁿ|nn)?)9\b'), r'ŏ\1\2'),
        (RC3(r'O([ae])((?:N|ⁿ|nn)?)9\b'), r'Ŏ\1\2'),

        # use RC1
        (RC1('a1'), r'a\1'), (RC1('A1'), r'A\1'),
        (RC1('a2'), r'á\1'), (RC1('A2'), r'Á\1'),
        (RC1('a3'), r'à\1'), (RC1('A3'), r'À\1'),
        (RC4('a4'), r'a\1'), (RC4('A4'), r'A\1'),
        (RC1('a5'), r'â\1'), (RC1('A5'), r'Â\1'),
        (RC1('a6'), r'ǎ\1'), (RC1('A6'), r'Ǎ\1'),
        (RC1('a7'), r'ā\1'), (RC1('A7'), r'Ā\1'),
        (RC8('a8'), r'a̍\1'), (RC8('A8'), r'A̍\1'),
        (RC1('a9'), r'ă\1'), (RC1('A9'), r'Ă\1'),
        (RC1('e1'), r'e\1'), (RC1('E1'), r'E\1'),
        (RC1('e2'), r'é\1'), (RC1('E2'), r'É\1'),
        (RC1('e3'), r'è\1'), (RC1('E3'), r'È\1'),
        (RC4('e4'), r'e\1'), (RC4('E4'), r'E\1'),
        (RC1('e5'), r'ê\1'), (RC1('E5'), r'Ê\1'),
        (RC1('e6'), r'ě\1'), (RC1('E6'), r'Ě\1'),
        (RC1('e7'), r'ē\1'), (RC1('E7'), r'Ē\1'),
        (RC8('e8'), r'e̍\1'), (RC8('E8'), r'E̍\1'),
        (RC1('e9'), r'ĕ\1'), (RC1('E9'), r'Ĕ\1'),
        (RC1('i1'), r'i\1'), (RC1('I1'), r'I\1'),
        (RC1('i2'), r'í\1'), (RC1('I2'), r'Í\1'),
        (RC1('i3'), r'ì\1'), (RC1('I3'), r'Ì\1'),
        (RC4('i4'), r'i\1'), (RC4('I4'), r'I\1'),
        (RC1('i5'), r'î\1'), (RC1('I5'), r'Î\1'),
        (RC1('i6'), r'ǐ\1'), (RC1('I6'), r'Ǐ\1'),
        (RC1('i7'), r'ī\1'), (RC1('I7'), r'Ī\1'),
        (RC8('i8'), r'i̍\1'), (RC8('I8'), r'I̍\1'),
        (RC1('i9'), r'ĭ\1'), (RC1('I9'), r'Ĭ\1'),
        (RC1('ou1'), r'o͘\1'), (RC1('Oo1'), r'Oo\1'),
        (RC1('ou2'), r'ó͘\1'), (RC1('Oo2'), r'Ó͘\1'),
        (RC1('ou3'), r'ò͘\1'), (RC1('Oo3'), r'Ò͘\1'),
        (RC4('ou4'), r'o͘\1'), (RC4('Oo4'), r'O͘\1'),
        (RC1('ou5'), r'ô͘\1'), (RC1('Oo5'), r'Ô͘\1'),
        (RC1('ou6'), r'ǒ͘\1'), (RC1('Oo6'), r'Ǒ͘\1'),
        (RC1('ou7'), r'ō͘\1'), (RC1('Oo7'), r'Ō͘\1'),
        (RC8('ou8'), r'o̍͘\1'), (RC8('Oo8'), r'O̍͘\1'),
        (RC1('ou9'), r'ŏ͘\1'), (RC1('Oo9'), r'Ŏ͘\1'),
        (RC1('o1'), r'o\1'), (RC1('O1'), r'O\1'),
        (RC1('o2'), r'ó\1'), (RC1('O2'), r'Ó\1'),
        (RC1('o3'), r'ò\1'), (RC1('O3'), r'Ò\1'),
        (RC4('o4'), r'o\1'), (RC4('O4'), r'O\1'),
        (RC1('o5'), r'ô\1'), (RC1('O5'), r'Ô\1'),
        (RC1('o6'), r'ǒ\1'), (RC1('O6'), r'Ǒ\1'),
        (RC1('o7'), r'ō\1'), (RC1('O7'), r'Ō\1'),
        (RC8('o8'), r'o̍\1'), (RC8('O8'), r'O̍\1'),
        (RC1('o9'), r'ŏ\1'), (RC1('O9'), r'Ŏ\1'),
        (RC1('u1'), r'u\1'), (RC1('U1'), r'U\1'),
        (RC1('u2'), r'ú\1'), (RC1('U2'), r'Ú\1'),
        (RC1('u3'), r'ù\1'), (RC1('U3'), r'Ù\1'),
        (RC4('u4'), r'u\1'), (RC4('U4'), r'U\1'),
        (RC1('u5'), r'û\1'), (RC1('U5'), r'Û\1'),
        (RC1('u6'), r'ǔ\1'), (RC1('U6'), r'Ǔ\1'),
        (RC1('u7'), r'ū\1'), (RC1('U7'), r'Ū\1'),
        (RC8('u8'), r'u̍\1'), (RC8('U8'), r'U̍\1'),
        (RC1('u9'), r'ŭ\1'), (RC1('U9'), r'Ŭ\1'),

        # use RC3
        (RC3('m1'), r'm'), (RC3('M1'), r'M'),
        (RC3('m2'), r'ḿ'), (RC3('M2'), r'Ḿ'),
        (RC3('m3'), r'm̀'), (RC3('M3'), r'M̀'),
        (RC3('mh4'), r'mh'), (RC3('Mh4'), r'Mh'),
        (RC3('m5'), r'm̂'), (RC3('M5'), r'M̂'),
        (RC3('m6'), r'm̌'), (RC3('M6'), r'M̌'),
        (RC3('m7'), r'm̄'), (RC3('M7'), r'M̄'),
        (RC3('mh8'), r'm̍h'), (RC3('Mh8'), r'M̍h'),
        (RC3('m9'), r'm̆'), (RC3('M9'), r'M̆'),

        (RC3('ng1'), r'ng'), (RC3('Ng1'), r'Ng'),
        (RC3('ng2'), r'ńg'), (RC3('Ng2'), r'Ńg'),
        (RC3('ng3'), r'ǹg'), (RC3('Ng3'), r'Ǹg'),
        (RC3('ngh4'), r'ngh'), (RC3('Ngh4'), r'Ngh'),
        (RC3('ng5'), r'n̂g'), (RC3('Ng5'), r'N̂g'),
        (RC3('ng6'), r'ňg'), (RC3('Ng6'), r'Ňg'),
        (RC3('ng7'), r'n̄g'), (RC3('Ng7'), r'N̄g'),
        (RC3('ngh8'), r'n̍gh'), (RC3('Ngh8'), r'N̍gh'),
        (RC3('ng9'), r'n̆g'), (RC3('Ng9'), r'N̆g')
    ]

    if poj_soo == '':
        return ''
    poj_tiau = poj_soo

    N_2_n = re.compile(r'(?:N|nn)(\d?)\b', re.A)
    poj_tiau = N_2_n.sub(r'ⁿ\1', poj_tiau)

    #counter = 0
    for soojisik, tiauhusik in POJ_S2T:
        #counter += 1
        poj_tiau = soojisik.sub(tiauhusik, poj_tiau)
        #print('c(%d): %s' % (counter, poj_tiau))

    return poj_tiau



# class interface
class poj_tl(str):
    def __new__(cls, *args, **kw):
        return str.__new__(cls, *args, **kw)

    def pojt_pojs(self):
        return poj_tl(POJtiau_2_POJsoo(self))

    def pojs_tls(self):
        return poj_tl(POJsoo_2_TLsoo(self))

    def tls_tlt(self):
        return poj_tl(TLsoo_2_TLtiau(self))

    def tlt_tls(self):
        return poj_tl(TLtiau_2_TLsoo(self))

    def tls_pojs(self):
        return poj_tl(TLsoo_2_POJsoo(self))

    def pojs_pojt(self):
        return poj_tl(POJsoo_2_POJtiau(self))

    def pojt_tlt(self):
        return poj_tl(self).pojt_pojs().pojs_tls().tls_tlt()

    def tlt_pojt(self):
        return poj_tl(self).tlt_tls().tls_pojs().pojs_pojt()

    def __str__(self):
        return super().__str__()
        

if __name__ == '__main__':
    print("Run POJ_TL-test.py for testing.")
