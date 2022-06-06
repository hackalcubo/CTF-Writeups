# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (default, Apr  9 2021, 19:21:03) 
# [GCC 10.2.1 20210110]
# Embedded file name: snek.py
# Compiled at: 2021-04-08 08:24:05
# Size of source mod 2**32: 834 bytes
"""
Written for RITSEC CTF 2021
Author: knif3
Flag: RITSEC{}

TODO: Finish this challenge
"""

class d(object):

    def __init__(self, password):
        self.password = password.encode()
        self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

    def __eq__(self, other):
        if self.password == bytes(self.decrypt):
            print('!flag')
            return True
        return False


x = input('Enter my name: ')
a = d(x)
if a == x:
    print('IS_THIS_THE_FLAG??')
    print('NOPE')
else:
    print('WRONG')
# okay decompiling snek.pyc
