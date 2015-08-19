# POJ_TL 白話字(POJ) vs. 台羅(TL) 轉換家私 Python3 模組 #
作者：潘科元  
版本：0.0.6-20150820  
授權：GNU General Public License, version 3.0 (GPL-3.0)

```
           pojt_pojs()              pojs_tls()            tls_tlt()
POJ調號式--------------->POJ數字式------------->TL數字式------------->TL調號式
  |      <--------------          <------------         <------------   |
  |        pojs_pojt()              tls_pojs()            tlt_tls()     |
  |                                                                     |
  |>--------------------->      pojt_tlt()     >----------------------->|
  |<---------------------<      tlt_pojt()     <-----------------------<|
```

Finished：前六个(pojt_pojs(), pojs_tls(), tls_tlt(), pojs_pojt(), tls_pojs(), tlt_tls())  
TODO: 直接實作 pojt_tlt(), tlt_pojt()。目前先透過前六个來進行間接轉換。

## Python3 程式呼法[khoo-huat]舉例 ##
```
#!/usr/bin/env python3

from POJ_TL import poj_tl

pojt = 'oaiⁿ oáiⁿ oàiⁿ oaihⁿ oâiⁿ oǎiⁿ oāiⁿ oa̍ihⁿ oăiⁿ'
# POJ調號式 轉做 POJ數字式: pojt_pojs()
print(poj_tl(pojt).pojt_pojs())
# =>    oaiN oaiN2 oaiN3 oaihN oaiN5 oaiN6 oaiN7 oaihN8 oaiN9

pojs = 'oaiN oaiN2 oaiN3 oaihN oaiN5 oaiN6 oaiN7 oaihN8 oaiN9'
# POJ數字式 轉做 TL數字式: pojs_tls()
print(poj_tl(pojs).pojs_tls())
# =>    uainn uainn2 uainn3 uainnh uainn5 uainn6 uainn7 uainnh8 uainn9  

tls = 'uainn uainn2 uainn3 uainnh uainn5 uainn6 uainn7 uainnh8 uainn9'
# TL數字式 轉做 TL調號式: tls_tlt()
print(poj_tl(tls).tls_tlt())
# =>   uainn uáinn uàinn uainnh uâinn uǎinn uāinn ua̍innh ua̋inn

pojt = 'oaiⁿ oáiⁿ oàiⁿ oaihⁿ oâiⁿ oǎiⁿ oāiⁿ oa̍ihⁿ oăiⁿ'
# POJ調號式 轉做 TL調號式: pojt_tlt()
print(poj_tl(pojt).pojt_tlt())
# =>    uainn uáinn uàinn uainnh uâinn uǎinn uāinn ua̍innh ua̋inn

tlt = 'uainn uáinn uàinn uainnh uâinn uǎinn uāinn ua̍innh ua̋inn'
# TL調號式 轉做 TL數字式: tlt_tls()
print(poj_tl(tlt).tlt_tls())
# =>   uainn uainn2 uainn3 uainnh uainn5 uainn6 uainn7 uainnh8 uainn9

tls = 'uainn uainn2 uainn3 uainnh uainn5 uainn6 uainn7 uainnh8 uainn9'
# TL數字式 轉做 POJ數字式: tls_pojs()
print(poj_tl(tls).tls_pojs())
# =>   oaiN oaiN2 oaiN3 oaihN oaiN5 oaiN6 oaiN7 oaihN8 oaiN9

pojs = 'oaiN oaiN2 oaiN3 oaihN oaiN5 oaiN6 oaiN7 oaihN8 oaiN9'
# POJ數字式 轉做 POJ調號式: pojs_pojt()
print(poj_tl(pojs).pojs_pojt())
# =>    oaiⁿ oáiⁿ oàiⁿ oaihⁿ oâiⁿ oǎiⁿ oāiⁿ oa̍ihⁿ oăiⁿ

tlt = 'uainn uáinn uàinn uainnh uâinn uǎinn uāinn ua̍innh ua̋inn'
# TL調號式 轉做 POJ調號式: tlt_pojt()
print(poj_tl(tlt).tlt_pojt())
# =>   oaiⁿ oáiⁿ oàiⁿ oaihⁿ oâiⁿ oǎiⁿ oāiⁿ oa̍ihⁿ oăiⁿ
