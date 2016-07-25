#!/usr/bin/python3
# -*- coding: utf-8 -*-
          
#my own image format file

# Чтобы наглядно можно было работать с нейронной сетью нужно уметь обрабатывать изображения. Но даже первое обращение к BMP, JPG, GIF, показывает, что хранение данных в этих форматах сделано непросто, или так описано, что понять это сложно. Чтобы нормально работать с изображениями - попробую сам создать свой формат изображений (который в дальнейшем может быть) преобразован в формат медиа-файлов в целом.


# Model
# HEADER + Descriptions
# CONTAINER + Archivation

#Also - need have a viewer of my own image file format

# a simple ver - Contentent is array (list) of pixel +  their colors:
# a first variation is black\white variation. If Black is 1, White is 0 then image data is a simle array. but need define a width and height of Image: Its can be resolved via using nested array (array of arrays), the nested arrays is a horisontal lines in pictures
# image = \
# [[0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0]]
# Current iff structure was extended a iff header block!!

'''Image file format library.'''

__author__ = 'q121212@gmail.com (Max R.)'


# Lybraries import part
try:
  from tkinter import *
except ImportError:
  print('Tkinter library is not available.')
  exit(0)


def transponse(data, width):
  '''A function do transponse from single-order list to double-order list. 
A func have 2 variables: data, width.'''

  count = 0
  new_data_line = []
  new_data = []
  for i in data:
    if count < width:
      new_data_line.append(int(i))
      count+=1
    else:
      new_data.append(new_data_line)
      new_data_line = []
      new_data_line.append(int(i))
      count=1
    
  new_data.append(new_data_line)
  return new_data

 
def openimagefile(filename, width):
  '''Method for opening filename with a width as an image.'''

  with open(filename, 'r') as f:
    data = f.read()


  data=data.split(',')
  new_data = transponse(data, width)
  print('A file: ' + filename + ' was opened.')
  print('Image width:  {0}, height: {1}'.format(width, str(len(new_data))))
  print('Image size: ' + str(len(data)))
  return new_data


def generate_empty_image(width, height):
  '''Method for generation empty image with dimensions: width, height'''

  image = []
  for i in range(height):
    for j in range(width):
      image.append(0)
  
  data = image
  new_data = transponse(data, width)
  print('Image with demensions: {0} x {1} (width x height) was generated'.format(width, height))
  print('Image size: ' + str(len(image)))
  return new_data
  
def save_image(image, filename):
  '''Method for saving image to a file with a filename.'''

  with open(filename, 'w') as f:
    for i in range(len(image)):
      for j in range(len(image[i])):
        if i == len(image)-1 and j == len(image[i])-1:
          f.write(str(image[i][j]))
        else:
          f.write(str(image[i][j])+',')
  print('A file was written as: ' + filename)
  
  
def draw_image_file(filename, image_width, canvas_width = 500, canvas_height = 500):
  '''Method foк showing/displaying image from file with filename. Until a image file object doesn't keep its own width, this method require a image_width, and also canvas_width and canvas_height for image displaying.'''

  master = Tk()
  w = Canvas(master, 
             width=canvas_width, 
             height=canvas_height)
  w.pack()
  image = openimagefile(filename, image_width)
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()    

def draw_image(image, image_width, canvas_width = 500, canvas_height = 500):
  '''Method foк showing/displaying image. Until a image file object doesn't keep its own width, this method require a image_width, and also canvas_width and canvas_height for image displaying.'''

  master = Tk()
  w = Canvas(master, 
             width=canvas_width, 
             height=canvas_height)
  w.pack()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()    
  
  
def paint_image(canvas_width = 500, canvas_height = 500):
  '''Method for painting b\w image. The dimensions of canvas (width and height) must be specified.'''

  with open('positions.txt', 'w') as f:
    f.close()
    def paint_pixel_for_image( event ):
      with open('positions.txt', 'a') as f:
        python_green = "#476042"
        x, y = ( event.x ), ( event.y )
        w.create_oval( x, y, x, y, fill = python_green )
        result = [x, y]
        print(result)
        f.write(str(result[0]) + ' ' + str(result[1]) + ',')
        return result
  master = Tk()
  master.title( "Painting canvas" )
  w = Canvas(master, 
             width=canvas_width, 
             height=canvas_height)
  w.pack(expand = YES, fill = BOTH)
  arr = []
  w.bind( "<B1-Motion>", paint_pixel_for_image )

  message = Label( master, text = "Press and Drag the mouse to draw" )
  message.pack( side = BOTTOM )
      
  mainloop()

  
def extract_image_from_painted_image(drawed_image_filename):
  '''Method for extractin image from painted image. That's method uses drawed_image (not image), i.e. positions.txt'''

  with open(drawed_image_filename, 'r') as f:
    data = f.read().rstrip(',').split(',')
    coords_data = []
    for i in data:
	    coords_data.append(i.split(' '))
    
    new_coords_data = []
    min_w_value = 10**12
    max_w_value = 0
    min_h_value = 10**12
    max_h_value = 0
    counter = 1

    for i in range(len(coords_data)):
      for j in range(len(coords_data[i])):
        new_coords_data.append(int(coords_data[i][j]))
        if counter%2 == 0:
          if new_coords_data[-1] > max_h_value:
            max_h_value = new_coords_data[-1]
          if new_coords_data[-1] < min_h_value:
            min_h_value = new_coords_data[-1]
        else:
          if new_coords_data[-1] > max_w_value:
            max_w_value = new_coords_data[-1]
          if new_coords_data[-1] < min_w_value:
            min_w_value = new_coords_data[-1]     
        
        counter+=1
      
    image = generate_empty_image(max_w_value,max_h_value)
    
    x_array = []
    y_array = []
    for i in range(len(new_coords_data)):
      if i%2 == 0:
        x_array.append(new_coords_data[i])
      else:
        y_array.append(new_coords_data[i])
    
    print(x_array, y_array)
    for i in range(len(x_array)):
      image[y_array[i]-1][x_array[i]-1] = 1
       
    return image

def max_image_w_value(image):
  '''Method for defining a max width value of image.'''

  return len(image[0])
  

def max_image_h_value(image):
  '''Method for defining a max height value of image.'''

  return len(image)
    

def paint_image_and_save_to_file(filename):
  '''Method for painting image and save it to the file with filename.'''

  paint_image()
  save_image(extract_image_from_painted_image('positions.txt'), filename)



def image_structure(image, image_width):
  '''Method defines the current structure of image file: image_header_section|image_width|image.'''
  image_header_section = 'imgff'
  separator = '|'
  image_in_str = ''
  for i in range(len(image)):
      for j in range(len(image[i])):
        if i == len(image)-1 and j == len(image[i])-1:
          image_in_str = image_in_str + str(image[i][j])
        else:
          image_in_str = image_in_str + str(image[i][j])+','
          
  result = image_header_section+separator+str(image_width)+separator+image_in_str
  return result


def save_image_with_metadata(image, image_width, filename):
  '''Method for saving image from image file with metadata.'''
  with open(filename, 'w') as f:
    f.write(image_structure(image,image_width))


def extract_image_from_image_with_metadata(filename):
  '''Method for extracting image from image file with metadata.'''
  with open(filename, 'r') as f:
    data = f.read()
  
  data = data.split('|')[-1].split(',')
  image = transponse(data, extract_image_width_from_image_with_metadata(filename))
  return image


def extract_image_width_from_image_with_metadata(filename):
  '''Method for extracting image_width from image file with metadata.'''
  
  with open(filename, 'r') as f:
    data = f.read()
    
  return int(data.split('|')[1])


def transponse_two_to_one_ordered_list(image):
  '''Method for transponse image (two ordered list) to one orderedlist.'''

  oneorderedlist = []
  for i in range(len(image)):
    for j in range(len(image[i])):
      oneorderedlist.append(image[i][j]) 
      
  return oneorderedlist
  
  
def paint_image_new(canvas_width = 500, canvas_height = 500):
  '''New, reprocessed method for painting b\w image (w\o 'positions.txt' file). The dimensions of canvas (width and height) may be passed optionally.'''

  # with open('positions.txt', 'w') as f:
    # f.close()
  positions = []
  def paint_pixel_for_image( event ):
    # with open('positions.txt', 'a') as f:
    python_green = "#476042"
    x, y = ( event.x ), ( event.y )
    w.create_oval( x, y, x, y, fill = python_green )
    result = [x, y]
    print(result)
    positions.append([result[0], result[1]])
    return result
  master = Tk()
  master.title( "Painting canvas" )
  w = Canvas(master, 
             width=canvas_width, 
             height=canvas_height)
  w.pack(expand = YES, fill = BOTH)
  arr = []
  w.bind( "<B1-Motion>", paint_pixel_for_image )

  message = Label( master, text = "Press and Drag the mouse to draw" )
  message.pack( side = BOTTOM )
      
  mainloop()
# this place comes into operation after the closure of the drawing window!!

  coords_data = positions
  new_coords_data = []
  min_w_value = 10**12
  max_w_value = 0
  min_h_value = 10**12
  max_h_value = 0
  counter = 1

  for i in range(len(coords_data)):
    for j in range(len(coords_data[i])):
      new_coords_data.append(int(coords_data[i][j]))
      if counter%2 == 0:
        if new_coords_data[-1] > max_h_value:
          max_h_value = new_coords_data[-1]
        if new_coords_data[-1] < min_h_value:
          min_h_value = new_coords_data[-1]
      else:
        if new_coords_data[-1] > max_w_value:
          max_w_value = new_coords_data[-1]
        if new_coords_data[-1] < min_w_value:
          min_w_value = new_coords_data[-1]     
      
      counter+=1
    
  image = generate_empty_image(max_w_value,max_h_value)
  
  x_array = []
  y_array = []
  for i in range(len(new_coords_data)):
    if i%2 == 0:
      x_array.append(new_coords_data[i])
    else:
      y_array.append(new_coords_data[i])
  
  print(x_array, y_array)
  for i in range(len(x_array)):
    image[y_array[i]-1][x_array[i]-1] = 1
     
  return image


def paint_image_new_and_save_image_with_metadata(filename, canvas_width = 500, canvas_height = 500):
  '''Method for painting image and saving it to image with metadata.'''
  
  image = paint_image_new(canvas_width, canvas_height)
  save_image_with_metadata(image, max_image_w_value(image), filename)


def draw_image_file_with_metadata(filename):
  '''Method for showing/displaying image with metadata.'''

  image = extract_image_from_image_with_metadata(filename)
  canvas_width = max_image_w_value(image)
  canvas_height = max_image_h_value(image)
  
  master = Tk()
  # value +50 is a random number for creating a frame (additional canvas space) for a more presentable view of image. In the future this values change to min_w_value & min_h_value (need calculate them (find where calculations are made and use it))
  w = Canvas(master, 
             width=canvas_width+50, 
             height=canvas_height+50)
  w.pack()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()  

def transform_image_to_zeroes_sequence_and_dec_number(image):
  '''Method for transforming image to zeroes sequence and decimal number. It's used for bin to dec compression.'''
  bin_list = transponse_two_to_one_ordered_list(image)
  bin_sequence = ''
  for i in bin_list:
    bin_sequence+=str(i)
  numbers_of_zeroes = len(bin_list)-len(bin_sequence.lstrip('0'))
  # print('len(bin_list): {0}, len(bin_sequence): {1}, numbers_of_zeroes: {2}, bin_sequence: {3}, type(bin_sequence): {4}'.format(len(bin_list), len(bin_sequence.lstrip('0')), numbers_of_zeroes, bin_sequence, type(bin_sequence)))
  # print(bin_sequence, type(bin_sequence))
  dec_number = int(bin_sequence, 2)  
  zeroes_and_dec_number = [numbers_of_zeroes, dec_number]
  return zeroes_and_dec_number

def resave_from_image_file_to_image_with_compression(source_filename, result_filename):
  '''Method for update (resave) image file from structures iff with metadata to iff with bin_to_dec compression.'''
  image = extract_image_from_image_with_metadata(source_filename)
  image_width = extract_image_width_from_image_with_metadata(source_filename)
  zeroes_and_dec_number = transform_image_to_zeroes_sequence_and_dec_number(image)
  with open(result_filename, 'w') as f:
    f.write(image_with_compression_structure(image,image_width))
  print('A file {0} was resaved to {1}'.format(source_filename, result_filename))

def image_with_compression_structure(image, image_width):
  '''Method defines the current structure of image with bin_to_dec compression file: image_header_section|image_width|image_with_bin_to_dec_compression.'''
  image_header_section = 'imgffwdc' #a decript: image file format with decimal compression
  separator = '|'
  zeroes_and_dec_number = transform_image_to_zeroes_sequence_and_dec_number(image)
  image_in_str = str(zeroes_and_dec_number[0]) + ',' + str(zeroes_and_dec_number[1])
            
  result = image_header_section+separator+str(image_width)+separator+image_in_str
  return result


def extract_image_from_compressed_image_file(filename):
  '''Method for extracting image from bin_to_dec compressed image file.'''
  with open(filename, 'r') as f:
    data = f.read()
  
  zeroes_and_dec_number = data.split('|')[-1].split(',')
  dec_number = zeroes_and_dec_number[1]
  data_sequence = '0' * int(zeroes_and_dec_number[0]) + bin(int(dec_number))[2:]
  image = transponse(data_sequence, extract_image_width_from_image_with_metadata(filename))
  return image
  
  
def draw_image_file_with_compression(filename):
  '''Method for showing/displaying image with bin_to_dec compression.'''

  image = extract_image_from_compressed_image_file(filename)
  canvas_width = max_image_w_value(image)
  canvas_height = max_image_h_value(image)
  
  master = Tk()
  # value +50 is a random number for creating a frame (additional canvas space) for a more presentable view of image. In the future this values change to min_w_value & min_h_value (need calculate them (find where calculations are made and use it))
  w = Canvas(master, 
             width=canvas_width+50, 
             height=canvas_height+50)
  w.pack()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()    


def extract_image_from_file(filename, width = 1):
  '''General method for extracting image from different files: bin file, image with metadata, image with bin_to_dec compression, colored image with and w\o compression.'''
  
  n = 15
  with open(filename, 'r') as fl:
    first_n_symbols_of_file  = fl.readlines()[0][:n]
  
  print(first_n_symbols_of_file)
  if first_n_symbols_of_file.startswith('0,0' or '0,1' or '1,1'):
    return openimagefile(filename, width)
  elif first_n_symbols_of_file.startswith('imgffwdc'):
    return extract_image_from_compressed_image_file(filename)  
  elif first_n_symbols_of_file.startswith('imgffwcac'):
    return extract_image_from_compressed_and_colors_image_file(filename)
  elif first_n_symbols_of_file.startswith('imgff'):
    return extract_image_from_image_with_metadata(filename)

def image_file_structure_with_compression_and_colors(image, image_width, compression_type, colors_mode):
  '''Method defines the current structure of image fiel with different types of compression and different modes of colors: image_header_section|image_width|compression type|colors mode|data.'''
  image_header_section = 'imgffwcac' #a decript: image file format with compression and colors
  separator = '|'
  # compression = no, colors = b\w
  if compression_type == 0 and colors_mode == 0:
    image_data = ''
    for i in range(len(image)):
      for j in range(len(image[i])):
        if i == len(image)-1 and j == len(image[i])-1:
          image_data = image_data + str(image[i][j])
        else:
          image_data = image_data + str(image[i][j])+','
    
  # compression = no, colors = rgb
  if compression_type == 0 and colors_mode == 1:
    #structure of rgb-colored non-compressed image: one pixel is [r,g,b], two pixels: [[r1,g1,b1],[r2,g2,b2]], image: [[[r1,g1,b1], [r2,g2,b2]], [[r3,g3,b3],[r4,g4,b4]]], for example: [[[0,1,2],[3,4,5]], [[6,7,8],[9,10,11]]]
    image_data = transponse_colors_image_to_hex_list(image)
    print('image_data {0}'.format(image_data))
    
  # compression = bin_to_dec, colors = b\w
  if compression_type == 1 and colors_mode == 0:
    zeroes_and_dec_number = transform_image_to_zeroes_sequence_and_dec_number(image)
    image_data = str(zeroes_and_dec_number[0]) + ',' + str(zeroes_and_dec_number[1])
    
  # compression = dec_to_hex, colors = rgb
  if compression_type == 1 and colors_mode == 1:
    colors_list = transponse_colors_image_to_hex_list(image)
    image_data = ''
    for i in colors_list.split('0x'):
      image_data += i + ','
    
    image_data = image_data[:-1]
  result = image_header_section + separator + str(image_width) + separator + str(compression_type) + separator + str(colors_mode) + separator + image_data
  return result

  
def transponse_colors_image_to_hex_list(image):
  '''Method for transponsing dec image colors to hex image colors.'''
  hex_list_colors = ''
  for i in range(len(image)):
    for j in range(len(image[i])):
      colors = image[i][j]
      hex_colors = ''
      for e in colors:
        hex_colors+=hex(int(e))
        
      hex_list_colors += hex_colors
  
  return hex_list_colors



def save_image_to_compressed_and_colors_image_file(image, image_width, filename, compression_type = 1, colors_mode = 0):
  '''Save image file with using image_file_structure_with_compression_and_colors. Default params: compression_type = 1, colors_mode = 0. For using different ones need to specify them specially.'''
  
  with open(filename, 'w') as f:
    f.write(image_file_structure_with_compression_and_colors(image, image_width, compression_type, colors_mode))
  
  
def extract_image_from_compressed_and_colors_image_file(filename):
    '''Method for extracting image from different types of image files: uncompressed & compressed, b\w & colors.'''
    
    with open(filename, 'r') as f:
      data = f.read()
    
    image_header = data.split('|')[0]
    compression_type = int(data.split('|')[2])
    colors_mode = int(data.split('|')[3])
    # check image_header
    try:
      image_header == 'imgffwcac'
    except ValueError:
      print('An incorrect file was passed.')
    else:
      # check compression_type
      try:
        compression_type in [0, 1] # 0 - an image file is uncompressed, 1 - an image file is bin_to_dec compressed
      except ValueError:
        print('An incorrect type of file compression was passed.')
      else:
        # check colors_mode
        try:
          colors_mode in [0, 1] # 0 - b/w, 1 - rgb
        except ValueError:
          print('An incorrect colors mode was passed.')
        else:
          if compression_type == 0 and colors_mode == 0:
            print('00')
            return extract_image_from_image_with_metadata(filename)
          if compression_type == 0 and colors_mode == 1:
            print('01')
            return extract_colored_image_from_file(filename)
          if (compression_type == 1 and colors_mode == 0):
            print('10')
            return extract_image_from_compressed_image_file(filename)
          if compression_type == 1 and colors_mode == 1:
            print('11')
            return extract_image_from_hex_compressed_colors_file(filename)


def extract_image_from_hex_compressed_colors_file(filename):
  '''Method for extracting image from dec_to_hex compressed colors image file.'''
  with open(filename, 'r') as f:
    data = f.read()
  
  image_width = int(data.split('|')[1])
  dec_colors_list = []
  hex_numbers = data.split('|')[-1].split(',')[1:]
  for i in hex_numbers:
    dec_colors_list.append(int(i, 16))
  
  image = transponse_colors(transponse_colors(dec_colors_list, 3), image_width)
  return image



def draw_image_file_with_compression_and_colors(filename):
  '''Method for showing/displaying b\w image with bin_to_dec compression.'''

  image = extract_image_from_compressed_and_colors_image_file(filename)
  canvas_width = max_image_w_value(image)
  canvas_height = max_image_h_value(image)
  print(canvas_width, canvas_height)
  
  master = Tk()
  # value +50 is a random number for creating a frame (additional canvas space) for a more presentable view of image. In the future this values change to min_w_value & min_h_value (need calculate them (find where calculations are made and use it))
  w = Canvas(master, 
             width=canvas_width+50, 
             height=canvas_height+50)
  w.pack()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()    

def extract_colored_image_from_file(filename):
  with open(filename) as f:
    data = f.read()
  
  image_width = int(data.split('|')[1])
  colors_list = data.split('|')[-1]
  colors_list = colors_list.split('0x')[1:]
  dec_colors_list = []
  for i in colors_list:
    dec_colors_list.append(int(i, 16))

  image = transponse_colors(dec_colors_list, 3)
  image = transponse_colors(image, image_width)
  return image
    

def transponse_colors(colors_list, width):
  '''A function do transponse from single-order list of colors to double-order list of colors. A func have 2 variables: data, width.'''

  count = 0
  new_data_list = []
  new_data = []
  for i in colors_list:
    if count < width:
      new_data_list.append(i)
      count+=1
    else:
      new_data.append(new_data_list)
      new_data_list = []
      new_data_list.append(i)
      count=1
    
  new_data.append(new_data_list)
  return new_data


def draw_image_from_file(filename, width = 10, canvas_width = 500, canvas_height = 600):
  '''General method for showing\drawing  different image files.'''
  
  n = 15
  with open(filename, 'r') as fl:
    first_n_symbols_of_file  = fl.readlines()[0][:n]
  
  print(first_n_symbols_of_file)
  if first_n_symbols_of_file.startswith('0,0' or '0,1' or '1,1'):
    image = openimagefile(filename, width)
    return draw_image(image, max_image_w_value(image), canvas_width, canvas_height)
  elif first_n_symbols_of_file.startswith('imgffwdc'):
    return draw_image_file_with_compression(filename)  
  elif first_n_symbols_of_file.startswith('imgffwcac'):
    return draw_an_image_file(filename)
  elif first_n_symbols_of_file.startswith('imgff'):
    return draw_image_file_with_metadata(filename)

    
def draw_an_image_file(filename):
  '''Method for routing opens "imgffwcac" (image with comresson and colored) files. '''
  with open(filename, 'r') as f:
    data = f.read()
  
  image_header = data.split('|')[0]
  compression_type = int(data.split('|')[2])
  colors_mode = int(data.split('|')[3])
  # check image_header
  try:
    image_header == 'imgffwcac'
  except ValueError:
    print('An incorrect file was passed.')
  else:
    # check compression_type
    try:
      compression_type in [0, 1] # 0 - an image file is uncompressed, 1 - an image file is bin_to_dec compressed
    except ValueError:
      print('An incorrect type of file compression was passed.')
    else:
      # check colors_mode
      try:
        colors_mode in [0, 1] # 0 - b/w, 1 - rgb
      except ValueError:
        print('An incorrect colors mode was passed.')
      else:
        if compression_type == 0 and colors_mode == 0:
          return draw_image_file_with_metadata(filename)
        if compression_type == 0 and colors_mode == 1:
          return draw_image_file_with_compression_and_colors(filename)
        if (compression_type == 1 and colors_mode == 0):
          return draw_colored_image_file(filename)
        if compression_type == 1 and colors_mode == 1:
          return draw_colored_image_file(filename)
          

def draw_colored_image_file(filename):
  '''Method for drawing\showing colored image file (uncompressed and hex compressed).'''
  
  image = extract_image_from_file(filename)
  with open(filename, 'r') as f:
    data = f.read()
  
  compression_type = int(data.split('|')[2])
  colors_mode = int(data.split('|')[3])
  if compression_type == 0: # uncompressed image
    if colors_mode == 0:
      pass 
    elif colors_mode == 1:
      pass
  elif compression_type == 1: #hex compressed image
    if colors_mode == 0:
      draw_image_file_with_compression(filename) 
    elif colors_mode == 1:
      pass
  
          
def main():
  # openimagefile('image.txt', 10)
  # save_image(generate_empty_image(50, 20), 'image2.txt')
  # save_image(openimagefile('image2.txt', 50), 'image3.txt')
  # draw_image_file('image4.txt', 500, 650, 650)
  # paint_image()
  # save_image(extract_image_from_painted_image('positions.txt'), 'image6.txt')
  # draw_image_file('image6.txt', max_image_w_value(extract_image_from_painted_image('positions.txt')),500,600)
  # paint_image_and_save_to_file('image7.txt')
  # draw_image_file('image7.txt', max_image_w_value(extract_image_from_painted_image('positions.txt')),500,600)
  # save_image_with_metadata(extract_image_from_painted_image('positions.txt'),max_image_w_value(extract_image_from_painted_image('positions.txt')),'imagewithmeta.txt')
  # extract_image_from_image_with_metadata('imagewithmeta.txt')
  # extract_image_width_from_image_with_metadata('imagewithmeta.txt')
  # save_image(extract_image_from_image_with_metadata('imagewithmeta.txt'), 'image8.txt')
  # draw_image_file('image8.txt', extract_image_width_from_image_with_metadata('imagewithmeta.txt'), 500, 600)
  # draw_image(extract_image_from_image_with_metadata('imagewithmeta.txt'), extract_image_width_from_image_with_metadata('imagewithmeta.txt'), 500, 600)
  # paint_image_new(500, 500)
  # paint_image_new_and_save_image_with_metadata('image9.txt', 500, 600)
  # draw_image_file_with_metadata('image9.txt')
  # print(transform_image_to_zeroes_sequence_and_dec_number(extract_image_from_image_with_metadata('image9.txt')))
  # print(extract_(transform_image_to_zeroes_sequence_and_dec_number(extract_image_from_image_with_metadata('image9.txt'))))
  # resave_from_image_file_to_image_with_compression('image9.txt', 'image10.txt')
  # print(extract_image_from_compressed_image_file('image10.txt'))
  # draw_image_file_with_compression('image10.txt')
  # draw_image_file_with_metadata(extract_image_from_file('image10.txt'))
  # draw_image_file_with_compression('image10.txt')
  # image = paint_image_new()
  # save_image_to_compressed_and_colors_image_file(image, max_image_w_value(image), 'image11.txt', 1, 0)
  # draw_image_file_with_compression_and_colors('image11.txt')
  # image2 = extract_image_from_compressed_and_colors_image_file('image11.txt')
  # draw_image(image2, max_image_w_value)
  # print(image_file_structure_with_compression_and_colors([[[0,1,2],[3,4,5],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]]], 3, 0, 1))
  # save_image_to_compressed_and_colors_image_file([[[0,1,2],[3,4,5],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]],[[18,19,20],[21,22,23],[24,25,26]],[[27,28,29],[30,31,32],[33,34,35]]], max_image_w_value([[[0,1,2],[3,4,5],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]],[[18,19,20],[21,22,23],[24,25,26]],[[27,28,29],[30,31,32],[33,34,35]]]), 'image12.txt', compression_type = 0, colors_mode = 1)
  # print(extract_colored_image_from_file('image12.txt'))
  # save_image_to_compressed_and_colors_image_file(extract_colored_image_from_file('image12.txt'), max_image_w_value(extract_colored_image_from_file('image12.txt')), 'image13.txt', compression_type = 0, colors_mode = 1)
  # print(extract_colored_image_from_file('image13.txt'))
  # save_image_to_compressed_and_colors_image_file(extract_colored_image_from_file('image13.txt'), max_image_w_value(extract_colored_image_from_file('image13.txt')), 'image14.txt', compression_type = 1, colors_mode = 1)
  # print(extract_image_from_compressed_and_colors_image_file('image14.txt'))
  # save_image_to_compressed_and_colors_image_file(extract_image_from_compressed_and_colors_image_file('image14.txt'), max_image_w_value(extract_image_from_compressed_and_colors_image_file('image14.txt')), 'image15.txt', compression_type = 1, colors_mode = 1)
  # print('extract_image_from_file image12.txt {0}'.format(extract_image_from_file('image12.txt')))
  # print('extract_image_from_file image14.txt {0}'.format(extract_image_from_file('image14.txt')))
  # print('extract_image_from_compressed_and_colors_image_file image12 {0}'.format(extract_image_from_compressed_and_colors_image_file('image12.txt')))
  # print('extract_colored_image_from_file image12 {0}'.format(extract_colored_image_from_file('image12.txt')))
  # draw_image_from_file('image.txt')
  # draw_image_from_file('image4.txt')
  # draw_image_from_file('image7.txt') # require width
  # draw_image_from_file('image8.txt') # require width
  # draw_image_from_file('image9.txt') # imgff
  # draw_image_from_file('image10.txt') # imgffwdc
  
  # starts from image12 - its colored files!
  # draw_image_from_file('image12.txt')
  # draw_image_from_file('image13.txt')
  # draw_image_from_file('image14.txt')
  # draw_image_from_file('image15.txt')
  # image = paint_image_new()
  # save_image_to_compressed_and_colors_image_file(image, max_image_w_value(image), 'image15.txt', compression_type = 0, colors_mode = 0)
  # draw_image_from_file('image15.txt')
  # save_image_to_compressed_and_colors_image_file(image, max_image_w_value(image), 'image16.txt', compression_type = 0, colors_mode = 0)
  # draw_image_from_file('image16.txt')
  draw_image_from_file('../Models/2/image0.iff')
  print(max_image_h_value(extract_image_from_compressed_and_colors_image_file('../Models/2/image1.iff')))
  pass

if __name__ == '__main__':
  main()