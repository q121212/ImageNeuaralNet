#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
lib_path = os.path.abspath(os.path.join('..', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('..', 'Models/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('..', 'Extract/'))
sys.path.insert(0, lib_path)

import iff
import models
import extract



def create_test_image():
  image = iff.paint_image_new()
  current_path = os.path.abspath('.')
  print(os.listdir(current_path))
  filename = input('Enter the filename for saving this image (without .iff), please: ')
  while filename + '.iff' in os.listdir(current_path): 
    filename = input('File with this filename: {0} already exists. Enter the another filename for saving this image (without .iff), please: '.format(filename))

  filename += '.iff'
      
  path_to_imagefile = os.path.join(current_path, filename)
  iff.save_image_to_compressed_and_colors_image_file(image, iff.max_image_w_value(image), path_to_imagefile, compression_type = 1, colors_mode = 0)
  print('This image was saved as: {0}'. format(filename))
  iff.draw_image_from_file(path_to_imagefile)


def data_preparation(*args):
  '''Method for preparating of data to transformations.'''
  results_images = []
  for image in args:
    results_images.append(iff.extract_image_from_file(image))

  return results_images

def horiz_summation(image_left, image_right):
  '''Method for creating horizontal summation of left and right images in the one.'''
  image_left_w_value  = iff.max_image_w_value(image_left)
  image_right_w_value = iff.max_image_w_value(image_right)
  image_left_h_value  = iff.max_image_h_value(image_left)
  image_right_h_value = iff.max_image_h_value(image_right)
  
  if image_left_w_value > image_right_w_value:
    new_w_value = image_left_w_value
  else:
    new_w_value = image_right_w_value

  if image_left_h_value > image_right_h_value:
    new_h_value = image_left_h_value
  else:
    new_h_value = image_right_h_value
  print(new_w_value, new_h_value)

  result_image = iff.generate_empty_image(image_left_w_value+image_right_w_value, new_h_value)
  for i in range(len(image_left)):
    for j in range(len(image_left[i])):
      result_image[i][j] = image_left[i][j]

  for i in range(len(image_right)):
    for j in range(len(image_right[i])):
      result_image[i][j+image_left_w_value] = image_right[i][j]
  # for i in range(new_h_value):
  #   if i < image_left_h_value:
  #     left_part  = image_left[i]
  #   else:
  #     left_part = result_image[i - image_left_h_value] 
    
  #   if i < image_right_h_value:
  #     right_part  = image_right[i]
  #   else:
  #     right_part = result_image[i - image_right_h_value] 
  #   result_image.append(left_part + right_part)

  iff.draw_image(result_image, iff.max_image_w_value(result_image))
  return result_image


def vert_summation(image_top, image_bottom):
  '''Method for creating horizontal summation of left and right images in the one.'''
  image_top_w_value  = iff.max_image_w_value(image_top)
  image_bottom_w_value = iff.max_image_w_value(image_bottom)
  image_top_h_value  = iff.max_image_h_value(image_top)
  image_bottom_h_value = iff.max_image_h_value(image_bottom)
  
  if image_top_w_value > image_bottom_w_value:
    new_w_value = image_top_w_value
  else:
    new_w_value = image_bottom_w_value

  if image_top_h_value > image_bottom_h_value:
    new_h_value = image_top_h_value
  else:
    new_h_value = image_bottom_h_value
  print(new_w_value, new_h_value)

  result_image = iff.generate_empty_image(new_w_value, image_top_h_value+image_bottom_h_value)
  for i in range(len(image_top)):
    for j in range(len(image_top[i])):
      result_image[i][j] = image_top[i][j]

  for i in range(len(image_bottom)):
    for j in range(len(image_bottom[i])):
      result_image[i+image_top_h_value][j] = image_bottom[i][j]
  iff.draw_image(result_image, iff.max_image_w_value(result_image))
  return result_image


if __name__ == '__main__':
  # create_test_image()
  images = data_preparation('m.iff', 'a.iff', 'x.iff')
  # for image in images:
  #   iff.draw_image(image, iff.max_image_w_value(image))
  horiz_summation(images[0], images[1])
  vert_summation(images[0], images[1])

  pass