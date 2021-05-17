#! /usr/bin/env python3
import unittest
import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(root_folder)

from ..mqttCom import iot
from WareHouseFlask.config.py import DevConfig

'''
class TestMqtt(unittest.TestCase):
	def test_pub(self)
'''

if __name__ == '__main__':
	print(DevConfig)
    #unittest.main()