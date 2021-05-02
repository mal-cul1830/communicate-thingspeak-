# -*- coding: utf-8 -*-
"""GetDataSendMessage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M0uY0XuHi8jVFzjMaGV3IXcdBvE5CUE7
"""

!pip install thingspeak
import urllib
from urllib.request import urlopen
import sys
from time import sleep
import thingspeak
import json

channel = thingspeak.Channel(1377861, api_key='68U094XXCY1QS75E',fmt = 'json');
pNo = 23
rNo = 454

while True:
  entry = float(json.loads(channel.get_field_last(1))['field1'])
  print(entry)
  if entry> 2.5: 
    continue
  elif entry >1.5:
    message = "Get bag ready, bag will soon need replacement!Patient" + str(pNo) + " Room No.:" + str(rNo) + + "_QUANTITY:"+ str(entry)
    print(message.replace(' ', '+'))
    requests.put('https://api.callmebot.com/whatsapp.php?phone=+917338240850&text='+message.replace(' ', '+')+'&apikey=366703')
    sleep(120)
  else:
    message = "EMERGENCY NEW BAG NEEDED!Patient" + str(pNo) + " Room No.:" + str(rNo) + "_QUANTITY:"+ str(entry)
    print(message.replace(' ', '+'))
    requests.put('https://api.callmebot.com/whatsapp.php?phone=+917338240850&text='+message.replace(' ', '+')+'&apikey=366703')
    sleep(120)

