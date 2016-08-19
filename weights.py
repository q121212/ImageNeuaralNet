#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This file defines methods for calculation main metrics for images.
Then this metrics need to recalculate in weights for different purposes and finally: metrics + thier weights need to use for neuron's calculations.
'''

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

def defining_weights_for_metrics(list_of_metrics, images):
  # sorted_by_value(list_of_metrics)
  pass



if __name__ == '__main__':
  #  

  pass
