# -*- coding: utf-8 -*- 

import urllib 
import urllib2 
import cookielib 
import string 
import re,sys
import random,time
import ctypes
reload(sys)
sys.setdefaultencoding("utf-8")


uri='http://music.tudou.com/theshow/index.html'


request = urllib2.Request(uri)  
response = urllib2.urlopen(request).read()
response=''.join(response.split('\n'))
# print response

f1 = file('data.txt',"w")

f1.write('视频播放数\n')
data1= re.findall("视频播放数：.*?orange\">(.*?)<",response,re.I)
for x in data1:
    f1.write(str(x)+'\n')
f1.write('\n')

f1.write('付费送礼数\n')
data2= re.findall("付费送礼数：.*?red\">(.*?)<",response,re.I)
for x in data2:
    f1.write(str(x)+'\n')
f1.write('\n')

f1.write('综合\n')
data3= re.findall("rock f_60  .*?\">(.*?)<",response,re.I)
for x in data3:
    f1.write(str(x)+'\n')
f1.write('\n')

f1.write('排名名字\n')
data4= re.findall("<a class=\"pic\".*?href=\".*?\" target=\"_blank\".*?title=\"(.*?)\">",response,re.I)
print data4
for x in data4:
    f1.write(str(x)+'\n')
f1.write('\n')

f1.write('X某值\n')
for x in xrange(20):
    f1.write(str(int(float(data1[x])*0.4+float(data2[x])*0.6))+'\n')
f1.write('\n')

f1.close()




