import os
import codecs
import configparser
import time

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "2.ini")

print(configPath)

config1 = open(configPath)
nr = config1.read()
print(nr)


cf = configparser.ConfigParser()
cf.read(configPath)
cf.add_section('test11')
# cf.remove_section('test11')
cf.set('test11','name','mazhao')
cf.set('test11','age','271')
###########################
with open(configPath, 'w') as f:
    cf.write(f)
############################
# file = open(configPath,'w')
# cf.write('tewss')
# file.close()
############################

# aa = cf.has_section('test')
# bb = cf.get('test','age')
#
# print(aa)

