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
    # print(path_to_imagefile)
    # iff.draw_image(image, iff.max_image_w_value(image))

    list_of_images_and_their_widths.append([image, iff.max_image_w_value(image)]) # this list have the next format: [[image0, width0],[image1, width1]..]


  images_width = []  
  for i in range(len(list_of_images_and_their_widths)):
    images_width.append(list_of_images_and_their_widths[i][1])
  
  average_width = int(sum(images_width)/len(images_width))

  # The following two methods that I need to write:
  # bring_images_to_common_width
  # search_a_common_in_images
  
  ####resize_image###
  new_image_width = average_width
  for i in range(len(list_of_images_and_their_widths)):
    image = list_of_images_and_their_widths[i][0]
    image_width = list_of_images_and_their_widths[i][1]
    if image_width > new_image_width: # this case used special for unfinished method rezise_image
      pass
    else:
      print('new_image_width {0}'.format(new_image_width))
      new_image = fake_resize_image(image, image_width, new_image_width)
      print(len(new_image[0]))
      iff.draw_image(new_image, iff.max_image_w_value(new_image))
  
  ###################  
  return generalizing_image


def fake_resize_image(image, image_width, new_image_width):
  new_image = []
  if image_width == new_image_width:
    return image

  else:
    aspect_ratio = new_image_width / image_width
    width_difference = new_image_width - image_width
    print('width_difference {0}, new_image_width {1}, image_width {2}'.format(width_difference, new_image_width, image_width))
    if aspect_ratio >= 10:
      for i in range(len(image)):
        for j in range(len(image[i])):
          for e in range(int(aspect_ratio)):
            new_image.append(((str(image[i][j])+' ')*int(aspect_ratio)).split(' ')[:-1])
      #new_image*aspect_ratio
    elif 2<aspect_ratio<10:
      pass
      # new_image*
    elif 1 < aspect_ratio <= 2: # in this case: add a zeroes to end of every of image width line.
      for i in range(len(image)):
        for j in range(len(image[0])):
          new_image.append(image[i][j])
        for e in range(width_difference):
            new_image.append('0')
      new_image = iff.transponse(new_image, new_image_width)
      # print(iff.max_image_w_value(new_image), iff.max_image_h_value(new_image))
      # iff.draw_image(new_image, new_image_width)
      return new_image

    else:
      pass


def search_a_common_in_images(image1, image2):
  pass

if __name__ == '__main__':
  # model_paint_a_sign(1, 4)
  # model_paint_a_sign(2, 4)
  # model_paint_a_sign('a', 4)
  # model_paint_a_sign('b', 4)
  # view_a_gallery_of_sign('1')
  print(extract_sign_from_images('b'))

  pass