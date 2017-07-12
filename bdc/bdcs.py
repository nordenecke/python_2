# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:00:39 2017

@author: norden
"""

import re
import urllib
 
word=input('input a word\n')
  
url='http://dict.youdao.com/search?q=%s'%word
  
content=urllib.request.urlopen(url)
  
pattern=re.compile("</h2.*?</ul>",re.DOTALL)
content_text=content.read().decode('utf-8')  
result=pattern.search(content_text).group()
pattern2=re.compile('<li>.*?</li>')

for i in pattern2.findall(result):
  print(i.strip('<li>').strip('</li>'))
  
#add comments for test