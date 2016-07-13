#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
lib_path = os.path.abspath(os.path.join('..', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)


import iff, unittest


# Any methods of the class below that begin with "test" will be executed
# when the the class is run (by calling unittest.main()
class IffTestCase(unittest.TestCase):

  def test_transponse(self):
    self.assertEqual(iff.transponse([0,0,0,1,1,1],2), [[0,0],[0,1],[1,1]])
    

if __name__ == '__main__':
  unittest.main()