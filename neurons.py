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
import metrics
import weights

def neuron_corner(path_to_images_folder):
  '''A handler for images from corner perspective.'''
  
  metrics_ = []
  for i in sorted(os.listdir(path_to_images_folder)):
    image = iff.extract_image_from_file(os.path.join(path_to_images_folder, i))
    metrics_.append([i, metrics.amount_corners_weight(image)])
  
  non_zeroes_metrics = []
  for i in metrics_:
    if i[1] != [0,0,0,0,0]:
      non_zeroes_metrics.append(i)
  print('Non zeroes corner metrics for reviewed images are the next: {0}'.format(non_zeroes_metrics))
  return metrics_ 

def normalization(neuron_output):
  pass




if __name__ == '__main__':
  #  
  path_to_images_folder = os.path.abspath(os.path.join('.', 'Models/plus'))

  neuron_corner(path_to_images_folder)

  pass
