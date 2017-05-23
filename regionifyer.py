#!/usr/bin/python3
import sys
import urllib.request
import json
from datetime import datetime

ERR_MSG = 'Must provide a valid ip'
def crash():
  print(ERR_MSG)
  exit(1)

# def get_hi(mapping_to_match, mappings):

#   hi = 255
#   for mapping in mappings:
#     if mapping['ip_prefix'].split('.')[2] < hi and mapping

ip = sys.argv[1]
if type(ip) is not str: crash()
octets = ip.split('.')
if (len(octets) != 4): crash()

jsonResult = urllib.request.urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json").read().decode("utf-8")
mappings = json.loads(jsonResult)
dateChanged = datetime.strptime(mappings['createDate'], '%Y-%m-%d-%H-%M-%S')
print('IP map last updated: ' + str(dateChanged))
sys.stdout.write('Region is: ')

for mapping in list(
  filter(
      lambda x: x['service'] == 'EC2' and x['ip_prefix'] != None,
      mappings['prefixes']
    )
  ):
  matchOctets = mapping['ip_prefix'].split('.')
  if octets[0] == matchOctets[0] and octets[1] == matchOctets[1]:
    print(mapping['region'])
  else:
    #TODO: Fix it
    print('Not found')
