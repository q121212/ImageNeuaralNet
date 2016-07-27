#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
lib_path = os.path.abspath(os.path.join('..', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)

lib_path = os.path.abspath(os.path.join('..', 'Models/'))
sys.path.insert(0, lib_path)

import iff
import models

def extract_a_one_pixel_width_line_segments(filename):
  
  image = iff.extract_image_from_file(filename)
  
  'There are only three variants of line segment placement are possible: in horisontal line, vertical line and diagonal line. And, also in the each line can contain multiple segments'
  
  horizontal_lines_of_image = image
  
  # calculating vertical_lines_of_image (WARNING: need to check calculation and result correctness!!!!!!!)
  # method1 for calculation vertical_lines_of_image

  # print(iff.max_image_w_value(image), iff.max_image_h_value(image))
  vertical_lines_of_image_empty = iff.generate_empty_image(len(image), len(image[0]))
  vertical_lines_of_image = []
  for i in range(len(vertical_lines_of_image_empty)):
    for j in range(len(vertical_lines_of_image_empty[0])):
      vertical_lines_of_image_empty[i][j] = image[-j][i]
  
  vertical_lines_of_image = vertical_lines_of_image_empty
  
  # method2 for calculation vertical_lines_of_image
  image_one_ordered_list = iff.transponse_two_to_one_ordered_list(image)
  new_image_one_ordered_list = iff.transponse_two_to_one_ordered_list(vertical_lines_of_image_empty)
  for i in range(len(new_image_one_ordered_list)):
    new_image_one_ordered_list[i] = image[-i % iff.max_image_h_value(image)][i // iff.max_image_h_value(image)]
  
  new_image = iff.transponse(new_image_one_ordered_list, iff.max_image_h_value(image))
  # print(new_image)

  # calculating diagonal_lines_of_image
  # need to write!!!
  diagonal_lines_of_image = []
  

  # receiving horizontal_line_segments from horizontal_lines_of_image
  print('Horizontal lines segments: {0}'.format(line_segments(horizontal_lines_of_image))) #looks right

  # for method1 calculation of vertical_lines_of_image
  print('Vertical lines segments: {0}'.format(line_segments(vertical_lines_of_image))) # in vertical case: (WARNING: need to check calculation and result correctness!!!!!!!)
  
  # for method2 calculation of vertical_lines_of_image
  print('Vertical lines segments: {0}'.format(line_segments(new_image))) #Thats result was culculated for rotated to 90 degrees image. In fact thats cant used in ordinary way for drawing this segments. This segments need to rotate again to normal image!!!!!!!

  # print(new_image == vertical_lines_of_image) # check results: are equal the results of each of methods?

  iff.draw_image(image, len(image[0]))
  iff.draw_image(vertical_lines_of_image, len(vertical_lines_of_image[0]))
  # iff.draw_image(new_image, len(new_image[0])) # draw result image for calculation vertical_lines_of_image with method2

  a_line = []
  return a_line

def line_segments(lines_of_image): 
  # receiving line_segments from lines_of_image
  line_segments = []
  segments = []
  
  for i in range(len(lines_of_image)): # i is in height
    position_in_line = 0
    len_of_seg = 0
    counter = 0
    for j in lines_of_image[i]: # j is in width
      if j == 1:
        len_of_seg+=1
        if position_in_line == 0:
          position_in_line = counter
        else: 
          pass
        # if position_in_line == 0:
        #   position_in_line = j
        # else:
        #   pass
      else:
        if len_of_seg > 1:
          # format of unity in line_segments:
          # [number of string in image, start position for segment in string, len of segment]
          line_segments.append([i, position_in_line, len_of_seg])
        else:
          pass
        position_in_line = 0
        len_of_seg = 0
      counter += 1
  return line_segments


def add_line_segments_to_image(line_segments, image):
  pass


def draw_line_segments(line_segments):
  pass

if __name__ == '__main__':
  # extract_a_one_pixel_width_line_segments('image1.iff')
  # extract_a_one_pixel_width_line_segments('imageplus.iff')
  extract_a_one_pixel_width_line_segments('imageplus3.iff')
  # extract_a_one_pixel_width_line_segments('imageplus4.iff')


  pass