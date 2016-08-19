#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
lib_path = os.path.abspath(os.path.join('.', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Models/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Extract/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('.', 'Transform/'))
sys.path.insert(0, lib_path)

import iff
import models
import extract
import transform
import weights

def neuron_corner(path_to_images_folder):
  '''A handler for images from corner perspective.'''
  
  wghts = []
  for i in sorted(os.listdir(path_to_images_folder)):
    image = iff.extract_image_from_file(os.path.join(path_to_images_folder, i))
    wghts.append([i, weights.amount_corners_weight(image)])
  
  non_zeroes_wghts = []
  for i in wghts:
    if i[1] != [0,0,0,0,0]:
      non_zeroes_wghts.append(i)
  print('Non zeroes weight corner for reviewed images are the next: {0}'.format(non_zeroes_wghts))
  return wghts 

def normalization(neuron_output):
  pass




if __name__ == '__main__':
  #  
  path_to_images_folder = os.path.abspath(os.path.join('.', 'Models/plus'))

  neuron_corner(path_to_images_folder)

  pass
