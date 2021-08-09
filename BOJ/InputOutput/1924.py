# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:44:48 2021

@author: lxs_9
"""

weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
day = 0
for i in range(0, x-1):
    day += days[i]
    
day = (day+y)%7

print(weekdays[day])
