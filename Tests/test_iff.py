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
  

  def test_generate_empty_image(self):
    self.assertEqual(iff.generate_empty_image(3,4), [[0,0,0],[0,0,0],[0,0,0],[0,0,0]])  

  
  def test_image_structure(self):
    self.assertEqual(iff.image_structure(iff.generate_empty_image(2,3), 2), 'imgff|2|0,0,0,0,0,0')


  def test_max_image_w_value(self):
    self.assertEqual(iff.max_image_w_value(iff.generate_empty_image(5,6)), 5)


  def test_max_image_h_value(self):
    self.assertEqual(iff.max_image_h_value(iff.generate_empty_image(100,200)), 200)

  
  def test_transform_image_to_zeroes_sequence_and_dec_number(self):
    self.assertEqual(iff.transform_image_to_zeroes_sequence_and_dec_number([[0,0,0,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,1,1,1,1]]), [6, 10943]) 


  def test_image_with_compression_structure(self):
    self.assertEqual(iff.image_with_compression_structure([[0,0,0,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,1,1,1,1]], 5), 'imgffwdc|5|6,10943')


if __name__ == '__main__':
  unittest.main()