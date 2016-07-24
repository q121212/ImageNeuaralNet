#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
lib_path = os.path.abspath(os.path.join('..', 'ImageFileFormat/'))
sys.path.insert(0, lib_path)


import iff

def model_paint_a_sign(sign, n):
  '''Method for painting n times a sign. This method is designed speccially to create/painting a models database of sign.'''

  current_path = os.path.abspath(os.path.join('.', str(sign)))
  
  # checking existence of folder. If  the folder doesn't exist - create it, in another case - do nothing.
  try: 
    os.mkdir(current_path) # create a folder, called as a sign
  except:
    pass

  additional_i = int(os.listdir(current_path)[-1][5:-4])
  for i in range(n+1):
    print('You need paint the next sign: {0}'.format(sign)) # message for painter
    image = iff.paint_image_new()
    path_to_imagefile = os.path.join(current_path, 'image' + str(i + additional_i) + '.iff')
    iff.save_image_to_compressed_and_colors_image_file(image, iff.max_image_w_value(image), path_to_imagefile, compression_type = 1, colors_mode = 0)
    iff.draw_image_from_file(path_to_imagefile)


def view_a_gallery_of_sign(sign, numbers_of_sign_examples=10, starts_with = 0):
  '''Method for sequential drawing image gallery.'''

  current_path = os.path.abspath(os.path.join('.', str(sign)))
  counter = 0
  for i in range(numbers_of_sign_examples):
    try:
      afilename = 'image' + str(i + starts_with) + '.iff'
      path_to_imagefile = os.path.join(current_path, afilename)
      iff.draw_image_from_file(path_to_imagefile)
      print('Was drawn: {0}'.format(afilename))
      counter+=1
    except:
      pass
  print('Gallery of {0} images was shown.'.format(counter))


def extract_sign_from_images(sign):
  
  current_path = os.path.abspath(os.path.join('.', str(sign)))
  number_of_files = int(os.listdir(current_path)[-1][5:-4]) #extract index of last image file in the sign_image folder
  
  generalizing_image = []

  list_of_images_and_their_widths = []
  for i in range(number_of_files+1):
    afilename = 'image' + str(i) + '.iff'
    path_to_imagefile = os.path.join(current_path, afilename)
    image = iff.extract_image_from_file(path_to_imagefile)

    # Below is 2 diagnostic lines
    print(path_to_imagefile)
    iff.draw_image(image, iff.max_image_w_value(image))

    list_of_images_and_their_widths.append([image, iff.max_image_w_value(image)]) # this list have the next format: [[image0, width0],[image1, width1]..]
    
  for i in range(len(list_of_images_and_their_widths)):
    generalizing_image.append(list_of_images_and_their_widths[i][1])

  # The following two methods that I need to write:
  # bring_images_to_common_width
  # search_a_common_in_images
    
  return generalizing_image


if __name__ == '__main__':
  # model_paint_a_sign(1, 4)
  # model_paint_a_sign(2, 4)
  # model_paint_a_sign('a', 4)
  # model_paint_a_sign('b', 4)
  # view_a_gallery_of_sign('1')
  print(extract_sign_from_images(2))

  pass