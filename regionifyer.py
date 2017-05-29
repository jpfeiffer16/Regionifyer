#!/usr/bin/python3
import sys
import urllib.request
import json
from datetime import datetime

ERR_MSG = 'Must provide a valid ip'
def crash():
  print(ERR_MSG)
  exit(1)

def get_hi(mapping_to_match, mappings):

  # hi = 255
  hi = {
    'ip_prefix': "13.32.255.0/15",
    'region': "GLOBAL",
    'service': "AWS"
  }
  print(hi)
  for mapping in mappings:
    if (mapping['ip_prefix'].split('.')[2] < hi['ip_prefix'].split('.')[2]) and (mapping['ip_prefix'].split('.')[2] > mapping_to_match['ip_prefix'].split('.')[2]):
      mapping = mapping
  return hi

ip = sys.argv[1]
if type(ip) is not str: crash()
octets = ip.split('.')
if (len(octets) != 4): crash()

jsonResult = urllib.request.urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json").read().decode("utf-8")
mappings = json.loads(jsonResult)
dateChanged = datetime.strptime(mappings['createDate'], '%Y-%m-%d-%H-%M-%S')
print('IP map last updated: ' + str(dateChanged))
sys.stdout.write('Region is: ')

aws_mappings = list(
filter(
    lambda x: x['service'] == 'EC2' and x['ip_prefix'] != None,
    mappings['prefixes']
  )
)

for mapping in aws_mappings:
  matchOctets = mapping['ip_prefix'].split('.')
  if octets[0] == matchOctets[0] and octets[1] == matchOctets[1]:
    print(mapping['region'])
  else:
    #TODO: Fix it
    print(get_hi(mapping, mappings))
