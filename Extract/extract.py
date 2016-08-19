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
  '''Method should extract list of lists of line segments (horizontal, vertical and diagonal) segments with length 2 and more pixels.'''
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
  image_height = len(image)
  image_width = len(image[0]) 
  for i in range(image_height):
    for j in range(image_width):
      if i == 0 and j == 0:
        pass
      elif i == j:
        diagonal_lines_of_image.append([image[i][0], image[0][j]])
      # elif i >= j and i-j>=0:
      #   diagonal_lines_of_image.append([image[i][0], image[0][j]])
      # elif i < j:
      #   diagonal_lines_of_image.append([image[i][0], image[0][j]])

  # receiving horizontal_line_segments from horizontal_lines_of_image
  horizontal_lines_segments = line_segments(horizontal_lines_of_image)
  print('Horizontal lines segments: {0}'.format(horizontal_lines_segments)) #looks right

  # for method1 calculation of vertical_lines_of_image
  vertical_lines_segments = line_segments(vertical_lines_of_image)
  print('Vertical lines segments: {0}'.format(vertical_lines_segments)) # in vertical case: (WARNING: need to check calculation and result correctness!!!!!!!)
  
  # for method2 calculation of vertical_lines_of_image
  print('Vertical lines segments: {0}'.format(line_segments(new_image))) #Thats result was culculated for rotated to 90 degrees image. In fact thats cant used in ordinary way for drawing this segments. This segments need to rotate again to normal image!!!!!!!

  # print(new_image == vertical_lines_of_image) # check results: are equal the results of each of methods?

  iff.draw_image(image, len(image[0]))
  iff.draw_image(vertical_lines_of_image, len(vertical_lines_of_image[0]))
  # iff.draw_image(new_image, len(new_image[0])) # draw result image for calculation vertical_lines_of_image with method2

  a_line = [horizontal_lines_segments, vertical_lines_segments]

  # print(extract_a_primitive(image, [[0,1,0,0,1,0,0,1,0],[0,1,0,0,1,0,0,1,0]])) #test example
  extract_a_primitive(vertical_lines_of_image, [[1,1]])
  return a_line

def line_segments(lines_of_image): 
  '''Receiving line_segments from lines_of_image'''
  
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
  '''Method for concantenation the image with line_segments to one image.'''
  pass


def draw_line_segments(line_segments):
  '''Method for drawing line_segments.'''
  pass


def extract_a_primitive(image, primitive):
  '''Abstract method for serch and extract an elements (primitives) from image.'''
  
  # primitive must be defined as list of lists. For example: [[1,1]] - a minimus segment with 2 pixels on placed on one line; [[0,1],[1,1]] - is a corner like this: _| placed on two lines.
  #
  #   image:       movable_window:
  #     (I)          (Template)
  #                    m = 2
  #      ----->        __
  #    j (w) = 5   n=1|__|
  #      _____
  # | 4 |     |     In this case,
  # |(h)|     |    template is [[1,1]], i.e.
  # | i |     |    is a 2 px segment
  # |   |_____|
  # V

  # First step of the method is - define an appropriate field (x*y) for Template (primitive) in Image.
  image_width = iff.max_image_w_value(image)
  image_height = iff.max_image_h_value(image)
  primitive_width = iff.max_image_w_value(primitive)
  primitive_height = iff.max_image_h_value(primitive)
  appropriate_field = [image_width - (primitive_width - 1), image_height - (primitive_height -1)]
  # print('image_width {0}, image_height {1}, primitive_width {2}, primitive_height {3}, appropriate_filed {4}'.format(image_width, image_height, primitive_width, primitive_height, appropriate_field))

  list_of_primitives_positions = []

  if appropriate_field[0] < 0:
    print('Width of primitive ({0}) is more than width of image!'.format(primitive))
    quit()
  if appropriate_field[1] < 0:
    print('Height of primitive ({0}) is more than height of image!'.format(primitive))
    quit()
  for i in range(appropriate_field[0]):
    for j in range(appropriate_field[1]):
      counter = 0
      primitive_positions = []
      for k in range(primitive_width):
        for l in range(primitive_height):
          # print('i: {0},j; {1},k: {2},l: {3}'.format(i,j,k,l))
          if image[j+l][i+k] == primitive[l][k]:
            counter+=1
            primitive_positions.append([i+k,j+l])
            if counter == primitive_width * primitive_height:
              list_of_primitives_positions.append(primitive_positions)
  
  print('Was extracted the next primitive: {0}'.format(primitive))
  print('List of primitives positions after extraction: {0}'.format(list_of_primitives_positions)) 
  return list_of_primitives_positions


def image_from_positions(list_of_positions):
  '''This method create an image from list of previously extracted positions of primitives or borders, etc.'''
  
  w_coords, h_coords = [], []
  for i in list_of_positions:
    w_coords.append(i[0]-1)
    h_coords.append(i[1]-1)

  # print(w_coords, '\n', h_coords)
  width = max(w_coords)
  height = max(h_coords)

  image = iff.generate_empty_image(width, height)
  for i in range(height):
    for j in range(width):
      for k in range(len(w_coords)):
        if h_coords[k] == i:
          if w_coords[k] == j:
            image[i][j] = 1
            # print(i,j)
            # print(h_coords[k], w_coords[k])
        else:
          if image[i][j] == 1:
            pass
          else: 
            image[i][j] = 0 
  # print(image)
  return image

def extract_a_border(image):
  '''Method for extracting a borders from image.'''
  
  list_of_border_positions = []

  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        counter = 0
        try:
          if image[i-1][j-1] == 1:
            counter += 1
        except:
          pass
        try:
          if image[i-1][j] == 1:
            counter += 1
        except:
          pass
        try:
          if image[i-1][j+1] == 1:
            counter += 1
        except:
          pass
        try:
          if image[i][j-1] == 1:
            counter += 1
        except:
          pass
        try:
          if image[i][j+1] == 1:
            counter +=1
        except:
          pass
        try:
          if image[i+1][j-1] == 1:
            counter +=1
        except:
          pass
        try:
          if image[i+1][j] == 1:
            counter +=1
        except:
          pass
        try:
          if image[i+1][j+1] == 1:
            counter +=1
        except:
          pass

        print('counter:  {0}'.format(counter))
        if counter == 8:
          pass
        else:
          list_of_border_positions.append([j,i])

  print('Was extracted the borders from image.')
  print('List of border positions after extraction: {0}'.format(list_of_border_positions)) 
  return list_of_border_positions


if __name__ == '__main__':
  # extract_a_one_pixel_width_line_segments('image1.iff')
  # extract_a_one_pixel_width_line_segments('imageplus.iff')
  # extract_a_one_pixel_width_line_segments('imageplus3.iff')
  # extract_a_one_pixel_width_line_segments('imageplus4.iff')
  # extract_a_primitive(iff.extract_image_from_file('imageplus3.iff'), primitive = [[1,0]])

  iff.draw_image_from_file('image_for_border_extraction.iff')
  list_of_border_positions = extract_a_border(iff.extract_image_from_file('image_for_border_extraction.iff'))
  image = image_from_positions(list_of_border_positions)
  iff.draw_image(image, iff.max_image_w_value(image))
  iff.save_image_to_compressed_and_colors_image_file(image, iff.max_image_w_value(image), 'image2.iff', compression_type = 0, colors_mode = 0)
  iff.draw_image_from_file('image2.iff')

  pass