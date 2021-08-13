# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:43:14 2021

@author: lxs_9
"""

import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    up, lo, sp, nu = 0, 0, 0, 0
    
    if not line:
        break
    for i in line:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
        elif i.isdigit():
            nu+=1
        elif i.isspace():
            sp+=1
        
    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))
