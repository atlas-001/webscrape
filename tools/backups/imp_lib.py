''' These are the imports for the program consolidated 
into one file for easier to read code down the road. 
'''
#. blahblahblahblahblahblahblahblahblahblah
'''
IMPORTANT: to install pyenchant for ubuntu check out 
$ sudo apt-get install -y libenchant-dev
$pip install pyenchant 
'''

import urllib.request, urllib.error, urllib.parse
import enchant #for the english dictionary
import html2text #for cleanup of html
import os
from collections import Counter
import json