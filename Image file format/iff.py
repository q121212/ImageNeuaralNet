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

# Lybraries import part
from tkinter import *

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


def paint_image(canvas_width = 500, canvas_height = 500):
  '''Method for painting image. The dimensions of canvas (width and height) must be specified.'''

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
  '''Method for extractin image from painted image.'''

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

    
def main():
  # openimagefile('image.txt', 10)
  # save_image(generate_empty_image(50, 20), 'image2.txt')
  # save_image(openimagefile('image2.txt', 50), 'image3.txt')
  # draw_image_file('image4.txt', 500, 650, 650)
  # paint_image()
  # save_image(extract_image_from_painted_image('positions.txt'), 'image6.txt')
  # draw_image_file('image6.txt', max_image_w_value(extract_image_from_painted_image('positions.txt')),500,600)
  paint_image_and_save_to_file('image7.txt')
  draw_image_file('image7.txt', max_image_w_value(extract_image_from_painted_image('positions.txt')),500,600)

if __name__ == '__main__':
  main()